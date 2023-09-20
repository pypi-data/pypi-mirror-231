import numpy as np
import re
import warnings
import csv
import datetime as dt
import os
from pythermalcomfort.psychrometrics import t_o, p_sat_torr, p_sat, psy_ta_rh
from pythermalcomfort.utilities import (
    units_converter,
    transpose_sharp_altitude,
    check_standard_compliance,
    mapping,
    check_standard_compliance_array,
    body_surface_area,
)
from pythermalcomfort.shared_functions import valid_range
import math
from scipy import optimize
from pythermalcomfort.optimized_functions import (
    two_nodes_optimized,
    phs_optimized,
    pmv_ppd_optimized,
    utci_optimized,
    two_nodes_optimized_return_set,
)

# import functions and valuables from "jos3_functions" folder
from pythermalcomfort.jos3_functions import thermoregulation as threg
from pythermalcomfort.jos3_functions import matrix
from pythermalcomfort.jos3_functions.matrix import (
    NUM_NODES,
    INDEX,
    VINDEX,
    BODY_NAMES,
    remove_body_name,
)
from pythermalcomfort.jos3_functions import construction as cons
from pythermalcomfort.jos3_functions.construction import _to17array
from pythermalcomfort.jos3_functions.parameters import Default, ALL_OUT_PARAMS
from pythermalcomfort.__init__ import __version__


def cooling_effect(tdb, tr, vr, rh, met, clo, wme=0, units="SI"):
    """Returns the value of the Cooling Effect (`CE`_) calculated in compliance
    with the ASHRAE 55 2020 Standard [1]_. The `CE`_ of the elevated air speed
    is the value that, when subtracted equally from both the average air
    temperature and the mean radiant temperature, yields the same `SET`_ under
    still air as in the first `SET`_ calculation under elevated air speed. The
    cooling effect is calculated only for air speed higher than 0.1 m/s.

    .. _CE: https://en.wikipedia.org/wiki/Thermal_comfort#Cooling_Effect

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float
        relative humidity, [%]
    met : float
        metabolic rate, [met]
    clo : float
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    wme : float, default 0
        external work, [met]
    units : {'SI', 'IP'}     select the SI (International System of Units) or the IP (Imperial Units) system.

    Returns
    -------
    ce : float
        Cooling Effect, default in [°C] in [°F] if `units` = 'IP'

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import cooling_effect
        >>> CE = cooling_effect(tdb=25, tr=25, vr=0.3, rh=50, met=1.2, clo=0.5)
        >>> print(CE)
        1.64

        >>> # for users who wants to use the IP system
        >>> CE = cooling_effect(tdb=77, tr=77, vr=1.64, rh=50, met=1, clo=0.6, units="IP")
        >>> print(CE)
        3.74

    Raises
    ------
    ValueError
        If the cooling effect could not be calculated
    """

    if units.lower() == "ip":
        tdb, tr, vr = units_converter(tdb=tdb, tr=tr, v=vr)

    if vr <= 0.1:
        return 0

    still_air_threshold = 0.1

    warnings.simplefilter("ignore")

    initial_set_tmp = set_tmp(
        tdb=tdb,
        tr=tr,
        v=vr,
        rh=rh,
        met=met,
        clo=clo,
        wme=wme,
        round=False,
        calculate_ce=True,
        limit_inputs=False,
    )

    def function(x):
        return (
            set_tmp(
                tdb - x,
                tr - x,
                v=still_air_threshold,
                rh=rh,
                met=met,
                clo=clo,
                wme=wme,
                round=False,
                calculate_ce=True,
                limit_inputs=False,
            )
            - initial_set_tmp
        )

    try:
        ce = optimize.brentq(function, 0.0, 40)
    except ValueError:
        ce = 0

    warnings.simplefilter("always")

    if ce == 0:
        warnings.warn(
            "Assuming cooling effect = 0 since it could not be calculated for this set"
            f" of inputs {tdb=}, {tr=}, {rh=}, {vr=}, {clo=}, {met=}",
            UserWarning,
        )

    if units.lower() == "ip":
        ce = ce / 1.8 * 3.28

    return round(ce, 2)


def pmv_ppd(tdb, tr, vr, rh, met, clo, wme=0, standard="ISO", **kwargs):
    """Returns Predicted Mean Vote (`PMV`_) and Predicted Percentage of
    Dissatisfied ( `PPD`_) calculated in accordance to main thermal comfort
    Standards. The PMV is an index that predicts the mean value of the thermal
    sensation votes (self-reported perceptions) of a large group of people on a
    sensation scale expressed from –3 to +3 corresponding to the categories:
    cold, cool, slightly cool, neutral, slightly warm, warm, and hot. [1]_

    While the PMV equation is the same for both the ISO and ASHRAE standards, in the
    ASHRAE 55 PMV equation, the SET is used to calculate the cooling effect first,
    this is then subtracted from both the air and mean radiant temperatures, and the
    differences are used as input to the PMV model, while the airspeed is set to 0.1m/s.
    Please read more in the Note below.

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float or array-like
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    clo : float or array-like
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently, the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    wme : float or array-like
        external work, [met] default 0
    standard : {"ISO", "ASHRAE"}
        comfort standard used for calculation

        - If "ISO", then the ISO Equation is used
        - If "ASHRAE", then the ASHRAE Equation is used

        Note: While the PMV equation is the same for both the ISO and ASHRAE standards,
        the ASHRAE Standard Use of the PMV model is limited to air speeds below 0.10
        m/s (20 fpm).
        When air speeds exceed 0.10 m/s (20 fpm), the comfort zone boundaries are
        adjusted based on the SET model.
        This change was indroduced by the `Addendum C to Standard 55-2020`_

    Other Parameters
    ----------------
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

        The ASHRAE 55 2020 limits are 10 < tdb [°C] < 40, 10 < tr [°C] < 40,
        0 < vr [m/s] < 2, 1 < met [met] < 4, and 0 < clo [clo] < 1.5.
        The ISO 7730 2005 limits are 10 < tdb [°C] < 30, 10 < tr [°C] < 40,
        0 < vr [m/s] < 1, 0.8 < met [met] < 4, 0 < clo [clo] < 2, and -2 < PMV < 2.
    airspeed_control : boolean default True
        This only applies if standard = "ASHRAE". By default it is assumed that the
        occupant has control over the airspeed. In this case the ASHRAE 55 Standard does
        not imposes any airspeed limits. On the other hand, if the occupant has no control
        over the airspeed the ASHRAE 55 imposes an upper limit for v which varies as a
        function of the operative temperature, for more information please consult the
        Standard.

    Returns
    -------
    pmv : float or array-like
        Predicted Mean Vote
    ppd : float or array-like
        Predicted Percentage of Dissatisfied occupants, [%]

    Notes
    -----
    You can use this function to calculate the `PMV`_ and `PPD`_ in accordance with
    either the ASHRAE 55 2020 Standard [1]_ or the ISO 7730 Standard [2]_.

    .. _PMV: https://en.wikipedia.org/wiki/Thermal_comfort#PMV/PPD_method
    .. _PPD: https://en.wikipedia.org/wiki/Thermal_comfort#PMV/PPD_method
    .. _Addendum C to Standard 55-2020: https://www.ashrae.org/file%20library/technical%20resources/standards%20and%20guidelines/standards%20addenda/55_2020_c_20210430.pdf

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import pmv_ppd
        >>> from pythermalcomfort.utilities import v_relative, clo_dynamic
        >>> tdb = 25
        >>> tr = 25
        >>> rh = 50
        >>> v = 0.1
        >>> met = 1.4
        >>> clo = 0.5
        >>> # calculate relative air speed
        >>> v_r = v_relative(v=v, met=met)
        >>> # calculate dynamic clothing
        >>> clo_d = clo_dynamic(clo=clo, met=met)
        >>> results = pmv_ppd(tdb=tdb, tr=tr, vr=v_r, rh=rh, met=met, clo=clo_d)
        >>> print(results)
        {'pmv': 0.06, 'ppd': 5.1}
        >>> print(results["pmv"])
        -0.06
        >>> # you can also pass an array-like of inputs
        >>> results = pmv_ppd(tdb=[22, 25], tr=tr, vr=v_r, rh=rh, met=met, clo=clo_d)
        >>> print(results)
        {'pmv': array([-0.47,  0.06]), 'ppd': array([9.6, 5.1])}

    Raises
    ------
    StopIteration
        Raised if the number of iterations exceeds the threshold
    ValueError
        The 'standard' function input parameter can only be 'ISO' or 'ASHRAE'
    """
    default_kwargs = {"units": "SI", "limit_inputs": True, "airspeed_control": True}
    kwargs = {**default_kwargs, **kwargs}

    tdb = np.array(tdb)
    tr = np.array(tr)
    vr = np.array(vr)
    met = np.array(met)
    clo = np.array(clo)
    wme = np.array(wme)

    if kwargs["units"].lower() == "ip":
        tdb, tr, vr = units_converter(tdb=tdb, tr=tr, v=vr)

    standard = standard.lower()
    if standard not in ["iso", "ashrae"]:
        raise ValueError(
            "PMV calculations can only be performed in compliance with ISO or ASHRAE "
            "Standards"
        )

    (
        tdb_valid,
        tr_valid,
        v_valid,
        met_valid,
        clo_valid,
    ) = check_standard_compliance_array(
        standard,
        tdb=tdb,
        tr=tr,
        v=vr,
        met=met,
        clo=clo,
        airspeed_control=kwargs["airspeed_control"],
    )

    # if v_r is higher than 0.1 follow methodology ASHRAE Appendix H, H3
    ce = 0.0
    if standard == "ashrae":
        ce = np.where(
            vr > 0.1,
            np.vectorize(cooling_effect, cache=True)(tdb, tr, vr, rh, met, clo, wme),
            0.0,
        )

    tdb = tdb - ce
    tr = tr - ce
    vr = np.where(ce > 0, 0.1, vr)

    pmv_array = pmv_ppd_optimized(tdb, tr, vr, rh, met, clo, wme)

    ppd_array = 100.0 - 95.0 * np.exp(
        -0.03353 * np.power(pmv_array, 4.0) - 0.2179 * np.power(pmv_array, 2.0)
    )

    # Checks that inputs are within the bounds accepted by the model if not return nan
    if kwargs["limit_inputs"]:
        pmv_valid = valid_range(pmv_array, (-2, 2))  # this is the ISO limit
        if standard == "ashrae":
            pmv_valid = valid_range(pmv_array, (-100, 100))

        all_valid = ~(
            np.isnan(tdb_valid)
            | np.isnan(tr_valid)
            | np.isnan(v_valid)
            | np.isnan(met_valid)
            | np.isnan(clo_valid)
            | np.isnan(pmv_valid)
        )
        pmv_array = np.where(all_valid, pmv_array, np.nan)
        ppd_array = np.where(all_valid, ppd_array, np.nan)

    return {
        "pmv": np.around(pmv_array, 2),
        "ppd": np.around(ppd_array, 1),
    }


def pmv(tdb, tr, vr, rh, met, clo, wme=0, standard="ISO", **kwargs):
    """Returns Predicted Mean Vote (`PMV`_) calculated in accordance to main
    thermal comfort Standards. The PMV is an index that predicts the mean value
    of the thermal sensation votes (self-reported perceptions) of a large group
    of people on a sensation scale expressed from –3 to +3 corresponding to the
    categories: cold, cool, slightly cool, neutral, slightly warm, warm, and hot. [1]_

    While the PMV equation is the same for both the ISO and ASHRAE standards, in the
    ASHRAE 55 PMV equation, the SET is used to calculate the cooling effect first,
    this is then subtracted from both the air and mean radiant temperatures, and the
    differences are used as input to the PMV model, while the airspeed is set to 0.1m/s.
    Please read more in the Note below.

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float or array-like
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    clo : float or array-like
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently, the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    wme : float or array-like
        external work, [met] default 0
    standard : {"ISO", "ASHRAE"}
        comfort standard used for calculation

        - If "ISO", then the ISO Equation is used
        - If "ASHRAE", then the ASHRAE Equation is used

        Note: While the PMV equation is the same for both the ISO and ASHRAE standards,
        the ASHRAE Standard Use of the PMV model is limited to air speeds below 0.10
        m/s (20 fpm).
        When air speeds exceed 0.10 m/s (20 fpm), the comfort zone boundaries are
        adjusted based on the SET model.
        This change was indroduced by the `Addendum C to Standard 55-2020`_

    Other Parameters
    ----------------
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

        The ASHRAE 55 2020 limits are 10 < tdb [°C] < 40, 10 < tr [°C] < 40,
        0 < vr [m/s] < 2, 1 < met [met] < 4, and 0 < clo [clo] < 1.5.
        The ISO 7730 2005 limits are 10 < tdb [°C] < 30, 10 < tr [°C] < 40,
        0 < vr [m/s] < 1, 0.8 < met [met] < 4, 0 < clo [clo] < 2, and -2 < PMV < 2.
    airspeed_control : boolean default True
        This only applies if standard = "ASHRAE". By default it is assumed that the
        occupant has control over the airspeed. In this case the ASHRAE 55 Standard does
        not impose any airspeed limits. On the other hand, if the occupant has no control
        over the airspeed the ASHRAE 55 imposes an upper limit for v which varies as a
        function of the operative temperature, for more information please consult the
        Standard.

    Returns
    -------
    pmv : float or array-like
        Predicted Mean Vote

    Notes
    -----
    You can use this function to calculate the `PMV`_ [1]_ [2]_.

    .. _PMV: https://en.wikipedia.org/wiki/Thermal_comfort#PMV/PPD_method
    .. _Addendum C to Standard 55-2020: https://www.ashrae.org/file%20library/technical%20resources/standards%20and%20guidelines/standards%20addenda/55_2020_c_20210430.pdf

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import pmv
        >>> from pythermalcomfort.utilities import v_relative, clo_dynamic
        >>> tdb = 25
        >>> tr = 25
        >>> rh = 50
        >>> v = 0.1
        >>> met = 1.4
        >>> clo = 0.5
        >>> # calculate relative air speed
        >>> v_r = v_relative(v=v, met=met)
        >>> # calculate dynamic clothing
        >>> clo_d = clo_dynamic(clo=clo, met=met)
        >>> results = pmv(tdb=tdb, tr=tr, vr=v_r, rh=rh, met=met, clo=clo_d)
        >>> print(results)
        0.06
        >>> # you can also pass an array-like of inputs
        >>> results = pmv(tdb=[22, 25], tr=tr, vr=v_r, rh=rh, met=met, clo=clo_d)
        >>> print(results)
        array([-0.47,  0.06])
    """
    default_kwargs = {"units": "SI", "limit_inputs": True, "airspeed_control": True}
    kwargs = {**default_kwargs, **kwargs}

    return pmv_ppd(tdb, tr, vr, rh, met, clo, wme, standard, **kwargs)["pmv"]


def a_pmv(tdb, tr, vr, rh, met, clo, a_coefficient, wme=0, **kwargs):
    """Returns Adaptive Predicted Mean Vote (aPMV) [25]_. This index was
    developed by Yao, R. et al. (2009). The model takes into account factors
    such as culture, climate, social, psychological and behavioural
    adaptations, which have an impact on the senses used to detect thermal
    comfort. This model uses an adaptive coefficient (λ) representing the
    adaptive factors that affect the sense of thermal comfort.

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float or array-like
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    clo : float or array-like
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently, the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    a_coefficient : float
        adaptive coefficient
    wme : float or array-like
        external work, [met] default 0

    Other Parameters
    ----------------
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

        The ISO 7730 2005 limits are 10 < tdb [°C] < 30, 10 < tr [°C] < 40,
        0 < vr [m/s] < 1, 0.8 < met [met] < 4, 0 < clo [clo] < 2, and -2 < PMV < 2.

    Returns
    -------
    pmv : float or array-like
        Predicted Mean Vote

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import a_pmv
        >>> from pythermalcomfort.utilities import v_relative, clo_dynamic
        >>> tdb = 28
        >>> tr = 28
        >>> rh = 50
        >>> v = 0.1
        >>> met = 1.4
        >>> clo = 0.5
        >>> # calculate relative air speed
        >>> v_r = v_relative(v=v, met=met)
        >>> # calculate dynamic clothing
        >>> clo_d = clo_dynamic(clo=clo, met=met)
        >>> results = a_pmv(tdb, tr, v_r, rh, met, clo_d, a_coefficient=0.293)
        >>> print(results)
        0.74
    """
    default_kwargs = {"units": "SI", "limit_inputs": True}
    kwargs = {**default_kwargs, **kwargs}

    _pmv = pmv(tdb, tr, vr, rh, met, clo, wme, "ISO", **kwargs)

    return np.around(_pmv / (1 + a_coefficient * _pmv), 2)


def e_pmv(tdb, tr, vr, rh, met, clo, e_coefficient, wme=0, **kwargs):
    """Returns Adjusted Predicted Mean Votes with Expectancy Factor (ePMV).
    This index was developed by Fanger, P. O. et al. (2002). In non-air-
    conditioned buildings in warm climates, occupants may sense the warmth as
    being less severe than the PMV predicts. The main reason is low
    expectations, but a metabolic rate that is estimated too high can also
    contribute to explaining the difference. An extension of the PMV model that
    includes an expectancy factor is introduced for use in non-air-conditioned
    buildings in warm climates [26]_.

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float or array-like
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    clo : float or array-like
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently, the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    e_coefficient : float
        expectacy factor
    wme : float or array-like
        external work, [met] default 0

    Other Parameters
    ----------------
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

        The ISO 7730 2005 limits are 10 < tdb [°C] < 30, 10 < tr [°C] < 40,
        0 < vr [m/s] < 1, 0.8 < met [met] < 4, 0 < clo [clo] < 2, and -2 < PMV < 2.

    Returns
    -------
    pmv : float or array-like
        Predicted Mean Vote

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import a_pmv
        >>> from pythermalcomfort.utilities import v_relative, clo_dynamic
        >>> tdb = 28
        >>> tr = 28
        >>> rh = 50
        >>> v = 0.1
        >>> met = 1.4
        >>> clo = 0.5
        >>> # calculate relative air speed
        >>> v_r = v_relative(v=v, met=met)
        >>> # calculate dynamic clothing
        >>> clo_d = clo_dynamic(clo=clo, met=met)
        >>> results = e_pmv(tdb, tr, v_r, rh, met, clo_d, e_coefficient=0.6)
        >>> print(results)
        0.51
    """
    default_kwargs = {"units": "SI", "limit_inputs": True}
    kwargs = {**default_kwargs, **kwargs}

    met = np.array(met)
    _pmv = pmv(tdb, tr, vr, rh, met, clo, wme, "ISO", **kwargs)
    met = np.where(_pmv > 0, met * (1 + _pmv * (-0.067)), met)
    _pmv = pmv(tdb, tr, vr, rh, met, clo, wme, "ISO", **kwargs)

    return np.around(_pmv * e_coefficient, 2)


def set_tmp(
    tdb,
    tr,
    v,
    rh,
    met,
    clo,
    wme=0,
    body_surface_area=1.8258,
    p_atm=101325,
    body_position="standing",
    units="SI",
    limit_inputs=True,
    **kwargs,
):
    """
    Calculates the Standard Effective Temperature (SET). The SET is the temperature of
    a hypothetical isothermal environment at 50% (rh), <0.1 m/s (20 fpm) average air
    speed (v), and tr = tdb, in which the total heat loss from the skin of an imaginary occupant
    wearing clothing, standardized for the activity concerned is the same as that
    from a person in the actual environment with actual clothing and activity level. [10]_

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    v : float or array-like
        air speed, default in [m/s] in [fps] if `units` = 'IP'
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    clo : float or array-like
        clothing insulation, [clo]
    wme : float or array-like
        external work, [met] default 0
    body_surface_area : float
        body surface area, default value 1.8258 [m2] in [ft2] if `units` = 'IP'

        The body surface area can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.body_surface_area`.
    p_atm : float
        atmospheric pressure, default value 101325 [Pa] in [atm] if `units` = 'IP'
    body_position: str default="standing" or array-like
        select either "sitting" or "standing"
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the following limits the
        function returns nan. If False returns values regardless of the input values.
        The limits are 10 < tdb [°C] < 40, 10 < tr [°C] < 40,
        0 < v [m/s] < 2, 1 < met [met] < 4, and 0 < clo [clo] < 1.5.

    Other Parameters
    ----------------
    round : boolean, deafult True
        if True rounds output value, if False it does not round it

    Returns
    -------
    SET : float or array-like
        Standard effective temperature, [°C]

    Notes
    -----
    You can use this function to calculate the `SET`_ temperature in accordance with
    the ASHRAE 55 2020 Standard [1]_.

    .. _SET: https://en.wikipedia.org/wiki/Thermal_comfort#Standard_effective_temperature

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import set_tmp
        >>> set_tmp(tdb=25, tr=25, v=0.1, rh=50, met=1.2, clo=.5)
        24.3
        >>> set_tmp(tdb=[25, 25], tr=25, v=0.1, rh=50, met=1.2, clo=.5)
        array([24.3, 24.3])

        >>> # for users who wants to use the IP system
        >>> set_tmp(tdb=77, tr=77, v=0.328, rh=50, met=1.2, clo=.5, units='IP')
        75.8

    """
    # When SET is used to calculate CE then h_c is calculated in a slightly different way
    default_kwargs = {"round": True, "calculate_ce": False}
    kwargs = {**default_kwargs, **kwargs}

    if units.lower() == "ip":
        if body_surface_area == 1.8258:
            body_surface_area = 19.65
        if p_atm == 101325:
            p_atm = 1
        tdb, tr, v, body_surface_area, p_atm = units_converter(
            tdb=tdb, tr=tr, v=v, area=body_surface_area, pressure=p_atm
        )

    tdb = np.array(tdb)
    tr = np.array(tr)
    v = np.array(v)
    rh = np.array(rh)
    met = np.array(met)
    clo = np.array(clo)
    wme = np.array(wme)

    set_array = two_nodes(
        tdb=tdb,
        tr=tr,
        v=v,
        rh=rh,
        met=met,
        clo=clo,
        wme=wme,
        body_surface_area=body_surface_area,
        p_atmospheric=p_atm,
        body_position=body_position,
        calculate_ce=kwargs["calculate_ce"],
        round=False,
        output="all",
    )["_set"]

    if units.lower() == "ip":
        set_array = units_converter(tmp=set_array, from_units="si")[0]

    if limit_inputs:
        (
            tdb_valid,
            tr_valid,
            v_valid,
            met_valid,
            clo_valid,
        ) = check_standard_compliance_array(
            "ashrae", tdb=tdb, tr=tr, v=v, met=met, clo=clo
        )
        all_valid = ~(
            np.isnan(tdb_valid)
            | np.isnan(tr_valid)
            | np.isnan(v_valid)
            | np.isnan(met_valid)
            | np.isnan(clo_valid)
        )
        set_array = np.where(all_valid, set_array, np.nan)

    if kwargs["round"]:
        return np.around(set_array, 1)
    else:
        return set_array


def use_fans_heatwaves(
    tdb,
    tr,
    v,
    rh,
    met,
    clo,
    wme=0,
    body_surface_area=1.8258,
    p_atm=101325,
    body_position="standing",
    units="SI",
    max_skin_blood_flow=80,
    **kwargs,
):
    """It helps you to estimate if the conditions you have selected would cause
    heat strain. This occurs when either the following variables reaches its
    maximum value:

    * m_rsw Rate at which regulatory sweat is generated, [mL/h/m2]
    * w : Skin wettedness, adimensional. Ranges from 0 and 1.
    * m_bl : Skin blood flow [kg/h/m2]

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    v : float
        air speed, default in [m/s] in [fps] if `units` = 'IP'
    rh : float
        relative humidity, [%]
    met : float
        metabolic rate, [met]
    clo : float
        clothing insulation, [clo]
    wme : float
        external work, [met] default 0
    body_surface_area : float
        body surface area, default value 1.8258 [m2] in [ft2] if `units` = 'IP'

        The body surface area can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.body_surface_area`.
    p_atm : float
        atmospheric pressure, default value 101325 [Pa] in [atm] if `units` = 'IP'
    body_position: str default="standing"
        select either "sitting" or "standing"
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    max_skin_blood_flow : float, [kg/h/m2] default 80
        maximum blood flow from the core to the skin

    Other Parameters
    ----------------
    max_sweating: float, [mL/h/m2] default 500
        max sweating
    round: boolean, default True
        if True rounds output value, if False it does not round it
    limit_inputs : boolean default True
        By default, if the inputs are outside the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

        The applicability limits are 20 < tdb [°C] < 50, 20 < tr [°C] < 50,
        0.1 < v [m/s] < 4.5, 0.7 < met [met] < 2, and 0 < clo [clo] < 1.

    Returns
    -------
    e_skin : float
        Total rate of evaporative heat loss from skin, [W/m2]. Equal to e_rsw + e_diff
    e_rsw : float
        Rate of evaporative heat loss from sweat evaporation, [W/m2]
    e_diff : float
        Rate of evaporative heat loss from moisture diffused through the skin, [W/m2]
    e_max : float
        Maximum rate of evaporative heat loss from skin, [W/m2]
    q_sensible : float
        Sensible heat loss from skin, [W/m2]
    q_skin : float
        Total rate of heat loss from skin, [W/m2]. Equal to q_sensible + e_skin
    q_res : float
        Total rate of heat loss through respiration, [W/m2]
    t_core : float
        Core temperature, [°C]
    t_skin : float
        Skin temperature, [°C]
    m_bl : float
        Skin blood flow, [kg/h/m2]
    m_rsw : float
        Rate at which regulatory sweat is generated, [mL/h/m2]
    w : float
        Skin wettedness, adimensional. Ranges from 0 and 1.
    w_max : float
        Skin wettedness (w) practical upper limit, adimensional. Ranges from 0 and 1.
    heat_strain : bool
        True if the model predict that the person may be experiencing heat strain
    heat_strain_blood_flow : bool
        True if heat strain is caused by skin blood flow (m_bl) reaching its maximum value
    heat_strain_w : bool
        True if heat strain is caused by skin wettedness (w) reaching its maximum value
    heat_strain_sweating : bool
        True if heat strain is caused by regulatory sweating (m_rsw) reaching its
        maximum value
    """
    # If the SET function is used to calculate the cooling effect then the h_c is
    # calculated in a slightly different way
    default_kwargs = {"round": True, "max_sweating": 500, "limit_inputs": True}
    kwargs = {**default_kwargs, **kwargs}

    tdb = np.array(tdb)
    tr = np.array(tr)
    v = np.array(v)
    rh = np.array(rh)
    met = np.array(met)
    clo = np.array(clo)
    wme = np.array(wme)

    if units.lower() == "ip":
        if body_surface_area == 1.8258:
            body_surface_area = 19.65
        if p_atm == 101325:
            p_atm = 1
        tdb, tr, v, body_surface_area, p_atm = units_converter(
            tdb=tdb, tr=tr, v=v, area=body_surface_area, pressure=p_atm
        )

    output = two_nodes(
        tdb,
        tr,
        v,
        rh,
        met,
        clo,
        wme=wme,
        body_surface_area=body_surface_area,
        p_atmospheric=p_atm,
        body_position=body_position,
        max_skin_blood_flow=max_skin_blood_flow,
        round=False,
        output="all",
        max_sweating=kwargs["max_sweating"],
    )

    output_vars = [
        "e_skin",
        "e_rsw",
        "e_max",
        "q_sensible",
        "q_skin",
        "q_res",
        "t_core",
        "t_skin",
        "m_bl",
        "m_rsw",
        "w",
        "w_max",
        "heat_strain_blood_flow",
        "heat_strain_w",
        "heat_strain_sweating",
        "heat_strain",
    ]

    output["heat_strain_blood_flow"] = np.where(
        output["m_bl"] == max_skin_blood_flow, True, False
    )
    output["heat_strain_w"] = np.where(output["w"] == output["w_max"], True, False)
    output["heat_strain_sweating"] = np.where(
        output["m_rsw"] == kwargs["max_sweating"], True, False
    )

    output["heat_strain"] = np.any(
        [
            output["heat_strain_blood_flow"],
            output["heat_strain_w"],
            output["heat_strain_sweating"],
        ],
        axis=0,
    )

    output = {key: output[key] for key in output_vars}

    if kwargs["limit_inputs"]:
        (
            tdb_valid,
            tr_valid,
            v_valid,
            rh_valid,
            met_valid,
            clo_valid,
        ) = check_standard_compliance_array(
            standard="fan_heatwaves", tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo
        )
        all_valid = ~(
            np.isnan(tdb_valid)
            | np.isnan(tr_valid)
            | np.isnan(v_valid)
            | np.isnan(met_valid)
            | np.isnan(clo_valid)
        )
        output = {key: np.where(all_valid, output[key], np.nan) for key in output_vars}

    for key in output.keys():
        # round the results if needed
        if (kwargs["round"]) and (type(output[key]) is not bool):
            output[key] = np.around(output[key], 1)

    return output


def adaptive_ashrae(tdb, tr, t_running_mean, v, units="SI", limit_inputs=True):
    """Determines the adaptive thermal comfort based on ASHRAE 55. The adaptive
    model relates indoor design temperatures or acceptable temperature ranges
    to outdoor meteorological or climatological parameters. The adaptive model
    can only be used in occupant-controlled naturally conditioned spaces that
    meet all the following criteria:

    * There is no mechianical cooling or heating system in operation
    * Occupants have a metabolic rate between 1.0 and 1.5 met
    * Occupants are free to adapt their clothing within a range as wide as 0.5 and 1.0 clo
    * The prevailing mean (runnin mean) outdoor temperature is between 10 and 33.5 °C

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    t_running_mean: float or array-like
        running mean temperature, default in [°C] in [°C] in [°F] if `units` = 'IP'

        The running mean temperature can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.running_mean_outdoor_temperature`.
    v : float or array-like
        air speed, default in [m/s] in [fps] if `units` = 'IP'
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

        The ASHRAE 55 2020 limits are 10 < tdb [°C] < 40, 10 < tr [°C] < 40,
        0 < vr [m/s] < 2, 10 < t running mean [°C] < 33.5

    Returns
    -------
    tmp_cmf : float or array-like
        Comfort temperature a that specific running mean temperature, default in [°C]
        or in [°F]
    tmp_cmf_80_low : float or array-like
        Lower acceptable comfort temperature for 80% occupants, default in [°C] or in [°F]
    tmp_cmf_80_up : float or array-like
        Upper acceptable comfort temperature for 80% occupants, default in [°C] or in [°F]
    tmp_cmf_90_low : float or array-like
        Lower acceptable comfort temperature for 90% occupants, default in [°C] or in [°F]
    tmp_cmf_90_up : float or array-like
        Upper acceptable comfort temperature for 90% occupants, default in [°C] or in [°F]
    acceptability_80 : bol or array-like
        Acceptability for 80% occupants
    acceptability_90 : bol or array-like
        Acceptability for 90% occupants

    Notes
    -----
    You can use this function to calculate if your conditions are within the `adaptive
    thermal comfort region`.
    Calculations with comply with the ASHRAE 55 2020 Standard [1]_.

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import adaptive_ashrae
        >>> results = adaptive_ashrae(tdb=25, tr=25, t_running_mean=20, v=0.1)
        >>> print(results)
        {'tmp_cmf': 24.0, 'tmp_cmf_80_low': 20.5, 'tmp_cmf_80_up': 27.5,
        'tmp_cmf_90_low': 21.5, 'tmp_cmf_90_up': 26.5, 'acceptability_80': array(True),
        'acceptability_90': array(True)}

        >>> print(results['acceptability_80'])
        True
        # The conditions you entered are considered to be comfortable for by 80% of the
        occupants

        >>> # for users who want to use the IP system
        >>> results = adaptive_ashrae(tdb=77, tr=77, t_running_mean=68, v=0.3, units='ip')
        >>> print(results)
        {'tmp_cmf': 75.2, 'tmp_cmf_80_low': 68.9, 'tmp_cmf_80_up': 81.5,
        'tmp_cmf_90_low': 70.7, 'tmp_cmf_90_up': 79.7, 'acceptability_80': array(True),
        'acceptability_90': array(True)}

        >>> adaptive_ashrae(tdb=25, tr=25, t_running_mean=9, v=0.1)
        {'tmp_cmf': nan, 'tmp_cmf_80_low': nan, ... }
        # The adaptive thermal comfort model can only be used
        # if the running mean temperature is higher than 10°C
    """

    tdb = np.array(tdb)
    tr = np.array(tr)
    t_running_mean = np.array(t_running_mean)
    v = np.array(v)
    standard = "ashrae"

    if units.lower() == "ip":
        tdb, tr, t_running_mean, v = units_converter(
            tdb=tdb, tr=tr, tmp_running_mean=t_running_mean, v=v
        )

    (
        tdb_valid,
        tr_valid,
        v_valid,
    ) = check_standard_compliance_array(standard, tdb=tdb, tr=tr, v=v)
    trm_valid = valid_range(t_running_mean, (10.0, 33.5))

    to = t_o(tdb, tr, v, standard=standard)

    # calculate cooling effect (ce) of elevated air speed when top > 25 degC.
    ce = np.where((v >= 0.6) & (to >= 25.0), 999, 0)
    ce = np.where((v < 0.9) & (ce == 999), 1.2, ce)
    ce = np.where((v < 1.2) & (ce == 999), 1.8, ce)
    ce = np.where(ce == 999, 2.2, ce)

    # Relation between comfort and outdoor temperature
    t_cmf = 0.31 * t_running_mean + 17.8

    if limit_inputs:
        all_valid = ~(
            np.isnan(tdb_valid)
            | np.isnan(tr_valid)
            | np.isnan(v_valid)
            | np.isnan(trm_valid)
        )
        t_cmf = np.where(all_valid, t_cmf, np.nan)

    t_cmf = np.around(t_cmf, 1)

    tmp_cmf_80_low = t_cmf - 3.5
    tmp_cmf_90_low = t_cmf - 2.5
    tmp_cmf_80_up = t_cmf + 3.5 + ce
    tmp_cmf_90_up = t_cmf + 2.5 + ce

    acceptability_80 = np.where(
        (tmp_cmf_80_low <= to) & (to <= tmp_cmf_80_up), True, False
    )
    acceptability_90 = np.where(
        (tmp_cmf_90_low <= to) & (to <= tmp_cmf_90_up), True, False
    )

    if units.lower() == "ip":
        (
            t_cmf,
            tmp_cmf_80_low,
            tmp_cmf_80_up,
            tmp_cmf_90_low,
            tmp_cmf_90_up,
        ) = units_converter(
            from_units="si",
            tmp_cmf=t_cmf,
            tmp_cmf_80_low=tmp_cmf_80_low,
            tmp_cmf_80_up=tmp_cmf_80_up,
            tmp_cmf_90_low=tmp_cmf_90_low,
            tmp_cmf_90_up=tmp_cmf_90_up,
        )

    return {
        "tmp_cmf": t_cmf,
        "tmp_cmf_80_low": tmp_cmf_80_low,
        "tmp_cmf_80_up": tmp_cmf_80_up,
        "tmp_cmf_90_low": tmp_cmf_90_low,
        "tmp_cmf_90_up": tmp_cmf_90_up,
        "acceptability_80": acceptability_80,
        "acceptability_90": acceptability_90,
    }


def adaptive_en(tdb, tr, t_running_mean, v, units="SI", limit_inputs=True):
    """Determines the adaptive thermal comfort based on EN 16798-1 2019 [3]_

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    t_running_mean: float or array-like
        running mean temperature, default in [°C] in [°C] in [°F] if `units` = 'IP'

        The running mean temperature can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.running_mean_outdoor_temperature`.
    v : float or array-like
        air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: Indoor operative temperature correction is applicable for buildings equipped
        with fans or personal systems providing building occupants with personal
        control over air speed at occupant level.
        For operative temperatures above 25°C the comfort zone upper limit can be
        increased by 1.2 °C (0.6 < v < 0.9 m/s), 1.8 °C (0.9 < v < 1.2 m/s), 2.2 °C ( v
        > 1.2 m/s)
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns pmv and ppd values even if input values are
        outside the applicability limits of the model.

    Returns
    -------
    tmp_cmf : float or array-like
        Comfort temperature at that specific running mean temperature, default in [°C]
        or in [°F]
    acceptability_cat_i : bol or array-like
        If the indoor conditions comply with comfort category I
    acceptability_cat_ii : bol or array-like
        If the indoor conditions comply with comfort category II
    acceptability_cat_iii : bol or array-like
        If the indoor conditions comply with comfort category III
    tmp_cmf_cat_i_up : float or array-like
        Upper acceptable comfort temperature for category I, default in [°C] or in [°F]
    tmp_cmf_cat_ii_up : float or array-like
        Upper acceptable comfort temperature for category II, default in [°C] or in [°F]
    tmp_cmf_cat_iii_up : float or array-like
        Upper acceptable comfort temperature for category III, default in [°C] or in [°F]
    tmp_cmf_cat_i_low : float or array-like
        Lower acceptable comfort temperature for category I, default in [°C] or in [°F]
    tmp_cmf_cat_ii_low : float or array-like
        Lower acceptable comfort temperature for category II, default in [°C] or in [°F]
    tmp_cmf_cat_iii_low : float or array-like
        Lower acceptable comfort temperature for category III, default in [°C] or in [°F]

    Notes
    -----
    You can use this function to calculate if your conditions are within the EN
    adaptive thermal comfort region.
    Calculations with comply with the EN 16798-1 2019 [3]_.

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import adaptive_en
        >>> results = adaptive_en(tdb=25, tr=25, t_running_mean=20, v=0.1)
        >>> print(results)
        {'tmp_cmf': 25.4, 'acceptability_cat_i': True, 'acceptability_cat_ii': True, ... }

        >>> print(results['acceptability_cat_i'])
        True
        # The conditions you entered are considered to comply with Category I

        >>> # for users who wants to use the IP system
        >>> results = adaptive_en(tdb=77, tr=77, t_running_mean=68, v=0.3, units='ip')
        >>> print(results)
        {'tmp_cmf': 77.7, 'acceptability_cat_i': True, 'acceptability_cat_ii': True, ... }

        >>> results = adaptive_en(tdb=25, tr=25, t_running_mean=9, v=0.1)
        {'tmp_cmf': nan, 'acceptability_cat_i': True, 'acceptability_cat_ii': True, ... }
        # The adaptive thermal comfort model can only be used
        # if the running mean temperature is between 10 °C and 30 °C
    """

    tdb = np.array(tdb)
    tr = np.array(tr)
    t_running_mean = np.array(t_running_mean)
    v = np.array(v)
    standard = "iso"

    if units.lower() == "ip":
        tdb, tr, t_running_mean, vr = units_converter(
            tdb=tdb, tr=tr, tmp_running_mean=t_running_mean, v=v
        )

    trm_valid = valid_range(t_running_mean, (10.0, 33.5))

    to = t_o(tdb, tr, v, standard=standard)

    # calculate cooling effect (ce) of elevated air speed when top > 25 degC.
    ce = np.where((v >= 0.6) & (to >= 25.0), 999, 0)
    ce = np.where((v < 0.9) & (ce == 999), 1.2, ce)
    ce = np.where((v < 1.2) & (ce == 999), 1.8, ce)
    ce = np.where(ce == 999, 2.2, ce)

    t_cmf = 0.33 * t_running_mean + 18.8

    if limit_inputs:
        all_valid = ~(np.isnan(trm_valid))
        t_cmf = np.where(all_valid, t_cmf, np.nan)

    t_cmf_i_lower = t_cmf - 3.0
    t_cmf_ii_lower = t_cmf - 4.0
    t_cmf_iii_lower = t_cmf - 5.0
    t_cmf_i_upper = t_cmf + 2.0 + ce
    t_cmf_ii_upper = t_cmf + 3.0 + ce
    t_cmf_iii_upper = t_cmf + 4.0 + ce

    acceptability_i = np.where(
        (t_cmf_i_lower <= to) & (to <= t_cmf_i_upper), True, False
    )
    acceptability_ii = np.where(
        (t_cmf_ii_lower <= to) & (to <= t_cmf_ii_upper), True, False
    )
    acceptability_iii = np.where(
        (t_cmf_iii_lower <= to) & (to <= t_cmf_iii_upper), True, False
    )

    if units.lower() == "ip":
        t_cmf, t_cmf_i_upper, t_cmf_ii_upper, t_cmf_iii_upper = units_converter(
            from_units="si",
            tmp_cmf=t_cmf,
            tmp_cmf_cat_i_up=t_cmf_i_upper,
            tmp_cmf_cat_ii_up=t_cmf_ii_upper,
            tmp_cmf_cat_iii_up=t_cmf_iii_upper,
        )
        t_cmf_i_lower, t_cmf_ii_lower, t_cmf_iii_lower = units_converter(
            from_units="si",
            tmp_cmf_cat_i_low=t_cmf_i_lower,
            tmp_cmf_cat_ii_low=t_cmf_ii_lower,
            tmp_cmf_cat_iii_low=t_cmf_iii_lower,
        )

    results = {
        "tmp_cmf": np.around(t_cmf, 1),
        "acceptability_cat_i": acceptability_i,
        "acceptability_cat_ii": acceptability_ii,
        "acceptability_cat_iii": acceptability_iii,
        "tmp_cmf_cat_i_up": np.around(t_cmf_i_upper, 1),
        "tmp_cmf_cat_ii_up": np.around(t_cmf_ii_upper, 1),
        "tmp_cmf_cat_iii_up": np.around(t_cmf_iii_upper, 1),
        "tmp_cmf_cat_i_low": np.around(t_cmf_i_lower, 1),
        "tmp_cmf_cat_ii_low": np.around(t_cmf_ii_lower, 1),
        "tmp_cmf_cat_iii_low": np.around(t_cmf_iii_lower, 1),
    }

    return results


def utci(tdb, tr, v, rh, units="SI", return_stress_category=False, limit_inputs=True):
    """Determines the Universal Thermal Climate Index (UTCI). The UTCI is the
    equivalent temperature for the environment derived from a reference
    environment. It is defined as the air temperature of the reference
    environment which produces the same strain index value in comparison with
    the reference individual's response to the real environment. It is regarded
    as one of the most comprehensive indices for calculating heat stress in
    outdoor spaces. The parameters that are taken into account for calculating
    UTCI involve dry bulb temperature, mean radiation temperature, the pressure
    of water vapor or relative humidity, and wind speed (at the elevation of 10
    m above the ground). [7]_

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    v : float or array-like
        wind speed 10m above ground level, default in [m/s] in [fps] if `units` = 'IP'
    rh : float or array-like
        relative humidity, [%]
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.
    return_stress_category : boolean default False
        if True returns the UTCI categorized in terms of thermal stress.
    limit_inputs : boolean default True
        By default, if the inputs are outsude the standard applicability limits the
        function returns nan. If False returns UTCI values even if input values are
        outside the applicability limits of the model. The valid input ranges are
        -50 < tdb [°C] < 50, tdb - 70 < tr [°C] < tdb + 30, and for 0.5 < v [m/s] < 17.0.

    Returns
    -------
    utci : float or array-like
         Universal Thermal Climate Index, [°C] or in [°F]
    stress_category : str or array-like
         UTCI categorized in terms of thermal stress [9]_.

    Notes
    -----
    You can use this function to calculate the Universal Thermal Climate Index (`UTCI`)
    The applicability wind speed value must be between 0.5 and 17 m/s.

    .. _UTCI: http://www.utci.org/utcineu/utcineu.php

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import utci
        >>> utci(tdb=25, tr=25, v=1.0, rh=50)
        24.6

        >>> # for users who wants to use the IP system
        >>> utci(tdb=77, tr=77, v=3.28, rh=50, units='ip')
        76.4

        >>> # for users who wants to get stress category
        >>> utci(tdb=25, tr=25, v=1.0, rh=50, return_stress_category=True)
        {"utci": 24.6, "stress_category": "no thermal stress"}

    Raises
    ------
    ValueError
        Raised if the input are outside the Standard's applicability limits
    """

    tdb = np.array(tdb)
    tr = np.array(tr)
    v = np.array(v)
    rh = np.array(rh)

    if units.lower() == "ip":
        tdb, tr, v = units_converter(tdb=tdb, tr=tr, v=v)

    def exponential(t_db):
        g = [
            -2836.5744,
            -6028.076559,
            19.54263612,
            -0.02737830188,
            0.000016261698,
            (7.0229056 * np.power(10.0, -10)),
            (-1.8680009 * np.power(10.0, -13)),
        ]
        tk = t_db + 273.15  # air temp in K
        es = 2.7150305 * np.log1p(tk)
        for count, i in enumerate(g):
            es = es + (i * np.power(tk, count - 2))
        es = np.exp(es) * 0.01  # convert Pa to hPa
        return es

    eh_pa = exponential(tdb) * (rh / 100.0)
    delta_t_tr = tr - tdb
    pa = eh_pa / 10.0  # convert vapour pressure to kPa

    utci_approx = utci_optimized(tdb, v, delta_t_tr, pa)

    # Checks that inputs are within the bounds accepted by the model if not return nan
    if limit_inputs:
        tdb_valid = valid_range(tdb, (-50.0, 50.0))
        diff_valid = valid_range(tr - tdb, (-30.0, 70.0))
        v_valid = valid_range(v, (0.5, 17.0))
        all_valid = ~(np.isnan(tdb_valid) | np.isnan(diff_valid) | np.isnan(v_valid))
        utci_approx = np.where(all_valid, utci_approx, np.nan)

    if units.lower() == "ip":
        utci_approx = units_converter(tmp=utci_approx, from_units="si")[0]

    if return_stress_category:
        stress_categories = {
            -40.0: "extreme cold stress",
            -27.0: "very strong cold stress",
            -13.0: "strong cold stress",
            0.0: "moderate cold stress",
            9.0: "slight cold stress",
            26.0: "no thermal stress",
            32.0: "moderate heat stress",
            38.0: "strong heat stress",
            46.0: "very strong heat stress",
            1000.0: "extreme heat stress",
        }

        return {
            "utci": np.round_(utci_approx, 1),
            "stress_category": mapping(utci_approx, stress_categories),
        }
    else:
        return np.round_(utci_approx, 1)


def clo_tout(tout, units="SI"):
    """Representative clothing insulation Icl as a function of outdoor air
    temperature at 06:00 a.m [4]_.

    Parameters
    ----------
    tout : float or array-like
        outdoor air temperature at 06:00 a.m., default in [°C] in [°F] if `units` = 'IP'
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.

    Returns
    -------
    clo : float or array-like
         Representative clothing insulation Icl, [clo]

    Notes
    -----
    The ASHRAE 55 2020 states that it is acceptable to determine the clothing
    insulation Icl using this equation in mechanically conditioned buildings [1]_.

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import clo_tout
        >>> clo_tout(tout=27)
        0.46
        >>> clo_tout(tout=[27, 25])
        array([0.46, 0.47])
    """

    tout = np.array(tout)

    if units.lower() == "ip":
        tout = units_converter(tmp=tout)[0]

    clo = np.where(tout < 26, np.power(10, -0.1635 - 0.0066 * tout), 0.46)
    clo = np.where(tout < 5, 0.818 - 0.0364 * tout, clo)
    clo = np.where(tout < -5, 1, clo)

    return np.around(clo, 2)


def vertical_tmp_grad_ppd(tdb, tr, vr, rh, met, clo, vertical_tmp_grad, units="SI"):
    """Calculates the percentage of thermally dissatisfied people with a
    vertical temperature gradient between feet and head [1]_. This equation is
    only applicable for vr < 0.2 m/s (40 fps).

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'

        Note: The air temperature is the average value over two heights: 0.6 m (24 in.)
        and 1.1 m (43 in.) for seated occupants
        and 1.1 m (43 in.) and 1.7 m (67 in.) for standing occupants.
    tr : float
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float
        relative humidity, [%]
    met : float
        metabolic rate, [met]
    clo : float
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    vertical_tmp_grad : float
        vertical temperature gradient between the feet and the head, default in [°C/m]
        in [°F/ft] if `units` = 'IP'
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.

    Returns
    -------
    PPD_vg: float
        Predicted Percentage of Dissatisfied occupants with vertical temperature
        gradient, [%]
    Acceptability: bol
        The ASHRAE 55 2020 standard defines that the value of air speed at the ankle
        level is acceptable if PPD_ad is lower or equal than 5 %

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import vertical_tmp_grad_ppd
        >>> results = vertical_tmp_grad_ppd(25, 25, 0.1, 50, 1.2, 0.5, 7)
        >>> print(results)
        {'PPD_vg': 12.6, 'Acceptability': False}
    """
    if units.lower() == "ip":
        tdb, tr, vr = units_converter(tdb=tdb, tr=tr, v=vr)
        vertical_tmp_grad = vertical_tmp_grad / 1.8 * 3.28

    check_standard_compliance(
        standard="ashrae", tdb=tdb, tr=tr, v_limited=vr, rh=rh, met=met, clo=clo
    )

    tsv = pmv(tdb, tr, vr, rh, met, clo, standard="ashrae")
    numerator = math.exp(0.13 * (tsv - 1.91) ** 2 + 0.15 * vertical_tmp_grad - 1.6)
    ppd_val = round((numerator / (1 + numerator) - 0.345) * 100, 1)
    acceptability = ppd_val <= 5
    return {"PPD_vg": ppd_val, "Acceptability": acceptability}


def ankle_draft(tdb, tr, vr, rh, met, clo, v_ankle, units="SI"):
    """
    Calculates the percentage of thermally dissatisfied people with the ankle draft (
    0.1 m) above floor level [23]_.
    This equation is only applicable for vr < 0.2 m/s (40 fps).

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'

        Note: The air temperature is the average value over two heights: 0.6 m (24 in.)
        and 1.1 m (43 in.) for seated occupants
        and 1.1 m (43 in.) and 1.7 m (67 in.) for standing occupants.
    tr : float
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    vr : float
        relative air speed, default in [m/s] in [fps] if `units` = 'IP'

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float
        relative humidity, [%]
    met : float
        metabolic rate, [met]
    clo : float
        clothing insulation, [clo]

        Note: The activity as well as the air speed modify the insulation characteristics
        of the clothing and the adjacent air layer. Consequently, the ISO 7730 states that
        the clothing insulation shall be corrected [2]_. The ASHRAE 55 Standard corrects
        for the effect of the body movement for met equal or higher than 1.2 met using
        the equation clo = Icl × (0.6 + 0.4/met) The dynamic clothing insulation, clo,
        can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.clo_dynamic`.
    v_ankle : float
        air speed at the 0.1 m (4 in.) above the floor, default in [m/s] in [fps] if
        `units` = 'IP'
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.

    Returns
    -------
    PPD_ad: float
        Predicted Percentage of Dissatisfied occupants with ankle draft, [%]
    Acceptability: bol
        The ASHRAE 55 2020 standard defines that the value of air speed at the ankle
        level is acceptable if PPD_ad is lower or equal than 20 %

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import ankle_draft
        >>> results = ankle_draft(25, 25, 0.2, 50, 1.2, 0.5, 0.3, units="SI")
        >>> print(results)
        {'PPD_ad': 18.5, 'Acceptability': True}

    """
    if units.lower() == "ip":
        tdb, tr, vr, v_ankle = units_converter(tdb=tdb, tr=tr, v=vr, vel=v_ankle)

    check_standard_compliance(
        standard="ashrae", tdb=tdb, tr=tr, v_limited=vr, rh=rh, met=met, clo=clo
    )

    tsv = pmv(tdb, tr, vr, rh, met, clo, standard="ashrae")
    ppd_val = round(
        math.exp(-2.58 + 3.05 * v_ankle - 1.06 * tsv)
        / (1 + math.exp(-2.58 + 3.05 * v_ankle - 1.06 * tsv))
        * 100,
        1,
    )
    acceptability = ppd_val <= 20
    return {"PPD_ad": ppd_val, "Acceptability": acceptability}


def solar_gain(
    sol_altitude,
    sharp,
    sol_radiation_dir,
    sol_transmittance,
    f_svv,
    f_bes,
    asw=0.7,
    posture="seated",
    floor_reflectance=0.6,
):
    """Calculates the solar gain to the human body using the Effective Radiant
    Field ( ERF) [1]_. The ERF is a measure of the net energy flux to or from
    the human body. ERF is expressed in W over human body surface area [w/m2].
    In addition, it calculates the delta mean radiant temperature. Which is the
    amount by which the mean radiant temperature of the space should be
    increased if no solar radiation is present.

    Parameters
    ----------
    sol_altitude : float
        Solar altitude, degrees from horizontal [deg]. Ranges between 0 and 90.
    sharp : float
        Solar horizontal angle relative to the front of the person (SHARP) [deg].
        Ranges between 0 and 180 and is symmetrical on either side. Zero (0) degrees
        represents direct-beam radiation from the front, 90 degrees represents
        direct-beam radiation from the side, and 180 degrees rep- resent direct-beam
        radiation from the back. SHARP is the angle between the sun and the person
        only. Orientation relative to compass or to room is not included in SHARP.
    posture : str
        Default 'seated' list of available options 'standing', 'supine' or 'seated'
    sol_radiation_dir : float
        Direct-beam solar radiation, [W/m2]. Ranges between 200 and 1000. See Table
        C2-3 of ASHRAE 55 2020 [1]_.
    sol_transmittance : float
        Total solar transmittance, ranges from 0 to 1. The total solar
        transmittance of window systems, including glazing unit, blinds, and other
        façade treatments, shall be determined using one of the following methods:
        i) Provided by manufacturer or from the National Fenestration Rating
        Council approved Lawrence Berkeley National Lab International Glazing
        Database.
        ii) Glazing unit plus venetian blinds or other complex or unique shades
        shall be calculated using National Fenestration Rating Council approved
        software or Lawrence Berkeley National Lab Complex Glazing Database.
    f_svv : float
        Fraction of sky-vault view fraction exposed to body, ranges from 0 to 1.
        It can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.f_svv`.
    f_bes : float
        Fraction of the possible body surface exposed to sun, ranges from 0 to 1.
        See Table C2-2 and equation C-7 ASHRAE 55 2020 [1]_.
    asw: float
        The average short-wave absorptivity of the occupant. It will range widely,
        depending on the color of the occupant’s skin as well as the color and
        amount of clothing covering the body.
        A value of 0.7 shall be used unless more specific information about the
        clothing or skin color of the occupants is available.
        Note: Short-wave absorptivity typically ranges from 0.57 to 0.84, depending
        on skin and clothing color. More information is available in Blum (1945).
    floor_reflectance: float
        Floor refectance. It is assumed to be constant and equal to 0.6.

    Notes
    -----
    More information on the calculation procedure can be found in Appendix C of [1]_.

    Returns
    -------
    erf: float
        Solar gain to the human body using the Effective Radiant Field [W/m2]
    delta_mrt: float
        Delta mean radiant temperature. The amount by which the mean radiant
        temperature of the space should be increased if no solar radiation is present.

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import solar_gain
        >>> results = solar_gain(sol_altitude=0, sharp=120,
        sol_radiation_dir=800, sol_transmittance=0.5, f_svv=0.5, f_bes=0.5,
        asw=0.7, posture='seated')
        >>> print(results)
        {'erf': 42.9, 'delta_mrt': 10.3}
    """

    posture = posture.lower()
    if posture not in ["standing", "supine", "seated"]:
        raise ValueError("Posture has to be either standing, supine or seated")

    def find_span(arr, x):
        for i in range(0, len(arr)):
            if arr[i + 1] >= x >= arr[i]:
                return i
        return -1

    deg_to_rad = 0.0174532925
    hr = 6
    i_diff = 0.2 * sol_radiation_dir

    # fp is the projected area factor
    fp_table = [
        [0.35, 0.35, 0.314, 0.258, 0.206, 0.144, 0.082],
        [0.342, 0.342, 0.31, 0.252, 0.2, 0.14, 0.082],
        [0.33, 0.33, 0.3, 0.244, 0.19, 0.132, 0.082],
        [0.31, 0.31, 0.275, 0.228, 0.175, 0.124, 0.082],
        [0.283, 0.283, 0.251, 0.208, 0.16, 0.114, 0.082],
        [0.252, 0.252, 0.228, 0.188, 0.15, 0.108, 0.082],
        [0.23, 0.23, 0.214, 0.18, 0.148, 0.108, 0.082],
        [0.242, 0.242, 0.222, 0.18, 0.153, 0.112, 0.082],
        [0.274, 0.274, 0.245, 0.203, 0.165, 0.116, 0.082],
        [0.304, 0.304, 0.27, 0.22, 0.174, 0.121, 0.082],
        [0.328, 0.328, 0.29, 0.234, 0.183, 0.125, 0.082],
        [0.344, 0.344, 0.304, 0.244, 0.19, 0.128, 0.082],
        [0.347, 0.347, 0.308, 0.246, 0.191, 0.128, 0.082],
    ]
    if posture == "seated":
        fp_table = [
            [0.29, 0.324, 0.305, 0.303, 0.262, 0.224, 0.177],
            [0.292, 0.328, 0.294, 0.288, 0.268, 0.227, 0.177],
            [0.288, 0.332, 0.298, 0.29, 0.264, 0.222, 0.177],
            [0.274, 0.326, 0.294, 0.289, 0.252, 0.214, 0.177],
            [0.254, 0.308, 0.28, 0.276, 0.241, 0.202, 0.177],
            [0.23, 0.282, 0.262, 0.26, 0.233, 0.193, 0.177],
            [0.216, 0.26, 0.248, 0.244, 0.22, 0.186, 0.177],
            [0.234, 0.258, 0.236, 0.227, 0.208, 0.18, 0.177],
            [0.262, 0.26, 0.224, 0.208, 0.196, 0.176, 0.177],
            [0.28, 0.26, 0.21, 0.192, 0.184, 0.17, 0.177],
            [0.298, 0.256, 0.194, 0.174, 0.168, 0.168, 0.177],
            [0.306, 0.25, 0.18, 0.156, 0.156, 0.166, 0.177],
            [0.3, 0.24, 0.168, 0.152, 0.152, 0.164, 0.177],
        ]

    if posture == "supine":
        sharp, sol_altitude = transpose_sharp_altitude(sharp, sol_altitude)

    alt_range = [0, 15, 30, 45, 60, 75, 90]
    az_range = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
    alt_i = find_span(alt_range, sol_altitude)
    az_i = find_span(az_range, sharp)
    fp11 = fp_table[az_i][alt_i]
    fp12 = fp_table[az_i][alt_i + 1]
    fp21 = fp_table[az_i + 1][alt_i]
    fp22 = fp_table[az_i + 1][alt_i + 1]
    az1 = az_range[az_i]
    az2 = az_range[az_i + 1]
    alt1 = alt_range[alt_i]
    alt2 = alt_range[alt_i + 1]
    fp = fp11 * (az2 - sharp) * (alt2 - sol_altitude)
    fp += fp21 * (sharp - az1) * (alt2 - sol_altitude)
    fp += fp12 * (az2 - sharp) * (sol_altitude - alt1)
    fp += fp22 * (sharp - az1) * (sol_altitude - alt1)
    fp /= (az2 - az1) * (alt2 - alt1)

    f_eff = 0.725  # fraction of the body surface exposed to environmental radiation
    if posture == "seated":
        f_eff = 0.696

    sw_abs = asw
    lw_abs = 0.95

    e_diff = f_eff * f_svv * 0.5 * sol_transmittance * i_diff
    e_direct = f_eff * fp * sol_transmittance * f_bes * sol_radiation_dir
    e_reflected = (
        f_eff
        * f_svv
        * 0.5
        * sol_transmittance
        * (sol_radiation_dir * math.sin(sol_altitude * deg_to_rad) + i_diff)
        * floor_reflectance
    )

    e_solar = e_diff + e_direct + e_reflected
    erf = e_solar * (sw_abs / lw_abs)
    d_mrt = erf / (hr * f_eff)

    return {"erf": round(erf, 1), "delta_mrt": round(d_mrt, 1)}


def phs(tdb, tr, v, rh, met, clo, posture, wme=0, **kwargs):
    """Calculates the Predicted Heat Strain (PHS) index based in compliace with
    the ISO 7933:2004 Standard [8]_. The ISO 7933 provides a method for the
    analytical evaluation and interpretation of the thermal stress experienced
    by a subject in a hot environment. It describes a method for predicting the
    sweat rate and the internal core temperature that the human body will
    develop in response to the working conditions.

    The PHS model can be used to predict the: heat by respiratory convection, heat flow
    by respiratory evaporation, steady state mean skin temperature, instantaneous value
    of skin temperature, heat accumulation associated with the metabolic rate, maximum
    evaporative heat flow at the skin surface, predicted sweat rate, predicted evaporative
    heat flow, and rectal temperature.

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, default in [°C]
    tr : float
        mean radiant temperature, default in [°C]
    v : float
        air speed, default in [m/s]
    rh : float
        relative humidity, [%]
    met : float
        metabolic rate, [W/(m2)]
    clo : float
        clothing insulation, [clo]
    posture:
        a numeric value presenting posture of person [sitting=1, standing=2, crouching=3]
    wme : float
        external work, [W/(m2)] default 0

    Other Parameters
    ----------------
    i_mst : float, default 0.38
        static moisture permeability index, [dimensionless]
    a_p : float, default 0.54
        fraction of the body surface covered by the reflective clothing, [dimensionless]
    drink : float, default 1
        1 if workers can drink freely, 0 otherwise
    weight : float, default 75
        body weight, [kg]
    height : float, default 1.8
        height, [m]
    walk_sp : float, default 0
        walking speed, [m/s]
    theta : float, default 0
        angle between walking direction and wind direction [degrees]
    acclimatized : float, default 100
        100 if acclimatized subject, 0 otherwise
    duration : float, default 480
        duration of the work sequence, [minutes]
    f_r : float, default 0.97
        emissivity of the reflective clothing, [dimensionless]
        Some reference values :py:meth:`pythermalcomfort.utilities.f_r_garments`.
    t_sk : float, default 34.1
        mean skin temperature when worker starts working, [°C]
    t_cr : float, default 36.8
        mean core temperature when worker starts working, [°C]
    t_re : float, default False
        mean rectal temperature when worker starts working, [°C]
    t_cr_eq : float, default False
        mean core temperature as a function of met when worker starts working, [°C]
    sweat_rate : float, default 0

    Returns
    -------
    t_re : float
        rectal temperature, [°C]
    t_sk : float
        skin temperature, [°C]
    t_cr : float
        core temperature, [°C]
    t_cr_eq : float
        core temperature as a function of the metabolic rate, [°C]
    t_sk_t_cr_wg : float
        fraction of the body mass at the skin temperature
    d_lim_loss_50 : float
        maximum allowable exposure time for water loss, mean subject, [minutes]
    d_lim_loss_95 : float
        maximum allowable exposure time for water loss, 95% of the working population,
        [minutes]
    d_lim_t_re : float
        maximum allowable exposure time for heat storage, [minutes]
    water_loss_watt : float
        maximum water loss in watts, [W]
    water_loss : float
        maximum water loss, [g]

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import phs
        >>> results = phs(tdb=40, tr=40, rh=33.85, v=0.3, met=150, clo=0.5, posture=2)
        >>> print(results)
        {'t_re': 37.5, 'd_lim_loss_50': 440, 'd_lim_loss_95': 298, 'd_lim_t_re': 480,
        'water_loss': 6166.0}
    """
    default_kwargs = {
        "i_mst": 0.38,
        "a_p": 0.54,
        "drink": 1,
        "weight": 75,
        "height": 1.8,
        "walk_sp": 0,
        "theta": 0,
        "acclimatized": 100,
        "duration": 480,
        "f_r": 0.97,
        "t_sk": 34.1,
        "t_cr": 36.8,
        "t_re": False,
        "t_cr_eq": False,
        "t_sk_t_cr_wg": 0.3,
        "sweat_rate": 0,
        "round": True,
    }
    kwargs = {**default_kwargs, **kwargs}

    i_mst = kwargs["i_mst"]
    a_p = kwargs["a_p"]
    drink = kwargs["drink"]
    weight = kwargs["weight"]
    height = kwargs["height"]
    walk_sp = kwargs["walk_sp"]
    theta = kwargs["theta"]
    acclimatized = kwargs["acclimatized"]
    duration = kwargs["duration"]
    f_r = kwargs["f_r"]
    t_sk = kwargs["t_sk"]
    t_cr = kwargs["t_cr"]
    t_re = kwargs["t_re"]
    t_cr_eq = kwargs["t_cr_eq"]
    t_sk_t_cr_wg = kwargs["t_sk_t_cr_wg"]
    sweat_rate = kwargs["sweat_rate"]

    p_a = p_sat(tdb) / 1000 * rh / 100

    check_standard_compliance(
        standard="ISO7933",
        tdb=tdb,
        tr=tr,
        v=v,
        rh=rh,
        met=met * body_surface_area(kwargs["weight"], kwargs["height"]),
        clo=clo,
    )

    if not t_re:
        t_re = t_cr
    if not t_cr_eq:
        t_cr_eq = t_cr

    (
        t_re,
        t_sk,
        t_cr,
        t_cr_eq,
        t_sk_t_cr_wg,
        sweat_rate,
        sw_tot_g,
        d_lim_loss_50,
        d_lim_loss_95,
        d_lim_t_re,
    ) = phs_optimized(
        tdb,
        tr,
        v,
        p_a,
        met,
        clo,
        posture,
        wme,
        i_mst,
        a_p,
        drink,
        weight,
        height,
        walk_sp,
        theta,
        acclimatized,
        duration,
        f_r,
        t_sk,
        t_cr,
        t_re,
        t_cr_eq,
        t_sk_t_cr_wg,
        sweat_rate,
    )

    if kwargs["round"]:
        return {
            "t_re": round(t_re, 1),
            "t_sk": round(t_sk, 1),
            "t_cr": round(t_cr, 1),
            "t_cr_eq": round(t_cr_eq, 1),
            "t_sk_t_cr_wg": round(t_sk_t_cr_wg, 2),
            "d_lim_loss_50": round(d_lim_loss_50, 1),
            "d_lim_loss_95": round(d_lim_loss_95, 1),
            "d_lim_t_re": round(d_lim_t_re, 1),
            "water_loss_watt": round(sweat_rate, 1),
            "water_loss": round(sw_tot_g, 1),
        }
    else:
        return {
            "t_re": t_re,
            "t_sk": t_sk,
            "t_cr": t_cr,
            "t_cr_eq": t_cr_eq,
            "t_sk_t_cr_wg": t_sk_t_cr_wg,
            "d_lim_loss_50": d_lim_loss_50,
            "d_lim_loss_95": d_lim_loss_95,
            "d_lim_t_re": d_lim_t_re,
            "water_loss_watt": sweat_rate,
            "water_loss": sw_tot_g,
        }


def two_nodes(
    tdb,
    tr,
    v,
    rh,
    met,
    clo,
    wme=0,
    body_surface_area=1.8258,
    p_atmospheric=101325,
    body_position="standing",
    max_skin_blood_flow=90,
    **kwargs,
):
    """Two-node model of human temperature regulation Gagge et al. (1986).

    [10]_ This model it can be used to calculate a variety of indices,
    including:

    * Gagge's version of Fanger's Predicted Mean Vote (PMV). This function uses the Fanger's PMV equations but it replaces the heat loss and gain terms with those calculated by the two node model developed by Gagge et al. (1986) [10]_.

    * PMV SET and the predicted thermal sensation based on SET [10]_. This function is similar in all aspects to the :py:meth:`pythermalcomfort.models.pmv_gagge` however, it uses the :py:meth:`pythermalcomfort.models.set` equation to calculate the dry heat loss by convection.

    * Thermal discomfort (DISC) as the relative thermoregulatory strain necessary to restore a state of comfort and thermal equilibrium by sweating [10]_. DISC is described numerically as: comfortable and pleasant (0), slightly uncomfortable but acceptable (1), uncomfortable and unpleasant (2), very uncomfortable (3), limited tolerance (4), and intolerable (S). The range of each category is ± 0.5 numerically. In the cold, the classical negative category descriptions used for Fanger's PMV apply [10]_.

    * Heat gains and losses via convection, radiation and conduction.

    * The Standard Effective Temperature (SET)

    * The New Effective Temperature (ET)

    * The Predicted  Thermal  Sensation  (TSENS)

    * The Predicted  Percent  Dissatisfied  Due  to  Draft  (PD)

    * Predicted  Percent  Satisfied  With  the  Level  of  Air  Movement"   (PS)

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    tr : float or array-like
        mean radiant temperature, default in [°C] in [°F] if `units` = 'IP'
    v : float or array-like
        air speed, default in [m/s] in [fps] if `units` = 'IP'
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    clo : float or array-like
        clothing insulation, [clo]
    wme : float or array-like
        external work, [met] default 0
    body_surface_area : float
        body surface area, default value 1.8258 [m2] in [ft2] if `units` = 'IP'

        The body surface area can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.body_surface_area`.
    p_atmospheric : float
        atmospheric pressure, default value 101325 [Pa] in [atm] if `units` = 'IP'
    body_position: str default="standing" or array-like
        select either "sitting" or "standing"
    max_skin_blood_flow : float
        maximum blood flow from the core to the skin, [kg/h/m2] default 80

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output values, if False it does not round them
    max_sweating : float
        Maximum rate at which regulatory sweat is generated, [kg/h/m2]
    w_max : float
        Maximum skin wettedness (w) adimensional. Ranges from 0 and 1.

    Returns
    -------
    e_skin : float or array-like
        Total rate of evaporative heat loss from skin, [W/m2]. Equal to e_rsw + e_diff
    e_rsw : float or array-like
        Rate of evaporative heat loss from sweat evaporation, [W/m2]
    e_diff : float or array-like
        Rate of evaporative heat loss from moisture diffused through the skin, [W/m2]
    e_max : float or array-like
        Maximum rate of evaporative heat loss from skin, [W/m2]
    q_sensible : float or array-like
        Sensible heat loss from skin, [W/m2]
    q_skin : float or array-like
        Total rate of heat loss from skin, [W/m2]. Equal to q_sensible + e_skin
    q_res : float or array-like
        Total rate of heat loss through respiration, [W/m2]
    t_core : float or array-like
        Core temperature, [°C]
    t_skin : float or array-like
        Skin temperature, [°C]
    m_bl : float or array-like
        Skin blood flow, [kg/h/m2]
    m_rsw : float or array-like
        Rate at which regulatory sweat is generated, [kg/h/m2]
    w : float or array-like
        Skin wettedness, adimensional. Ranges from 0 and 1.
    w_max : float or array-like
        Skin wettedness (w) practical upper limit, adimensional. Ranges from 0 and 1.
    set : float or array-like
        Standard Effective Temperature (SET)
    et : float or array-like
        New Effective Temperature (ET)
    pmv_gagge : float or array-like
        PMV Gagge
    pmv_set : float or array-like
        PMV SET
    pd : float or array-like
        Predicted  Percent  Dissatisfied  Due  to  Draft"
    ps : float or array-like
        Predicted  Percent  Satisfied  With  the  Level  of  Air  Movement
    disc : float or array-like
        Thermal discomfort
    t_sens : float or array-like
        Predicted  Thermal  Sensation

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import two_nodes
        >>> print(two_nodes(tdb=25, tr=25, v=0.3, rh=50, met=1.2, clo=0.5))
        {'e_skin': 15.8, 'e_rsw': 6.5, 'e_diff': 9.3, ... }
        >>> print(two_nodes(tdb=[25, 25], tr=25, v=0.3, rh=50, met=1.2, clo=0.5))
        {'e_skin': array([15.8, 15.8]), 'e_rsw': array([6.5, 6.5]), ... }
    """
    default_kwargs = {
        "round": True,
        "calculate_ce": False,
        "max_sweating": 500,
        "w_max": False,
    }
    kwargs = {**default_kwargs, **kwargs}

    tdb = np.array(tdb)
    tr = np.array(tr)
    v = np.array(v)
    rh = np.array(rh)
    met = np.array(met)
    clo = np.array(clo)
    wme = np.array(wme)
    body_position = np.array(body_position)

    vapor_pressure = rh * p_sat_torr(tdb) / 100

    if kwargs["calculate_ce"]:
        result = two_nodes_optimized_return_set(
            tdb,
            tr,
            v,
            met,
            clo,
            vapor_pressure,
            wme,
            body_surface_area,
            p_atmospheric,
            1,
        )
        return {"_set": result}

    (
        _set,
        e_skin,
        e_rsw,
        e_max,
        q_sensible,
        q_skin,
        q_res,
        t_core,
        t_skin,
        m_bl,
        m_rsw,
        w,
        w_max,
        et,
        pmv_gagge,
        pmv_set,
        disc,
        t_sens,
    ) = np.vectorize(two_nodes_optimized, cache=True)(
        tdb=tdb,
        tr=tr,
        v=v,
        met=met,
        clo=clo,
        vapor_pressure=vapor_pressure,
        wme=wme,
        body_surface_area=body_surface_area,
        p_atmospheric=p_atmospheric,
        body_position=body_position,
        calculate_ce=kwargs["calculate_ce"],
        max_skin_blood_flow=max_skin_blood_flow,
        max_sweating=kwargs["max_sweating"],
        w_max=kwargs["w_max"],
    )

    output = {
        "e_skin": e_skin,
        "e_rsw": e_rsw,
        "e_max": e_max,
        "q_sensible": q_sensible,
        "q_skin": q_skin,
        "q_res": q_res,
        "t_core": t_core,
        "t_skin": t_skin,
        "m_bl": m_bl,
        "m_rsw": m_rsw,
        "w": w,
        "w_max": w_max,
        "_set": _set,
        "et": et,
        "pmv_gagge": pmv_gagge,
        "pmv_set": pmv_set,
        "disc": disc,
        "t_sens": t_sens,
    }

    for key in output.keys():
        # round the results if needed
        if kwargs["round"]:
            output[key] = np.around(output[key], 1)

    return output


def wbgt(twb, tg, tdb=None, with_solar_load=False, **kwargs):
    """Calculates the Wet Bulb Globe Temperature (WBGT) index calculated in
    compliance with the ISO 7243 [11]_. The WBGT is a heat stress index that
    measures the thermal environment to which a person is exposed. In most
    situations, this index is simple to calculate. It should be used as a
    screening tool to determine whether heat stress is present. The PHS model
    allows a more accurate estimation of stress. PHS can be calculated using
    the function :py:meth:`pythermalcomfort.models.phs`.

    The WBGT determines the impact of heat on a person throughout the course of a working
    day (up to 8 h). It does not apply to very brief heat exposures. It pertains to
    the evaluation of male and female people who are fit for work in both indoor
    and outdoor occupational environments, as well as other sorts of surroundings [11]_.

    The WBGT is defined as a function of only twb and tg if the person is not exposed to
    direct radiant heat from the sun. When a person is exposed to direct radiant heat,
    tdb must also be specified.

    Parameters
    ----------
    twb : float,
        natural (no forced air flow) wet bulb temperature, [°C]
    tg : float
        globe temperature, [°C]
    tdb : float
        dry bulb air temperature, [°C]. This value is needed as input if the person is
        exposed to direct solar radiation
    with_solar_load: bool
        True if the globe sensor is exposed to direct solar radiation

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output value, if False it does not round it

    Returns
    -------
    wbgt : float
        Wet Bulb Globe Temperature Index, [°C]

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import wbgt
        >>> wbgt(twb=25, tg=32)
        27.1

        >>> # if the persion is exposed to direct solar radiation
        >>> wbgt(twb=25, tg=32, tdb=20, with_solar_load=True)
        25.9
    """
    default_kwargs = {
        "round": True,
    }
    kwargs = {**default_kwargs, **kwargs}
    if with_solar_load:
        if tdb:
            t_wbg = 0.7 * twb + 0.2 * tg + 0.1 * tdb
        else:
            raise ValueError("Please enter the dry bulb air temperature")
    else:
        t_wbg = 0.7 * twb + 0.3 * tg

    if kwargs["round"]:
        return round(t_wbg, 1)
    else:
        return t_wbg


def net(tdb, rh, v, **kwargs):
    """Calculates the Normal Effective Temperature (NET). Missenard (1933)
    devised a formula for calculating effective temperature. The index
    establishes a link between the same condition of the organism's
    thermoregulatory capability (warm and cold perception) and the surrounding
    environment's temperature and humidity. The index is calculated as a
    function of three meteorological factors: air temperature, relative
    humidity of air, and wind speed. This index allows to calculate the
    effective temperature felt by a person. Missenard original equation was
    then used to calculate the Normal Effective Temperature (NET), by
    considering normal atmospheric pressure and a normal human body temperature
    (37°C). The NET is still in use in Germany, where medical check-ups for
    subjects working in the heat are decided on by prevailing levels of ET,
    depending on metabolic rates. The NET is also constantly monitored by the
    Hong Kong Observatory [16]_. In central Europe the following thresholds are
    in use: <1°C = very cold; 1–9 = cold; 9–17 = cool; 17–21 = fresh; 21–23 = comfortable;
    23–27 = warm; >27°C = hot [16]_.

    Parameters
    ----------
    tdb : float,
        dry bulb air temperature, [°C]
    rh : float
        relative humidity, [%]
    v : float
        wind speed [m/s] at 1.2 m above the ground

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output value, if False it does not round it

    Returns
    -------
    net : float
        Normal Effective Temperature, [°C]

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import net
        >>> net(tdb=37, rh=100, v=0.1)
        37
    """
    default_kwargs = {
        "round": True,
    }
    kwargs = {**default_kwargs, **kwargs}

    frac = 1.0 / (1.76 + 1.4 * v**0.75)

    et = 37 - (37 - tdb) / (0.68 - 0.0014 * rh + frac) - 0.29 * tdb * (1 - 0.01 * rh)

    if kwargs["round"]:
        return round(et, 1)
    else:
        return et


def heat_index(tdb, rh, **kwargs):
    """Calculates the Heat Index (HI). It combines air temperature and relative
    humidity to determine an apparent temperature. The HI equation [12]_ is
    derived by multiple regression analysis in temperature and relative
    humidity from the first version of Steadman’s (1979) apparent temperature
    (AT) [13]_.

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, default in [°C] in [°F] if `units` = 'IP'
    rh : float
        relative humidity, [%]

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output value, if False it does not round it
    units : {'SI', 'IP'}
        select the SI (International System of Units) or the IP (Imperial Units) system.

    Returns
    -------
    hi : float
        Heat Index, default in [°C] in [°F] if `units` = 'IP'

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import heat_index
        >>> heat_index(tdb=25, rh=50)
        25.9
    """
    default_kwargs = {
        "round": True,
        "units": "SI",
    }
    kwargs = {**default_kwargs, **kwargs}

    if kwargs["units"] == "SI":
        # from doi: 10.1007/s00484-011-0453-2
        hi = -8.784695 + 1.61139411 * tdb + 2.338549 * rh - 0.14611605 * tdb * rh
        hi += -1.2308094 * 10**-2 * tdb**2 - 1.6424828 * 10**-2 * rh**2
        hi += 2.211732 * 10**-3 * tdb**2 * rh + 7.2546 * 10**-4 * tdb * rh**2
        hi += -3.582 * 10**-6 * tdb**2 * rh**2

    else:
        # from doi: 10.1007/s00484-021-02105-0
        hi = -42.379 + 2.04901523 * tdb + 10.14333127 * rh
        hi += -0.22475541 * tdb * rh - 6.83783 * 10**-3 * tdb**2
        hi += -5.481717 * 10**-2 * rh**2
        hi += 1.22874 * 10**-3 * tdb**2 * rh + 8.5282 * 10**-4 * tdb * rh**2
        hi += -1.99 * 10**-6 * tdb**2 * rh**2

    if kwargs["round"]:
        return round(hi, 1)
    else:
        return hi


def discomfort_index(tdb, rh):
    """Calculates the Discomfort Index (DI). The index is essentially an
    effective temperature based on air temperature and humidity. The discomfort
    index is usuallly divided in 6 dicomfort categories and it only applies to
    warm environments: [24]_

    * class 1 - DI < 21 °C - No discomfort
    * class 2 - 21 <= DI < 24 °C - Less than 50% feels discomfort
    * class 3 - 24 <= DI < 27 °C - More than 50% feels discomfort
    * class 4 - 27 <= DI < 29 °C - Most of the population feels discomfort
    * class 5 - 29 <= DI < 32 °C - Everyone feels severe stress
    * class 6 - DI >= 32 °C - State of medical emergency

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, [°C]
    rh : float or array-like
        relative humidity, [%]

    Returns
    -------
    di : float or array-like
        Discomfort Index, [°C]
    discomfort_condition : str or array-like
        Classification of the thermal comfort conditions according to the discomfort index

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import discomfort_index
        >>> discomfort_index(tdb=25, rh=50)
        {'di': 22.1, 'discomfort_condition': 'Less than 50% feels discomfort'}
    """

    tdb = np.array(tdb)
    rh = np.array(rh)

    di = tdb - 0.55 * (1 - 0.01 * rh) * (tdb - 14.5)

    di_categories = {
        21: "No discomfort",
        24: "Less than 50% feels discomfort",
        27: "More than 50% feels discomfort",
        29: "Most of the population feels discomfort",
        32: "Everyone feels severe stress",
        99: "State of medical emergency",
    }

    return {
        "di": np.around(di, 1),
        "discomfort_condition": mapping(di, di_categories, right=False),
    }


def humidex(tdb, rh, **kwargs):
    """Calculates the humidex (short for "humidity index"). It has been
    developed by the Canadian Meteorological service. It was introduced in 1965
    and then it was revised by Masterson and Richardson (1979) [14]_. It aims
    to describe how hot, humid weather is felt by the average person. The
    Humidex differs from the heat index in being related to the dew point
    rather than relative humidity [15]_.

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, [°C]
    rh : float
        relative humidity, [%]

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output value, if False it does not round it

    Returns
    -------
    humidex: float
        Heat Index, [°C]
    discomfort: str
        Degree of Comfort or Discomfort as defined in Havenith and Fiala (2016) [15]_

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import humidex
        >>> humidex(tdb=25, rh=50)
        {"humidex": 28.2, "discomfort": "Little or no discomfort"}
    """
    default_kwargs = {
        "round": True,
    }
    kwargs = {**default_kwargs, **kwargs}

    hi = tdb + 5 / 9 * ((6.112 * 10 ** (7.5 * tdb / (237.7 + tdb)) * rh / 100) - 10)

    if kwargs["round"]:
        hi = round(hi, 1)

    stress_category = "Heat stroke probable"
    if hi <= 30:
        stress_category = "Little or no discomfort"
    elif hi <= 35:
        stress_category = "Noticeable discomfort"
    elif hi <= 40:
        stress_category = "Evident discomfort"
    elif hi <= 45:
        stress_category = "Intense discomfort; avoid exertion"
    elif hi <= 54:
        stress_category = "Dangerous discomfort"

    return {"humidex": hi, "discomfort": stress_category}


def at(tdb, rh, v, q=None, **kwargs):
    """Calculates the Apparent Temperature (AT). The AT is defined as the
    temperature at the reference humidity level producing the same amount of
    discomfort as that experienced under the current ambient temperature,
    humidity, and solar radiation [17]_. In other words, the AT is an
    adjustment to the dry bulb temperature based on the relative humidity
    value. Absolute humidity with a dew point of 14°C is chosen as a reference.

    [16]_. It includes the chilling effect of the wind at lower temperatures.

    Two formulas for AT are in use by the Australian Bureau of Meteorology: one includes
    solar radiation and the other one does not (http://www.bom.gov.au/info/thermal_stress/
    , 29 Sep 2021). Please specify q if you want to estimate AT with solar load.

    Parameters
    ----------
    tdb : float
        dry bulb air temperature,[°C]
    rh : float
        relative humidity, [%]
    v : float
        wind speed 10m above ground level, [m/s]
    q : float
        Net radiation absorbed per unit area of body surface [W/m2]

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output value, if False it does not round it

    Returns
    -------
    at: float
        apparent temperature, [°C]

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import at
        >>> at(tdb=25, rh=30, v=0.1)
        24.1
    """
    default_kwargs = {
        "round": True,
    }
    kwargs = {**default_kwargs, **kwargs}

    # dividing it by 100 since the at eq. requires p_vap to be in hPa
    p_vap = psy_ta_rh(tdb, rh)["p_vap"] / 100

    # equation sources [16] and http://www.bom.gov.au/info/thermal_stress/#apparent
    if q:
        t_at = tdb + 0.348 * p_vap - 0.7 * v + 0.7 * q / (v + 10) - 4.25
    else:
        t_at = tdb + 0.33 * p_vap - 0.7 * v - 4.00

    if kwargs["round"]:
        t_at = round(t_at, 1)

    return t_at


def wc(tdb, v, **kwargs):
    """Calculates the Wind Chill Index (WCI) in accordance with the ASHRAE 2017 Handbook Fundamentals - Chapter 9 [18]_.

    The wind chill index (WCI) is an empirical index based on cooling measurements
    taken on a cylindrical flask partially filled with water in Antarctica
    (Siple and Passel 1945). For a surface temperature of 33°C, the index describes
    the rate of heat loss from the cylinder via radiation and convection as a function
    of ambient temperature and wind velocity.

    This formulation has been met with some valid criticism. WCI is unlikely to be an
    accurate measure of heat loss from exposed flesh, which differs from plastic in terms
    of curvature, roughness, and radiation exchange qualities, and is always below 33°C
    in a cold environment. Furthermore, the equation's values peak at 90 km/h and then
    decline as velocity increases. Nonetheless, this score reliably represents the
    combined effects of temperature and wind on subjective discomfort for velocities
    below 80 km/h [18]_.

    Parameters
    ----------
    tdb : float
        dry bulb air temperature,[°C]
    v : float
        wind speed 10m above ground level, [m/s]

    Other Parameters
    ----------------
    round: boolean, default True
        if True rounds output value, if False it does not round it

    Returns
    -------
    wci: float
        wind chill index, [W/m2)]

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import wc
        >>> wc(tdb=-5, v=5.5)
        {"wci": 1255.2}
    """
    default_kwargs = {
        "round": True,
    }
    kwargs = {**default_kwargs, **kwargs}

    wci = (10.45 + 10 * v**0.5 - v) * (33 - tdb)

    # the factor 1.163 is used to convert to W/m2
    wci = wci * 1.163

    if kwargs["round"]:
        wci = round(wci, 1)

    return {"wci": wci}


def pet_steady(
    tdb,
    tr,
    v,
    rh,
    met,
    clo,
    p_atm=1013.25,
    position=1,
    age=23,
    sex=1,
    weight=75,
    height=1.8,
    wme=0,
):
    """
    The steady physiological equivalent temperature (PET) is calculated using the Munich
    Energy-balance Model for Individuals (MEMI), which simulates the human body's thermal
    circumstances in a medically realistic manner. PET is defined as the air temperature
    at which, in a typical indoor setting the heat budget of the human body is balanced
    with the same core and skin temperature as under the complex outdoor conditions to be
    assessed [20]_.
    The following assumptions are made for the indoor reference climate: tdb = tr, v = 0.1
    m/s, water vapour pressure = 12 hPa, clo = 0.9 clo, and met = 1.37 met + basic
    metabolism.
    PET allows a layperson to compare the total effects of complex thermal circumstances
    outside with his or her own personal experience indoors in this way. This function
    solves the heat balances without accounting for heat storage in the human body.

    The PET was originally proposed by Hoppe [20]_. In 2018, Walther and Goestchel [21]_
    proposed a correction of the original model, purging the errors in the
    PET calculation routine, and implementing a state-of-the-art vapour diffusion model.
    Walther and Goestchel (2018) model is therefore used to calculate the PET.

    Parameters
    ----------
    tdb : float
        dry bulb air temperature, [°C]
    tr : float
        mean radiant temperature, [°C]
    v : float
        air speed, [m/s]
    rh : float
        relative humidity, [%]
    met : float
        metabolic rate, [met]
    clo : float
        clothing insulation, [clo]
    p_atm : float
        atmospheric pressure, default value 1013.25 [hPa]
    position : int
        position of the individual (1=sitting, 2=standing, 3=standing, forced convection)
    age : int, default 23
        age in years
    sex : int, default 1
        male (1) or female (2).
    weight : float, default 75
        body mass, [kg]
    height: float, default 1.8
        height, [m]
    wme : float, default 0
        external work, [W/(m2)] default 0

    Returns
    -------
    PET
        Steady-state PET under the given ambient conditions

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import pet_steady
        >>> pet_steady(tdb=20, tr=20, rh=50, v=0.15, met=1.37, clo=0.5)
        18.85
    """

    met_factor = 58.2  # met conversion factor
    met = met * met_factor  # metabolic rate

    def solve_pet(
        t_arr,
        _tdb,
        _tr,
        _v=0.1,
        _rh=50,
        _met=80,
        _clo=0.9,
        actual_environment=False,
    ):
        """
        This function allows solving for the PET : either it solves the vectorial balance
        of the 3 unknown temperatures (T_core, T_sk, T_clo) or it solves for the
        environment operative temperature that would yield the same energy balance as the
        actual environment.

        Parameters
        ----------
        t_arr : list or array-like
            [T_core, T_sk, T_clo], [°C]
        _tdb : float
            dry bulb air temperature, [°C]
        _tr : float
            mean radiant temperature, [°C]
        _v : float, default 0.1 m/s for the reference environment
            air speed, [m/s]
        _rh : float, default 50 % for the reference environment
            relative humidity, [%]
        _met : float, default 80 W for the reference environment
            metabolic rate, [W/m2]
        _clo : float, default 0.9 clo for the reference environment
            clothing insulation, [clo]
        actual_environment : boolean
            True=solve 3eqs/3unknowns, False=solve for PET

        Returns
        -------
        float
            PET or energy balance.
        """

        def vasomotricity(t_cr, t_sk):
            """Defines the vasomotricity (blood flow) in function of the core
            and skin temperatures.

            Parameters
            ----------
            t_cr : float
                The body core temperature, [°C]
            t_sk : float
                The body skin temperature, [°C]

            Returns
            -------
            dict
                "m_blood": Blood flow rate, [kg/m2/h] and "alpha": repartition of body
                mass
                between core and skin [].
            """
            # skin and core temperatures set values
            tc_set = 36.6  # 36.8
            tsk_set = 34  # 33.7
            # Set value signals
            sig_skin = tsk_set - t_sk
            sig_core = t_cr - tc_set
            if sig_core < 0:
                # In this case, T_core<Tc_set --> the blood flow is reduced
                sig_core = 0.0
            if sig_skin < 0:
                # In this case, Tsk>Tsk_set --> the blood flow is increased
                sig_skin = 0.0
            # 6.3 L/m^2/h is the set value of the blood flow
            m_blood = (6.3 + 75.0 * sig_core) / (1.0 + 0.5 * sig_skin)
            # 90 L/m^2/h is the blood flow upper limit
            if m_blood > 90:
                m_blood = 90.0
            # in other models, alpha is used to update tbody
            alpha = 0.0417737 + 0.7451833 / (m_blood + 0.585417)

            return {"m_blood": m_blood, "alpha": alpha}

        def sweat_rate(t_body):
            """Defines the sweating mechanism depending on the body and core
            temperatures.

            Parameters
            ----------
            t_body : float
                weighted average between skin and core temperatures, [°C]

            Returns
            -------
            m_rsw : float
                The sweating flow rate, [g/m2/h].
            """
            tc_set = 36.6  # 36.8
            tsk_set = 34  # 33.7
            tbody_set = 0.1 * tsk_set + 0.9 * tc_set  # Calculation of the body
            # temperature
            # through a weighted average
            sig_body = t_body - tbody_set
            if sig_body < 0:
                # In this case, Tbody<Tbody_set --> The sweat flow is 0
                sig_body = 0.0
            # from Gagge's model
            m_rsw = 304.94 * 10**-3 * sig_body
            # 500 g/m^2/h is the upper sweat rate limit
            if m_rsw > 500:
                m_rsw = 500

            return m_rsw

        e_skin = 0.99  # Skin emissivity
        e_clo = 0.95  # Clothing emissivity
        h_vap = 2.42 * 10**6  # Latent heat of evaporation [J/Kg]
        sbc = 5.67 * 10**-8  # Stefan-Boltzmann constant [W/(m2*K^(-4))]
        cb = 3640  # Blood specific heat [J/kg/k]

        t_arr = np.reshape(t_arr, (3, 1))  # reshape to proper dimensions for fsolve
        e_bal_vec = np.zeros(
            (3, 1)
        )  # required for the vectorial expression of the balance
        # Area parameters of the body:
        a_dubois = body_surface_area(weight, height)
        # Base metabolism for men and women in [W]
        met_female = (
            3.19
            * weight**0.75
            * (
                1.0
                + 0.004 * (30.0 - age)
                + 0.018 * (height * 100.0 / weight ** (1.0 / 3.0) - 42.1)
            )
        )
        met_male = (
            3.45
            * weight**0.75
            * (
                1.0
                + 0.004 * (30.0 - age)
                + 0.01 * (height * 100.0 / weight ** (1.0 / 3.0) - 43.4)
            )
        )
        # Attribution of internal energy depending on the sex of the subject
        met_correction = met_male if sex == 1 else met_female

        # Source term : metabolic activity
        he = (_met + met_correction) / a_dubois
        # impact of efficiency
        h = he * (1.0 - wme)  # [W/m2]

        # correction for wind
        i_m = 0.38  # Woodcock ratio for vapour transfer through clothing [-]

        # Calculation of the Burton surface increase coefficient, k = 0.31 for Hoeppe:
        fcl = (
            1 + 0.31 * _clo
        )  # Increase heat exchange surface depending on clothing level
        f_a_cl = (
            173.51 * _clo - 2.36 - 100.76 * _clo * _clo + 19.28 * _clo**3.0
        ) / 100
        a_clo = a_dubois * f_a_cl + a_dubois * (fcl - 1.0)  # clothed body surface area

        f_eff = 0.696 if position == 2 else 0.725  # effective radiation factor

        a_r_eff = (
            a_dubois * f_eff
        )  # Effective radiative area depending on the position of the subject

        # Partial pressure of water in the air
        vpa = _rh / 100.0 * p_sat(_tdb) / 100  # [hPa]
        if not actual_environment:  # mode=False means we are calculating the PET
            vpa = 12  # [hPa] vapour pressure of the standard environment

        # Convection coefficient depending on wind velocity and subject position
        hc = 2.67 + 6.5 * _v**0.67  # sitting
        if position == 2:  # standing
            hc = 2.26 + 7.42 * _v**0.67
        if position == 3:  # standing, forced convection
            hc = 8.6 * _v**0.513
        # h_cc corrected convective heat transfer coefficient
        h_cc = 3.0 * pow(p_atm / 1013.25, 0.53)
        hc = max(h_cc, hc)
        # modification of hc with the total pressure
        hc = hc * (p_atm / 1013.25) ** 0.55

        # Respiratory energy losses
        t_exp = 0.47 * _tdb + 21.0  # Expired air temperature calculation [degC]
        d_vent_pulm = he * 1.44 * 10.0 ** (-6.0)  # breathing flow rate
        c_res = 1010 * (_tdb - t_exp) * d_vent_pulm  # Sensible heat energy loss [W/m2]
        vpexp = p_sat(t_exp) / 100  # Latent heat energy loss [hPa]
        q_res = 0.623 * h_vap / p_atm * (vpa - vpexp) * d_vent_pulm  # [W/m2]
        ere = c_res + q_res  # [W/m2]

        # Calculation of the equivalent thermal resistance of body tissues
        alpha = vasomotricity(t_arr[0, 0], t_arr[1, 0])["alpha"]
        tbody = alpha * t_arr[1, 0] + (1 - alpha) * t_arr[0, 0]

        # Clothed fraction of the body approximation
        r_cl = _clo / 6.45  # Conversion in [m2.K/W]
        y = 0
        if f_a_cl > 1.0:
            f_a_cl = 1.0
        if _clo >= 2.0:
            y = 1.0
        if 0.6 < _clo < 2.0:
            y = (height - 0.2) / height
        if 0.6 >= _clo > 0.3:
            y = 0.5
        if 0.3 >= _clo > 0.0:
            y = 0.1
        # calculation of the clothing radius depending on the clothing level (6.28 = 2*
        # pi !)
        r2 = a_dubois * (fcl - 1.0 + f_a_cl) / (6.28 * height * y)  # External radius
        r1 = f_a_cl * a_dubois / (6.28 * height * y)  # Internal radius
        di = r2 - r1
        # Calculation of the equivalent thermal resistance of body tissues
        htcl = 6.28 * height * y * di / (r_cl * np.log(r2 / r1) * a_clo)  # [W/(m2.K)]

        # Calculation of sweat losses
        qmsw = sweat_rate(tbody)
        # h_vap/1000 = 2400 000[J/kg] divided by 1000 = [J/g] // qwsw/3600 for [g/m2/h]
        # to [
        # g/m2/s]
        esw = h_vap / 1000 * qmsw / 3600  # [W/m2]
        # Saturation vapor pressure at temperature Tsk
        p_v_sk = p_sat(t_arr[1, 0]) / 100  # hPa
        # Calculation of vapour transfer
        lr = 16.7 * 10 ** (-1)  # [K/hPa] Lewis ratio
        he_diff = hc * lr  # diffusion coefficient of air layer
        fecl = 1 / (1 + 0.92 * hc * r_cl)  # Burton efficiency factor
        e_max = he_diff * fecl * (p_v_sk - vpa)  # maximum diffusion at skin surface
        if e_max == 0:  # added this otherwise e_req / e_max cannot be calculated
            e_max = 0.001
        w = esw / e_max  # skin wettedness
        if w > 1:
            w = 1
            delta = esw - e_max
            if delta < 0:
                esw = e_max
        if esw < 0:
            esw = 0
        # i_m= Woodcock's ratio (see above)
        r_ecl = (1 / (fcl * hc) + r_cl) / (
            lr * i_m
        )  # clothing vapour transfer resistance after Woodcock's method
        ediff = (1 - w) * (p_v_sk - vpa) / r_ecl  # diffusion heat transfer
        evap = -(ediff + esw)  # [W/m2]

        # Radiation losses bare skin
        r_bare = (
            a_r_eff
            * (1.0 - f_a_cl)
            * e_skin
            * sbc
            * ((_tr + 273.15) ** 4.0 - (t_arr[1, 0] + 273.15) ** 4.0)
            / a_dubois
        )
        # ... for clothed area
        r_clo = (
            f_eff
            * a_clo
            * e_clo
            * sbc
            * ((_tr + 273.15) ** 4.0 - (t_arr[2, 0] + 273.15) ** 4.0)
            / a_dubois
        )
        r_sum = r_clo + r_bare  # radiation total

        # Convection losses for bare skin
        c_bare = (
            hc * (_tdb - t_arr[1, 0]) * a_dubois * (1.0 - f_a_cl) / a_dubois
        )  # [W/m^2]
        # ... for clothed area
        c_clo = hc * (_tdb - t_arr[2, 0]) * a_clo / a_dubois  # [W/m^2]
        csum = c_clo + c_bare  # convection total

        # Balance equations of the 3-nodes model
        e_bal_vec[0, 0] = (
            h
            + ere
            - (vasomotricity(t_arr[0, 0], t_arr[1, 0])["m_blood"] / 3600 * cb + 5.28)
            * (t_arr[0, 0] - t_arr[1, 0])
        )  # Core balance [W/m^2]
        e_bal_vec[1, 0] = (
            r_bare
            + c_bare
            + evap
            + (vasomotricity(t_arr[0, 0], t_arr[1, 0])["m_blood"] / 3600 * cb + 5.28)
            * (t_arr[0, 0] - t_arr[1, 0])
            - htcl * (t_arr[1, 0] - t_arr[2, 0])
        )  # Skin balance [W/m^2]
        e_bal_vec[2, 0] = (
            c_clo + r_clo + htcl * (t_arr[1, 0] - t_arr[2, 0])
        )  # Clothes balance [W/m^2]
        e_bal_scal = h + ere + r_sum + csum + evap

        # returning either the calculated core,skin,clo temperatures or the PET
        if actual_environment:
            # if we solve for the system we need to return 3 temperatures
            return [e_bal_vec[0, 0], e_bal_vec[1, 0], e_bal_vec[2, 0]]
        else:
            # solving for the PET requires the scalar balance only
            return e_bal_scal

    def pet_fc(_t_stable):
        """Function to find the solution.

        Parameters
        ----------
        _t_stable : list or array-like
            3 temperatures obtained from the actual environment (T_core,T_skin,T_clo).

        Returns
        -------
        float
            The PET comfort index.
        """

        # Definition of a function with the input variables of the PET reference situation
        def f(tx):
            return solve_pet(
                _t_stable,
                _tdb=tx,
                _tr=tx,
                actual_environment=False,
            )

        # solving for PET
        pet_guess = _t_stable[2]  # start with the clothing temperature

        return round(optimize.fsolve(f, pet_guess)[0], 2)

    # initial guess
    t_guess = np.array([36.7, 34, 0.5 * (tdb + tr)])
    # solve for Tc, Tsk, Tcl temperatures
    t_stable = optimize.fsolve(
        solve_pet,
        t_guess,
        args=(
            tdb,
            tr,
            v,
            rh,
            met,
            clo,
            True,
        ),
    )
    # compute PET
    return pet_fc(t_stable)


def athb(tdb, tr, vr, rh, met, t_running_mean):
    """Return the PMV value calculated with the Adaptive Thermal Heat Balance
    Framework [27]_. The adaptive thermal heat balance (ATHB) framework
    introduced a method to account for the three adaptive principals, namely
    physiological, behavioral, and psychological adaptation, individually
    within existing heat balance models. The objective is a predictive model of
    thermal sensation applicable during the design stage or in international
    standards without knowing characteristics of future occupants.

    Parameters
    ----------
    tdb : float or array-like
        dry bulb air temperature, in [°C]
    tr : float or array-like
        mean radiant temperature, in [°C]
    vr : float or array-like
        relative air speed, in [m/s]

        Note: vr is the relative air speed caused by body movement and not the air
        speed measured by the air speed sensor. The relative air speed is the sum of the
        average air speed measured by the sensor plus the activity-generated air speed
        (Vag). Where Vag is the activity-generated air speed caused by motion of
        individual body parts. vr can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.v_relative`.
    rh : float or array-like
        relative humidity, [%]
    met : float or array-like
        metabolic rate, [met]
    t_running_mean: float or array-like
        running mean temperature, in [°C]

        The running mean temperature can be calculated using the function
        :py:meth:`pythermalcomfort.utilities.running_mean_outdoor_temperature`.

    Returns
    -------
    athb_pmv : float or array-like
        Predicted Mean Vote calculated with the Adaptive Thermal Heat Balance framework

    Examples
    --------
    .. code-block:: python

        >>> from pythermalcomfort.models import athb
        >>> print(athb( tdb=[25, 27], tr=25, vr=0.1, rh=50, met=1.1, t_running_mean=20))
        [0.2, 0.209]
    """
    tdb = np.array(tdb)
    tr = np.array(tr)
    vr = np.array(vr)
    met = np.array(met)
    rh = np.array(rh)
    t_running_mean = np.array(t_running_mean)

    met_adapted = met - (0.234 * t_running_mean) / 58.2

    # adapted clothing insulation level through behavioural adaptation
    clo_adapted = np.power(
        10,
        (
            -0.17168
            - 0.000485 * t_running_mean
            + 0.08176 * met_adapted
            - 0.00527 * t_running_mean * met_adapted
        ),
    )

    pmv_res = pmv_ppd_optimized(tdb, tr, vr, rh, met_adapted, clo_adapted, 0)
    ts = 0.303 * np.exp(-0.036 * met_adapted * 58.15) + 0.028
    l_adapted = pmv_res / ts

    # predicted thermal sensation vote
    return np.around(
        1.484
        + 0.0276 * l_adapted
        - 0.9602 * met_adapted
        - 0.0342 * t_running_mean
        + 0.0002264 * l_adapted * t_running_mean
        + 0.018696 * met_adapted * t_running_mean
        - 0.0002909 * l_adapted * met_adapted * t_running_mean,
        3,
    )


# # testing morris equation
# from scipy import optimize
# import matplotlib.pyplot as plt
# import numpy as np
# f, ax = plt.subplots()
# for person in ["young", "old", "meds"]:
#     t_lim = []
#     rh_array = list(range(5, 100))
#     for rh in rh_array:
#
#         def function(x):
#             return use_fans_morris(x, 3.5, rh, 70, target_person=person)
#
#         t_lim.append(optimize.brentq(function, 30, 70))
#
#     z = np.polyfit(rh_array, t_lim, 4)
#     p = np.poly1d(z)
#     y_new = p(rh_array)
#     # plt.plot(rh_array, t_lim, "o")
#     plt.plot(rh_array, y_new, "-", label=person)
# ax.set(
#     ylabel="Temperature [°C]",
#     xlabel="Relative Humidity [Rh]",
#     ylim=(24, 52),
#     xlim=(5, 70),
# )
# plt.legend()


# include also the following models:
#  radiant_tmp_asymmetry
#  draft
#  floor_surface_tmp
#  Perceived temperature (Blazejczyk2012)
#  Physiological subjective temperature and physiological strain (Blazejczyk2012)
#  more models here: https://www.rdocumentation.org/packages/comf/versions/0.1.9
#  more models here: https://rdrr.io/cran/comf/man/
#  to print the R source code use comf::pmv


class JOS3:
    """JOS-3 model simulates human thermal physiology including skin
    temperature, core temperature, sweating rate, etc. for the whole body and
    17 local body parts.

    This model was developed at Shin-ichi Tanabe Laboratory, Waseda University
    and was derived from 65 Multi-Node model (https://doi.org/10.1016/S0378-7788(02)00014-2)
    and JOS-2 model (https://doi.org/10.1016/j.buildenv.2013.04.013).

    To use this model, create an instance of the JOS3 class with optional body parameters
    such as body height, weight, age, sex, etc.

    Environmental conditions such as air temperature, mean radiant temperature, air velocity, etc.
    can be set using the setter methods. (ex. X.tdb, X.tr X.v)
    If you want to set the different conditions in each body part, set them
    as a 17 lengths of list, dictionary, or numpy array format.

    List or numpy array format input must be 17 lengths and means the order of "head", "neck", "chest",
    "back", "pelvis", "left_shoulder", "left_arm", "left_hand", "right_shoulder", "right_arm",
    "right_hand", "left_thigh", "left_leg", "left_foot", "right_thigh", "right_leg" and "right_foot".

    The model output includes local and mean skin temperature, local core temperature,
    local and mean skin wettedness, and heat loss from the skin etc.
    The model output can be accessed using "dict_results()" method and be converted to a csv file
    using "to_csv" method.
    Each output parameter also can be accessed using getter methods.
    (ex. X.t_skin, X.t_skin_mean, X.t_core)

    If you use this package, please cite us as follows and mention the version of pythermalcomfort used:
    Y. Takahashi, A. Nomoto, S. Yoda, R. Hisayama, M. Ogata, Y. Ozeki, S. Tanabe,
    Thermoregulation Model JOS-3 with New Open Source Code, Energy & Buildings (2020),
    doi: https://doi.org/10.1016/j.enbuild.2020.110575

    Note: To maintain consistency in variable names for pythermalcomfort,
    some variable names differ from those used in the original paper.
    """

    def __init__(
        self,
        height=Default.height,
        weight=Default.weight,
        fat=Default.body_fat,
        age=Default.age,
        sex=Default.sex,
        ci=Default.cardiac_index,
        bmr_equation=Default.bmr_equation,
        bsa_equation=Default.bsa_equation,
        ex_output=None,
    ):
        """Initialize a new instance of JOS3 class, which is designed to model
        and simulate various physiological parameters related to human
        thermoregulation.

        This class uses mathematical models to calculate and predict
        body temperature, basal metabolic rate, body surface area, and
        other related parameters.

        Parameters
        ----------
        height : float, optional
            body height, in [m]. The default is 1.72.
        weight : float, optional
            body weight, in [kg]. The default is 74.43.
        fat : float, optional
            fat percentage, in [%]. The default is 15.
        age : int, optional
            age, in [years]. The default is 20.
        sex : str, optional
            sex ("male" or "female"). The default is "male".
        ci : float, optional
            Cardiac index, in [L/min/m2]. The default is 2.6432.
        bmr_equation : str, optional
            The equation used to calculate basal metabolic rate (BMR). Choose a BMR equation.
            The default is "harris-benedict" equation created uding Caucasian's data. (DOI: doi.org/10.1073/pnas.4.12.370)
            If the Ganpule's equation (DOI: doi.org/10.1038/sj.ejcn.1602645) for Japanese people is used, input "japanese".
        bsa_equation : str, optional
            The equation used to calculate body surface area (bsa). Choose a bsa equation.
            You can choose "dubois", "fujimoto", "kruazumi", or "takahira". The default is "dubois".
            The body surface area can be calculated using the function
            :py:meth:`pythermalcomfort.utilities.body_surface_area`.
        ex_output : None, list or "all", optional
            This is used when you want to display results other than the default output parameters (ex.skin temperature);
            by default, JOS outputs only the most necessary parameters in order to reduce the computational load.
            If the parameters other than the default output parameters are needed,
            specify the list of the desired parameter names in string format like ["bf_skin", "bf_core", "t_artery"].
            If you want to display all output results, set ex_output is "all".

        Attributes
        ----------
        tdb : float or array-like
            Dry bulb air temperature [°C].
        tr : float or array-like
            Mean radiant temperature [°C].
        to : float or array-like
            Operative temperature [°C].
        v : float or array-like
            Air speed [m/s].
        rh : float or array-like
            Relative humidity [%].
        clo : float or array-like
            Clothing insulation [clo].
            Note: If you want to input clothing insulation to each body part,
            it can be input using the dictionaly in "utilities.py" in "jos3_function" folder.
            :py:meth:`pythermalcomfort.jos3_functions.utilities.local_clo_typical_ensembles`.
        par : float
            Physical activity ratio [-].
            This equals the ratio of metabolic rate to basal metabolic rate.
            The par of sitting quietly is 1.2.
        posture : str
            Body posture [-]. Choose a posture from standing, sitting or lying.
        body_temp : numpy.ndarray (85,)
            All segment temperatures of JOS-3

        Methods
        -------
        simulate(times, dtime, output):
            Run JOS-3 model for given times.
        dict_results():
            Get results as a dictionary with pandas.DataFrame values.
        to_csv(path=None, folder=None, unit=True, meaning=True):
            Export results as csv format.

        Returns
        -------
        cardiac_output: cardiac output (the sum of the whole blood flow) [L/h]
        cycle_time: the counts of executing one cycle calculation [-]
        dt      : time step [sec]
        pythermalcomfort_version: version of pythermalcomfort [-]
        q_res   : heat loss by respiration [W]
        q_skin2env: total heat loss from the skin (each body part) [W]
        q_thermogenesis_total: total thermogenesis of the whole body [W]
        simulation_time: simulation times [sec]
        t_core  : core temperature (each body part) [°C]
        t_skin  : skin temperature (each body part) [°C]
        t_skin_mean: mean skin temperature [°C]
        w       : skin wettedness (each body part) [-]
        w_mean  : mean skin wettedness [-]
        weight_loss_by_evap_and_res: weight loss by the evaporation and respiration of the whole body [g/sec]
        OPTIONAL PARAMETERS : the paramters listed below are returned if ex_output = "all"
        age     : age [years]
        bf_ava_foot: AVA blood flow rate of one foot [L/h]
        bf_ava_hand: AVA blood flow rate of one hand [L/h]
        bf_core : core blood flow rate (each body part) [L/h]
        bf_fat  : fat blood flow rate (each body part) [L/h]
        bf_muscle: muscle blood flow rate (each body part) [L/h]
        bf_skin : skin blood flow rate (each body part) [L/h]
        bsa     : body surface area (each body part) [m2]
        clo     : clothing insulation (each body part) [clo]
        e_max   : maximum evaporative heat loss from the skin (each body part) [W]
        e_skin  : evaporative heat loss from the skin (each body part) [W]
        e_sweat : evaporative heat loss from the skin by only sweating (each body part) [W]
        fat     : body fat rate [%]
        height  : body height [m]
        name    : name of the model [-]
        par     : physical activity ratio [-]
        q_bmr_core: core thermogenesis by basal metabolism (each body part) [W]
        q_bmr_fat: fat thermogenesis by basal metabolism (each body part) [W]
        q_bmr_muscle: muscle thermogenesis by basal metabolism (each body part) [W]
        q_bmr_skin: skin thermogenesis by basal metabolism (each body part) [W]
        q_nst   : core thermogenesis by non-shivering (each body part) [W]
        q_res_latent: latent heat loss by respiration (each body part) [W]
        q_res_sensible: sensible heat loss by respiration (each body part) [W]
        q_shiv  : core or muscle thermogenesis by shivering (each body part) [W]
        q_skin2env_latent: latent heat loss from the skin (each body part) [W]
        q_skin2env_sensible: sensible heat loss from the skin (each body part) [W]
        q_thermogenesis_core: core total thermogenesis (each body part) [W]
        q_thermogenesis_fat: fat total thermogenesis (each body part) [W]
        q_thermogenesis_muscle: muscle total thermogenesis (each body part) [W]
        q_thermogenesis_skin: skin total thermogenesis (each body part) [W]
        q_work  : core or muscle thermogenesis by work (each body part) [W]
        r_et    : total clothing evaporative heat resistance (each body part) [(m2*kPa)/W]
        r_t     : total clothing heat resistance (each body part) [(m2*K)/W]
        rh      : relative humidity (each body part) [%]
        sex     : sex [-]
        t_artery: arterial temperature (each body part) [°C]
        t_cb    : central blood temperature [°C]
        t_core_set: core set point temperature (each body part) [°C]
        t_fat   : fat temperature (each body part) [°C]
        t_muscle: muscle temperature (each body part) [°C]
        t_skin_set: skin set point temperature (each body part) [°C]
        t_superficial_vein: superficial vein temperature (each body part) [°C]
        t_vein  : vein temperature (each body part) [°C]
        tdb     : dry bulb air temperature (each body part) [°C]
        to      : operative temperature (each body part) [°C]
        tr      : mean radiant temperature (each body part) [°C]
        v       : air velocity (each body part) [m/s]
        weight  : body weight [kg]


        Examples
        --------
        Build a model and set a body built
        Create an instance of the JOS3 class with optional body parameters such as body height, weight, age, sex, etc.

        .. code-block:: python

            >>> import numpy as np
            >>> import pandas as pd
            >>> import matplotlib.pyplot as plt
            >>> import os
            >>> from pythermalcomfort.models import JOS3
            >>> from pythermalcomfort.jos3_functions.utilities import local_clo_typical_ensembles
            >>>
            >>> directory_name = "jos3_output_example"
            >>> current_directory = os.getcwd()
            >>> jos3_example_directory = os.path.join(current_directory, directory_name)
            >>> if not os.path.exists(jos3_example_directory):
            >>>     os.makedirs(jos3_example_directory)
            >>>
            >>> model = JOS3(
            >>>     height=1.7,
            >>>     weight=60,
            >>>     fat=20,
            >>>     age=30,
            >>>     sex="male",
            >>>     bmr_equation="japanese",
            >>>     bsa_equation="fujimoto",
            >>>     ex_output="all",
            >>> )
            >>> # Set environmental conditions such as air temperature, mean radiant temperature using the setter methods.
            >>> # Set the first condition
            >>> # Environmental parameters can be input as int, float, list, dict, numpy array format.
            >>> model.tdb = 28  # Air temperature [°C]
            >>> model.tr = 30  # Mean radiant temperature [°C]
            >>> model.rh = 40  # Relative humidity [%]
            >>> model.v = np.array( # Air velocity [m/s]
            >>>     [
            >>>         0.2,  # head
            >>>         0.4,  # neck
            >>>         0.4,  # chest
            >>>         0.1,  # back
            >>>         0.1,  # pelvis
            >>>         0.4,  # left shoulder
            >>>         0.4,  # left arm
            >>>         0.4,  # left hand
            >>>         0.4,  # right shoulder
            >>>         0.4,  # right arm
            >>>         0.4,  # right hand
            >>>         0.1,  # left thigh
            >>>         0.1,  # left leg
            >>>         0.1,  # left foot
            >>>         0.1,  # right thigh
            >>>         0.1,  # right leg
            >>>         0.1,  # right foot
            >>>     ]
            >>> )
            >>> model.clo = local_clo_typical_ensembles["briefs, socks, undershirt, work jacket, work pants, safety shoes"]["local_body_part"]
            >>> # par should be input as int, float.
            >>> model.par = 1.2  # Physical activity ratio [-], assuming a sitting position
            >>> # posture should be input as int (0, 1, or 2) or str ("standing", "sitting" or "lying").
            >>> # (0="standing", 1="sitting" or 2="lying")
            >>> model.posture = "sitting"  # Posture [-], assuming a sitting position
            >>>
            >>> # Run JOS-3 model
            >>> model.simulate(
            >>>     times=30,  # Number of loops of a simulation
            >>>     dtime=60,  # Time delta [sec]. The default is 60.
            >>> )  # Exposure time = 30 [loops] * 60 [sec] = 30 [min]
            >>> # Set the next condition (You only need to change the parameters that you want to change)
            >>> model.to = 20  # Change operative temperature
            >>> model.v = { # Air velocity [m/s], assuming to use a desk fan
            >>>     'head' : 0.2,
            >>>     'neck' : 0.4,
            >>>     'chest' : 0.4,
            >>>     'back': 0.1,
            >>>     'pelvis' : 0.1,
            >>>     'left_shoulder' : 0.4,
            >>>     'left_arm' : 0.4,
            >>>     'left_hand' : 0.4,
            >>>     'right_shoulder' : 0.4,
            >>>     'right_arm' : 0.4,
            >>>     'right_hand' : 0.4,
            >>>     'left_thigh' : 0.1,
            >>>     'left_leg' : 0.1,
            >>>     'left_foot' : 0.1,
            >>>     'right_thigh' : 0.1,
            >>>     'right_leg' : 0.1,
            >>>     'right_foot' : 0.1
            >>>     }
            >>> # Run JOS-3 model
            >>> model.simulate(
            >>>     times=60,  # Number of loops of a simulation
            >>>     dtime=60,  # Time delta [sec]. The default is 60.
            >>> )  # Additional exposure time = 60 [loops] * 60 [sec] = 60 [min]
            >>> # Set the next condition (You only need to change the parameters that you want to change)
            >>> model.tdb = 30  # Change air temperature [°C]
            >>> model.tr = 35  # Change mean radiant temperature [°C]
            >>> # Run JOS-3 model
            >>> model.simulate(
            >>>     times=30,  # Number of loops of a simulation
            >>>     dtime=60,  # Time delta [sec]. The default is 60.
            >>> )  # Additional exposure time = 30 [loops] * 60 [sec] = 30 [min]
            >>> # Show the results
            >>> df = pd.DataFrame(model.dict_results())  # Make pandas.DataFrame
            >>> df[["t_skin_mean", "t_skin_head", "t_skin_chest", "t_skin_left_hand"]].plot()  # Plot time series of local skin temperature.
            >>> plt.legend(["Mean", "Head", "Chest", "Left hand"])  # Reset the legends
            >>> plt.ylabel("Skin temperature [°C]")  # Set y-label as 'Skin temperature [°C]'
            >>> plt.xlabel("Time [min]")  # Set x-label as 'Time [min]'
            >>> plt.savefig(os.path.join(jos3_example_directory, "jos3_example2_skin_temperatures.png"))  # Save plot at the current directory
            >>> plt.show()  # Show the plot
            >>> # Exporting the results as csv
            >>> model.to_csv(os.path.join(jos3_example_directory, "jos3_example2 (all output).csv"))
        """

        # Version of pythermalcomfort
        version_string = (
            __version__  # get the current version of pythermalcomfort package
        )
        version_number_string = re.findall("\d+\.\d+\.\d+", version_string)[0]
        self._version = version_number_string  # (ex. 'X.Y.Z')

        # Initialize basic attributes
        self._height = height
        self._weight = weight
        self._fat = fat
        self._sex = sex
        self._age = age
        self._ci = ci
        self._bmr_equation = bmr_equation
        self._bsa_equation = bsa_equation
        self._ex_output = ex_output

        # Calculate body surface area (bsa) rate
        self._bsa_rate = cons.bsa_rate(height, weight, bsa_equation)

        # Calculate local body surface area
        self._bsa = cons.local_bsa(height, weight, bsa_equation)

        # Calculate basal blood flow (BFB) rate [-]
        self._bfb_rate = cons.bfb_rate(height, weight, bsa_equation, age, ci)

        # Calculate thermal conductance (CDT) [W/K]
        self._cdt = cons.conductance(height, weight, bsa_equation, fat)

        # Calculate thermal capacity [J/K]
        self._cap = cons.capacity(height, weight, bsa_equation, age, ci)

        # Set initial core and skin temperature set points [°C]
        self.setpt_cr = np.ones(17) * Default.core_temperature
        self.setpt_sk = np.ones(17) * Default.skin_temperature

        # Initialize body temperature [°C]
        self._bodytemp = np.ones(NUM_NODES) * Default.other_body_temperature

        # Initialize environmental conditions and other factors
        # (Default values of input conditions)
        self._ta = np.ones(17) * Default.dry_bulb_air_temperature
        self._tr = np.ones(17) * Default.mean_radiant_temperature
        self._rh = np.ones(17) * Default.relative_humidity
        self._va = np.ones(17) * Default.air_speed
        self._clo = np.ones(17) * Default.clothing_insulation
        self._iclo = np.ones(17) * Default.clothing_vapor_permeation_efficiency
        self._par = Default.physical_activity_ratio
        self._posture = Default.posture
        self._hc = None  # Convective heat transfer coefficient
        self._hr = None  # Radiative heat transfer coefficient
        self.ex_q = np.zeros(NUM_NODES)  # External heat gain
        self._t = dt.timedelta(0)  # Elapsed time
        self._cycle = 0  # Cycle time
        self.model_name = "JOS3"  # Model name
        self.options = {
            "nonshivering_thermogenesis": True,
            "cold_acclimated": False,
            "shivering_threshold": False,
            "limit_dshiv/dt": False,
            "bat_positive": False,
            "ava_zero": False,
            "shivering": False,
        }

        # Set shivering threshold = 0
        threg.PRE_SHIV = 0

        # Initialize history to store model parameters
        self._history = []

        # Set elapsed time and cycle time to 0
        self._t = dt.timedelta(0)  # Elapsed time
        self._cycle = 0  # Cycle time

        # Reset set-point temperature and save the last model parameters
        dictout = self._reset_setpt(par=Default.physical_activity_ratio)
        self._history.append(dictout)

    def _calculate_operative_temp_when_pmv_is_zero(
        self,
        va=Default.air_speed,
        rh=Default.relative_humidity,
        met=Default.metabolic_rate,
        clo=Default.clothing_insulation,
    ) -> float:
        """Calculate operative temperature [°C] when PMV=0.

        Parameters
        ----------
        va : float, optional
            Air velocity [m/s]. The default is 0.1.
        rh : float, optional
            Relative humidity [%]. The default is 50.
        met : float, optional
            Metabolic rate [met]. The default is 1.
        clo : float, optional
            Clothing insulation [clo]. The default is 0.

        Returns
        -------
        to : float
            Operative temperature [°C].
        """

        to = 28  # initial operative temperature
        # Iterate until the PMV (Predicted Mean Vote) value is less than 0.001
        for _ in range(100):
            vpmv = pmv(tdb=to, tr=to, vr=va, rh=rh, met=met, clo=clo)
            # Break the loop if the absolute value of PMV is less than 0.001
            if abs(vpmv) < 0.001:
                break
            # Update the temperature based on the PMV value
            else:
                to = to - vpmv / 3
        return to

    def _reset_setpt(self, par=Default.physical_activity_ratio):
        """Reset set-point temperatures under steady state calculation.
        Set-point temperatures are hypothetical core or skin temperatures in a thermally neutral state
        when at rest (similar to room set-point temperature for air conditioning).
        This function is used during initialization to calculate the set-point temperatures as a reference for thermoregulation.
        Be careful, input parameters (tdb, tr, rh, v, clo, par) and body temperatures are also reset.

        Returns
        -------
        dict
            Parameters of JOS-3 model.
        """
        # Set operative temperature under PMV=0 environment
        # 1 met = 58.15 W/m2
        w_per_m2_to_met = 1 / 58.15  # unit converter W/m2 to met
        met = self.bmr * par * w_per_m2_to_met  # [met]
        self.to = self._calculate_operative_temp_when_pmv_is_zero(met=met)
        self.rh = Default.relative_humidity
        self.v = Default.air_speed
        self.clo = Default.clothing_insulation
        self.par = par  # Physical activity ratio

        # Steady-calculation
        self.options["ava_zero"] = True
        for _ in range(10):
            dict_out = self._run(dtime=60000, passive=True)

        # Set new set-point temperatures for core and skin
        self.setpt_cr = self.t_core
        self.setpt_sk = self.t_skin
        self.options["ava_zero"] = False

        return dict_out

    def simulate(self, times, dtime=60, output=True):
        """Run JOS-3 model.

        Parameters
        ----------
        times : int
            Number of loops of a simulation.
        dtime : int or float, optional
            Time delta in seconds. The default is 60.
        output : bool, optional
            If you don't want to record parameters, set False. The default is True.

        Returns
        -------
        None.
        """
        # Loop through the simulation for the given number of times
        for _ in range(times):
            # Increment the elapsed time by the time delta
            self._t += dt.timedelta(0, dtime)

            # Increment the cycle counter
            self._cycle += 1

            # Execute the simulation step
            dict_data = self._run(dtime=dtime, output=output)

            # If output is True, append the results to the history
            if output:
                self._history.append(dict_data)

    def _run(self, dtime=60, passive=False, output=True):
        """Runs the model once and gets the model parameters.

        The function then calculates several thermoregulation parameters using the input data,
        such as convective and radiative heat transfer coefficients, operative temperature, heat resistance,
        and blood flow rates.

        It also calculates the thermogenesis by shivering and non-shivering, basal thermogenesis, and thermogenesis by work.

        The function then calculates the total heat loss and gains, including respiratory,
        sweating, and extra heat gain, and builds the matrices required
        to solve for the new body temperature.

        It then calculates the new body temperature by solving the matrices using numpy's linalg library.

        Finally, the function returns a dictionary of the simulation results.
        The output parameters include cycle time, model time, t_skin_mean, t_skin, t_core, w_mean, w, weight_loss_by_evap_and_res, cardiac_output, q_thermogenesis_total, q_res, and q_skin_env.

        Additionally, if the _ex_output variable is set to "all" or is a list of keys,
        the function also returns a detailed dictionary of all the thermoregulation parameters
        and other variables used in the simulation.

        Parameters
        ----------
        dtime : int or float, optional
            Time delta [sec]. Default is 60.
        passive : bool, optional
            If you run a passive model, set to True. Default is False.
        output : bool, optional
            If you don't need parameters, set to False. Default is True.

        Returns
        -------
        dict_out : dictionary
            Output parameters.
        """

        # Compute convective and radiative heat transfer coefficient [W/(m2*K)]
        # based on posture, air velocity, air temperature, and skin temperature.
        # Manual setting is possible by setting self._hc and self._hr.
        # Compute heat and evaporative heat resistance [m2.K/W], [m2.kPa/W]

        # Get core and skin temperatures
        tcr = self.t_core
        tsk = self.t_skin

        # Convective and radiative heat transfer coefficients [W/(m2*K)]
        hc = threg.fixed_hc(
            threg.conv_coef(
                self._posture,
                self._va,
                self._ta,
                tsk,
            ),
            self._va,
        )
        hr = threg.fixed_hr(
            threg.rad_coef(
                self._posture,
            )
        )

        # Manually set convective and radiative heat transfer coefficients if necessary
        if self._hc is not None:
            hc = self._hc
        if self._hr is not None:
            hr = self._hr

        # Compute operative temp. [°C], clothing heat and evaporative resistance [m2.K/W], [m2.kPa/W]
        # Operative temp. [°C]
        to = threg.operative_temp(
            self._ta,
            self._tr,
            hc,
            hr,
        )
        # Clothing heat resistance [m2.K/W]
        r_t = threg.dry_r(hc, hr, self._clo)
        # Clothing evaporative resistance [m2.kPa/W]
        r_et = threg.wet_r(hc, self._clo, self._iclo)

        # ------------------------------------------------------------------
        # Thermoregulation
        # 1) Sweating
        # 2) Vasoconstriction, Vasodilation
        # 3) Shivering and non-shivering thermogenesis
        # ------------------------------------------------------------------

        # Compute the difference between the set-point temperature and body temperatures
        # and other thermoregulation parameters.
        # If running a passive model, the set-point temperature of thermoregulation is
        # set to the current body temperature.

        # set-point temperature for thermoregulation
        if passive:
            setpt_cr = tcr.copy()
            setpt_sk = tsk.copy()
        else:
            setpt_cr = self.setpt_cr.copy()
            setpt_sk = self.setpt_sk.copy()

        # Error signal = Difference between set-point and body temperatures
        err_cr = tcr - setpt_cr
        err_sk = tsk - setpt_sk

        # SWEATING THERMOREGULATION
        # Skin wettedness [-], e_skin, e_max, e_sweat [W]
        # Calculate skin wettedness, sweating heat loss, maximum sweating rate, and total sweat rate
        wet, e_sk, e_max, e_sweat = threg.evaporation(
            err_cr,
            err_sk,
            tsk,
            self._ta,
            self._rh,
            r_et,
            self._height,
            self._weight,
            self._bsa_equation,
            self._age,
        )

        # VASOCONSTRICTION, VASODILATION
        # Calculate skin blood flow and basal skin blood flow [L/h]
        bf_skin = threg.skin_blood_flow(
            err_cr,
            err_sk,
            self._height,
            self._weight,
            self._bsa_equation,
            self._age,
            self._ci,
        )

        # Calculate hands and feet's AVA blood flow [L/h]
        bf_ava_hand, bf_ava_foot = threg.ava_blood_flow(
            err_cr,
            err_sk,
            self._height,
            self._weight,
            self._bsa_equation,
            self._age,
            self._ci,
        )
        if self.options["ava_zero"] and passive:
            bf_ava_hand = 0
            bf_ava_foot = 0

        # SHIVERING AND NON-SHIVERING
        # Calculate shivering thermogenesis [W]
        q_shiv = threg.shivering(
            err_cr,
            err_sk,
            tcr,
            tsk,
            self._height,
            self._weight,
            self._bsa_equation,
            self._age,
            self._sex,
            dtime,
            self.options,
        )

        # Calculate non-shivering thermogenesis (NST) [W]
        if self.options["nonshivering_thermogenesis"]:
            q_nst = threg.nonshivering(
                err_sk,
                self._height,
                self._weight,
                self._bsa_equation,
                self._age,
                self.options["cold_acclimated"],
                self.options["bat_positive"],
            )
        else:  # not consider NST
            q_nst = np.zeros(17)

        # ------------------------------------------------------------------
        # Thermogenesis
        # ------------------------------------------------------------------

        # Calculate local basal metabolic rate (BMR) [W]
        q_bmr_local = threg.local_mbase(
            self._height,
            self._weight,
            self._age,
            self._sex,
            self._bmr_equation,
        )
        # Calculate overall basal metabolic rate (BMR) [W]
        q_bmr_total = sum([m.sum() for m in q_bmr_local])

        # Calculate thermogenesis by work [W]
        q_work = threg.local_q_work(q_bmr_total, self._par)

        # Calculate the sum of thermogenesis in core, muscle, fat, skin [W]
        (
            q_thermogenesis_core,
            q_thermogenesis_muscle,
            q_thermogenesis_fat,
            q_thermogenesis_skin,
        ) = threg.sum_m(
            q_bmr_local,
            q_work,
            q_shiv,
            q_nst,
        )
        q_thermogenesis_total = (
            q_thermogenesis_core.sum()
            + q_thermogenesis_muscle.sum()
            + q_thermogenesis_fat.sum()
            + q_thermogenesis_skin.sum()
        )

        # ------------------------------------------------------------------
        # Others
        # ------------------------------------------------------------------
        # Calculate blood flow in core, muscle, fat [L/h]
        bf_core, bf_muscle, bf_fat = threg.cr_ms_fat_blood_flow(
            q_work,
            q_shiv,
            self._height,
            self._weight,
            self._bsa_equation,
            self._age,
            self._ci,
        )

        # Calculate heat loss by respiratory
        p_a = threg.antoine(self._ta) * self._rh / 100
        res_sh, res_lh = threg.resp_heat_loss(
            self._ta[0], p_a[0], q_thermogenesis_total
        )

        # Calculate sensible heat loss [W]
        shl_sk = (tsk - to) / r_t * self._bsa

        # Calculate cardiac output [L/h]
        co = threg.sum_bf(bf_core, bf_muscle, bf_fat, bf_skin, bf_ava_hand, bf_ava_foot)

        # Calculate weight loss rate by evaporation [g/sec]
        wlesk = (e_sweat + 0.06 * e_max) / 2418
        wleres = res_lh / 2418

        # ------------------------------------------------------------------
        # Matrix
        # This code section is focused on constructing and calculating
        # various matrices required for modeling the thermoregulation
        # of the human body.
        # Since JOS-3 has 85 thermal nodes, the determinant of 85*85 is to be solved.
        # ------------------------------------------------------------------

        # Matrix A = Matrix for heat exchange due to blood flow and conduction occurring between tissues
        # (85, 85,) ndarray

        # Calculates the blood flow in arteries and veins for core, muscle, fat, skin,
        # and arteriovenous anastomoses (AVA) in hands and feet,
        # and combines them into two arrays:
        # 1) bf_local for the local blood flow and 2) bf_whole for the whole-body blood flow.
        # These arrays are then combined to form arr_bf.
        bf_art, bf_vein = matrix.vessel_blood_flow(
            bf_core, bf_muscle, bf_fat, bf_skin, bf_ava_hand, bf_ava_foot
        )
        bf_local = matrix.local_arr(
            bf_core, bf_muscle, bf_fat, bf_skin, bf_ava_hand, bf_ava_foot
        )
        bf_whole = matrix.whole_body(bf_art, bf_vein, bf_ava_hand, bf_ava_foot)
        arr_bf = np.zeros((NUM_NODES, NUM_NODES))
        arr_bf += bf_local
        arr_bf += bf_whole

        # Adjusts the units of arr_bf from [W/K] to [/sec] and then to [-]
        # by dividing by the heat capacity self._cap and multiplying by the time step dtime.
        arr_bf /= self._cap.reshape((NUM_NODES, 1))  # Change unit [W/K] to [/sec]
        arr_bf *= dtime  # Change unit [/sec] to [-]

        # Performs similar unit conversions for the convective heat transfer coefficient array arr_cdt
        # (also divided by self._cap and multiplied by dtime).
        arr_cdt = self._cdt.copy()
        arr_cdt /= self._cap.reshape((NUM_NODES, 1))  # Change unit [W/K] to [/sec]
        arr_cdt *= dtime  # Change unit [/sec] to [-]

        # Matrix B = Matrix for heat transfer between skin and environment
        arr_b = np.zeros(NUM_NODES)
        arr_b[INDEX["skin"]] += 1 / r_t * self._bsa
        arr_b /= self._cap  # Change unit [W/K] to [/sec]
        arr_b *= dtime  # Change unit [/sec] to [-]

        # Calculates the off-diagonal and diagonal elements of the matrix A,
        # which represents the heat transfer coefficients between different parts of the body,
        # and combines them to form the full matrix A (arrA).
        # Then, the inverse of matrix A is computed (arrA_inv).
        arr_a_tria = -(arr_cdt + arr_bf)

        arr_a_dia = arr_cdt + arr_bf
        arr_a_dia = arr_a_dia.sum(axis=1) + arr_b
        arr_a_dia = np.diag(arr_a_dia)
        arr_a_dia += np.eye(NUM_NODES)

        arr_a = arr_a_tria + arr_a_dia
        arr_a_inv = np.linalg.inv(arr_a)

        # Matrix Q = Matrix for heat generation rate from thermogenesis, respiratory, sweating,
        # and extra heat gain processes in different body parts.

        # Matrix Q [W] / [J/K] * [sec] = [-]
        # Thermogensis
        arr_q = np.zeros(NUM_NODES)
        arr_q[INDEX["core"]] += q_thermogenesis_core
        arr_q[INDEX["muscle"]] += q_thermogenesis_muscle[VINDEX["muscle"]]
        arr_q[INDEX["fat"]] += q_thermogenesis_fat[VINDEX["fat"]]
        arr_q[INDEX["skin"]] += q_thermogenesis_skin

        # Respiratory [W]
        arr_q[INDEX["core"][2]] -= res_sh + res_lh  # chest core

        # Sweating [W]
        arr_q[INDEX["skin"]] -= e_sk

        # Extra heat gain [W]
        arr_q += self.ex_q.copy()

        arr_q /= self._cap  # Change unit [W]/[J/K] to [K/sec]
        arr_q *= dtime  # Change unit [K/sec] to [K]

        # Boundary batrix [°C]
        arr_to = np.zeros(NUM_NODES)
        arr_to[INDEX["skin"]] += to

        # Combines the current body temperature, the boundary matrix, and the heat generation matrix
        # to calculate the new body temperature distribution (arr).
        arr = self._bodytemp + arr_b * arr_to + arr_q

        # ------------------------------------------------------------------
        # New body temp. [°C]
        # ------------------------------------------------------------------
        self._bodytemp = np.dot(arr_a_inv, arr)

        # ------------------------------------------------------------------
        # Output parameters
        # ------------------------------------------------------------------
        dict_out = {}
        if output:  # Default output
            dict_out["pythermalcomfort_version"] = self._version
            dict_out["cycle_time"] = self._cycle
            dict_out["simulation_time"] = self._t
            dict_out["dt"] = dtime
            dict_out["t_skin_mean"] = self.t_skin_mean
            dict_out["t_skin"] = self.t_skin
            dict_out["t_core"] = self.t_core
            dict_out["w_mean"] = np.average(wet, weights=Default.local_bsa)
            dict_out["w"] = wet
            dict_out["weight_loss_by_evap_and_res"] = wlesk.sum() + wleres
            dict_out["cardiac_output"] = co
            dict_out["q_thermogenesis_total"] = q_thermogenesis_total
            dict_out["q_res"] = res_sh + res_lh
            dict_out["q_skin2env"] = shl_sk + e_sk

        detail_out = {}
        if self._ex_output and output:
            detail_out["name"] = self.model_name
            detail_out["height"] = self._height
            detail_out["weight"] = self._weight
            detail_out["bsa"] = self._bsa
            detail_out["fat"] = self._fat
            detail_out["sex"] = self._sex
            detail_out["age"] = self._age
            detail_out["t_core_set"] = setpt_cr
            detail_out["t_skin_set"] = setpt_sk
            detail_out["t_cb"] = self.t_cb
            detail_out["t_artery"] = self.t_artery
            detail_out["t_vein"] = self.t_vein
            detail_out["t_superficial_vein"] = self.t_superficial_vein
            detail_out["t_muscle"] = self.t_muscle
            detail_out["t_fat"] = self.t_fat
            detail_out["to"] = to
            detail_out["r_t"] = r_t
            detail_out["r_et"] = r_et
            detail_out["tdb"] = self._ta.copy()
            detail_out["tr"] = self._tr.copy()
            detail_out["rh"] = self._rh.copy()
            detail_out["v"] = self._va.copy()
            detail_out["par"] = self._par
            detail_out["clo"] = self._clo.copy()
            detail_out["e_skin"] = e_sk
            detail_out["e_max"] = e_max
            detail_out["e_sweat"] = e_sweat
            detail_out["bf_core"] = bf_core
            detail_out["bf_muscle"] = bf_muscle[VINDEX["muscle"]]
            detail_out["bf_fat"] = bf_fat[VINDEX["fat"]]
            detail_out["bf_skin"] = bf_skin
            detail_out["bf_ava_hand"] = bf_ava_hand
            detail_out["bf_ava_foot"] = bf_ava_foot
            detail_out["q_bmr_core"] = q_bmr_local[0]
            detail_out["q_bmr_muscle"] = q_bmr_local[1][VINDEX["muscle"]]
            detail_out["q_bmr_fat"] = q_bmr_local[2][VINDEX["fat"]]
            detail_out["q_bmr_skin"] = q_bmr_local[3]
            detail_out["q_work"] = q_work
            detail_out["q_shiv"] = q_shiv
            detail_out["q_nst"] = q_nst
            detail_out["q_thermogenesis_core"] = q_thermogenesis_core
            detail_out["q_thermogenesis_muscle"] = q_thermogenesis_muscle[
                VINDEX["muscle"]
            ]
            detail_out["q_thermogenesis_fat"] = q_thermogenesis_fat[VINDEX["fat"]]
            detail_out["q_thermogenesis_skin"] = q_thermogenesis_skin
            dict_out["q_skin2env_sensible"] = shl_sk
            dict_out["q_skin2env_latent"] = e_sk
            dict_out["q_res_sensible"] = res_sh
            dict_out["q_res_latent"] = res_lh

        if self._ex_output == "all":
            dict_out.update(detail_out)
        elif isinstance(self._ex_output, list):  # if ex_out type is list
            out_keys = detail_out.keys()
            for key in self._ex_output:
                if key in out_keys:
                    dict_out[key] = detail_out[key]
        return dict_out

    def dict_results(self):
        """Get results as a dictionary with pandas.DataFrame values.

        Returns
        -------
        dict
            A dictionary of the results, with keys as column names and values as pandas.DataFrame objects.
        """
        if not self._history:
            print("The model has no data.")
            return None

        def check_word_contain(word, *args):
            """Check if word contains *args."""
            bool_filter = False
            for arg in args:
                if arg in word:
                    bool_filter = True
            return bool_filter

        # Set column titles
        # If the values are iter, add the body names as suffix words.
        # If the values are not iter and the single value data, convert it to iter.
        key2keys = {}  # Column keys
        for key, value in self._history[0].items():
            try:
                length = len(value)
                if isinstance(value, str):
                    keys = [key]  # str is iter. Convert to list without suffix
                elif check_word_contain(key, "sve", "sfv", "superficialvein"):
                    keys = [key + "_" + BODY_NAMES[i] for i in VINDEX["sfvein"]]
                elif check_word_contain(key, "ms", "muscle"):
                    keys = [key + "_" + BODY_NAMES[i] for i in VINDEX["muscle"]]
                elif check_word_contain(key, "fat"):
                    keys = [key + "_" + BODY_NAMES[i] for i in VINDEX["fat"]]
                elif length == 17:  # if data contains 17 values
                    keys = [key + "_" + bn for bn in BODY_NAMES]
                else:
                    keys = [key + "_" + BODY_NAMES[i] for i in range(length)]
            except TypeError:  # if the value is not iter.
                keys = [key]  # convert to iter
            key2keys.update({key: keys})

        data = []
        for i, dictout in enumerate(self._history):
            row = {}
            for key, value in dictout.items():
                keys = key2keys[key]
                if len(keys) == 1:
                    values = [value]  # make list if value is not iter
                else:
                    values = value
                row.update(dict(zip(keys, values)))
            data.append(row)

        out_dict = dict(zip(data[0].keys(), [[] for _ in range(len(data[0].keys()))]))
        for row in data:
            for k in data[0].keys():
                out_dict[k].append(row[k])
        return out_dict

    def to_csv(
        self,
        path: str = None,
        folder: str = None,
        unit: bool = True,
        meaning: bool = True,
    ) -> None:
        """Export results as csv format.

        Parameters
        ----------
        path : str, optional
            Output path. If you don't use the default file name, set a name.
            The default is None.
        folder : str, optional
            Output folder. If you use the default file name with the current time,
            set a only folder path.
            The default is None.
        unit : bool, optional
            Write units in csv file. The default is True.
        meaning : bool, optional
            Write meanings of the parameters in csv file. The default is True.

        Returns
        -------
        None

        Examples
        ----------
        >>> from pythermalcomfort.models import JOS3
        >>> model = JOS3()
        >>> model.simulate(60)
        >>> model.to_csv()
        """

        # Use the model name and current time as default output file name
        if path is None:
            now_time = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
            path = "{}_{}.csv".format(self.model_name, now_time)
            if folder:
                os.makedirs(folder, exist_ok=True)
                path = folder + os.sep + path
        elif not ((path[-4:] == ".csv") or (path[-4:] == ".txt")):
            path += ".csv"

        # Get simulation results as a dictionary
        dict_out = self.dict_results()

        # Get column names, units and meanings
        columns = [k for k in dict_out.keys()]
        units = []
        meanings = []
        for col in columns:
            param, body_name = remove_body_name(col)
            if param in ALL_OUT_PARAMS:
                u = ALL_OUT_PARAMS[param]["unit"]
                units.append(u)

                m = ALL_OUT_PARAMS[param]["meaning"]
                if body_name:
                    # Replace underscores with spaces
                    body_name_with_spaces = body_name.replace("_", " ")
                    meanings.append(m.replace("each body part", body_name_with_spaces))
                else:
                    meanings.append(m)
            else:
                units.append("")
                meanings.append("")

        # Write to csv file
        with open(path, "wt", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(list(columns))
            if unit:
                writer.writerow(units)
            if meaning:
                writer.writerow(meanings)
            for i in range(len(dict_out["cycle_time"])):
                row = []
                for k in columns:
                    row.append(dict_out[k][i])
                writer.writerow(row)

    def _set_ex_q(self, tissue, value):
        """Set extra heat gain by tissue name.

        Parameters
        ----------
        tissue : str
            Tissue name. "core", "skin", or "artery".... If you set value to
            head muscle and other segment's core, set "all_muscle".
        value : int, float, array
            Heat gain [W]

        Returns
        -------
        array
            Extra heat gain of model.
        """
        self.ex_q[INDEX[tissue]] = value
        return self.ex_q

    @property
    def tdb(self):
        """Dry-bulb air temperature. The setter accepts int, float, dict, list,
        ndarray. The inputs are used to create a 17-element array. dict should
        be passed with BODY_NAMES as keys.

        Returns
        -------
        ndarray
            A NumPy array of shape (17,).
        """
        return self._ta

    @tdb.setter
    def tdb(self, inp):
        self._ta = _to17array(inp)

    @property
    def tr(self):
        """tr : numpy.ndarray (17,) Mean radiant temperature [°C]."""
        return self._tr

    @tr.setter
    def tr(self, inp):
        self._tr = _to17array(inp)

    @property
    def to(self):
        """to : numpy.ndarray (17,) Operative temperature [°C]."""
        hc = threg.fixed_hc(
            threg.conv_coef(
                self._posture,
                self._va,
                self._ta,
                self.t_skin,
            ),
            self._va,
        )
        hr = threg.fixed_hr(
            threg.rad_coef(
                self._posture,
            )
        )
        to = threg.operative_temp(
            self._ta,
            self._tr,
            hc,
            hr,
        )
        return to

    @to.setter
    def to(self, inp):
        self._ta = _to17array(inp)
        self._tr = _to17array(inp)

    @property
    def rh(self):
        """rh : numpy.ndarray (17,) Relative humidity [%]."""
        return self._rh

    @rh.setter
    def rh(self, inp):
        self._rh = _to17array(inp)

    @property
    def v(self):
        """v : numpy.ndarray (17,) Air velocity [m/s]."""
        return self._va

    @v.setter
    def v(self, inp):
        self._va = _to17array(inp)

    @property
    def posture(self):
        """posture : str Current JOS3 posture."""
        return self._posture

    @posture.setter
    def posture(self, inp):
        if inp == 0:
            self._posture = "standing"
        elif inp == 1:
            self._posture = "sitting"
        elif inp == 2:
            self._posture = "lying"
        elif type(inp) == str:
            if inp.lower() == "standing":
                self._posture = "standing"
            elif inp.lower() in ["sitting", "sedentary"]:
                self._posture = "sitting"
            elif inp.lower() in ["lying", "supine"]:
                self._posture = "lying"
        else:
            self._posture = "standing"
            print('posture must be 0="standing", 1="sitting" or 2="lying".')
            print('posture was set "standing".')

    @property
    def clo(self):
        """clo : numpy.ndarray (17,) Clothing insulation [clo]."""
        return self._clo

    @clo.setter
    def clo(self, inp):
        self._clo = _to17array(inp)

    @property
    def par(self):
        """par : float Physical activity ratio [-].This equals the ratio of metabolic rate to basal metabolic rate. par of sitting quietly is 1.2."""
        return self._par

    @par.setter
    def par(self, inp):
        self._par = inp

    @property
    def body_temp(self):
        """body_temp : numpy.ndarray (85,) All segment temperatures of JOS-3"""
        return self._bodytemp

    @body_temp.setter
    def body_temp(self, inp):
        self._bodytemp = inp.copy()

    @property
    def bsa(self):
        """bsa : numpy.ndarray (17,) Body surface areas by local body segments [m2]."""
        return self._bsa.copy()

    @property
    def r_t(self):
        """r_t : numpy.ndarray (17,) Dry heat resistances between the skin and ambience areas by local body segments [(m2*K)/W]."""
        hc = threg.fixed_hc(
            threg.conv_coef(
                self._posture,
                self._va,
                self._ta,
                self.t_skin,
            ),
            self._va,
        )
        hr = threg.fixed_hr(
            threg.rad_coef(
                self._posture,
            )
        )
        return threg.dry_r(hc, hr, self._clo)

    @property
    def r_et(self):
        """r_et : numpy.ndarray (17,) w (Evaporative) heat resistances between the skin and ambience areas by local body segments [(m2*kPa)/W]."""
        hc = threg.fixed_hc(
            threg.conv_coef(
                self._posture,
                self._va,
                self._ta,
                self.t_skin,
            ),
            self._va,
        )
        return threg.wet_r(hc, self._clo, self._iclo)

    @property
    def w(self):
        """w : numpy.ndarray (17,) Skin wettedness on local body segments [-]."""
        err_cr = self.t_core - self.setpt_cr
        err_sk = self.t_skin - self.setpt_sk
        wet, *_ = threg.evaporation(
            err_cr, err_sk, self._ta, self._rh, self.r_et, self._bsa_rate, self._age
        )
        return wet

    @property
    def w_mean(self):
        """w_mean : float Mean skin wettedness of the whole body [-]."""
        wet = self.w
        return np.average(wet, weights=Default.local_bsa)

    @property
    def t_skin_mean(self):
        """t_skin_mean : float Mean skin temperature of the whole body [°C]."""
        return np.average(self._bodytemp[INDEX["skin"]], weights=Default.local_bsa)

    @property
    def t_skin(self):
        """t_skin : numpy.ndarray (17,) Skin temperatures by the local body segments [°C]."""
        return self._bodytemp[INDEX["skin"]].copy()

    @t_skin.setter
    def t_skin(self, inp):
        self._bodytemp[INDEX["skin"]] = _to17array(inp)

    @property
    def t_core(self):
        """t_core : numpy.ndarray (17,) Skin temperatures by the local body segments [°C]."""
        return self._bodytemp[INDEX["core"]].copy()

    @property
    def t_cb(self):
        """t_cb : numpy.ndarray (1,) Temperature at central blood pool [°C]."""
        return self._bodytemp[0].copy()

    @property
    def t_artery(self):
        """t_artery : numpy.ndarray (17,) Arterial temperatures by the local body segments [°C]."""
        return self._bodytemp[INDEX["artery"]].copy()

    @property
    def t_vein(self):
        """t_vein : numpy.ndarray (17,) Vein temperatures by the local body segments [°C]."""
        return self._bodytemp[INDEX["vein"]].copy()

    @property
    def t_superficial_vein(self):
        """t_superficial_vein : numpy.ndarray (12,) Superficial vein temperatures by the local body segments [°C]."""
        return self._bodytemp[INDEX["sfvein"]].copy()

    @property
    def t_muscle(self):
        """t_muscle : numpy.ndarray (2,) Muscle temperatures of head and pelvis [°C]."""
        return self._bodytemp[INDEX["muscle"]].copy()

    @property
    def t_fat(self):
        """t_fat : numpy.ndarray (2,) fat temperatures of head and pelvis  [°C]."""
        return self._bodytemp[INDEX["fat"]].copy()

    @property
    def body_names(self):
        """body_names : list JOS3 body names"""
        return BODY_NAMES

    @property
    def results(self):
        """Results of the model: dict."""
        return self.dict_results()

    @property
    def bmr(self):
        """bmr : float Basal metabolic rate [W/m2]."""
        tcr = threg.basal_met(
            self._height,
            self._weight,
            self._age,
            self._sex,
            self._bmr_equation,
        )
        return tcr / self.bsa.sum()

    @property
    def version(self):
        """version : float The current version of pythermalcomfort."""
        return self._version
