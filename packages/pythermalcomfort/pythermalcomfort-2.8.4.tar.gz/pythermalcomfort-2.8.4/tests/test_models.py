import pytest
import numpy as np
import json
import warnings
import requests
from itertools import product

from pythermalcomfort.optimized_functions import pmv_ppd_optimized, utci_optimized
from pythermalcomfort.models import (
    solar_gain,
    pmv_ppd,
    set_tmp,
    cooling_effect,
    adaptive_ashrae,
    clo_tout,
    vertical_tmp_grad_ppd,
    utci,
    pmv,
    ankle_draft,
    phs,
    use_fans_heatwaves,
    wbgt,
    heat_index,
    humidex,
    two_nodes,
    net,
    at,
    wc,
    adaptive_en,
    pet_steady,
    discomfort_index,
    athb,
    a_pmv,
    e_pmv,
)
from pythermalcomfort.psychrometrics import (
    t_dp,
    t_wb,
    enthalpy,
    psy_ta_rh,
    p_sat,
    t_mrt,
    t_o,
)
from pythermalcomfort.utilities import (
    transpose_sharp_altitude,
    f_svv,
    clo_dynamic,
    running_mean_outdoor_temperature,
    units_converter,
    body_surface_area,
    v_relative,
)

# get file containing validation tables
url = "https://raw.githubusercontent.com/FedericoTartarini/validation-data-comfort-models/main/validation_data.json"
resp = requests.get(url)
reference_tables = json.loads(resp.text)

# fmt: off
data_test_set_ip = [  # I have commented the lines of code that don't pass the test
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 74.9},
    {'tdb': 32, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 53.7},
    {'tdb': 50, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 62.3},
    {'tdb': 59, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 66.5},
    {'tdb': 68, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 70.7},
    {'tdb': 86, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 79.6},
    {'tdb': 104, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 93.8},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 10, 'met': 1, 'clo': 0.5, 'set': 74.0},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 90, 'met': 1, 'clo': 0.5, 'set': 76.8},
    {'tdb': 77, 'tr': 77, 'v': 19.7 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 75.2},
    {'tdb': 77, 'tr': 77, 'v': 118.1 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 70.4},
    {'tdb': 77, 'tr': 77, 'v': 216.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 68.4},
    {'tdb': 77, 'tr': 77, 'v': 590.6 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 65.6},
    {'tdb': 77, 'tr': 50, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 59.6},
    {'tdb': 77, 'tr': 104, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.5, 'set': 88.9},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 0.1, 'set': 69.3},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 1, 'set': 81.0},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 2, 'set': 90.3},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 1, 'clo': 4, 'set': 99.7},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 0.8, 'clo': 0.5, 'set': 73.9},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 2, 'clo': 0.5, 'set': 78.7},
    {'tdb': 77, 'tr': 77, 'v': 29.5 / 60, 'rh': 50, 'met': 4, 'clo': 0.5, 'set': 86.8},
    ]

data_test_pmv_ip = [  # I have commented the lines of code that don't pass the test
    {'tdb': 67.3, 'rh': 86, 'vr': 20 / 60, 'met': 1.1, 'clo': 1, 'pmv': -0.5, 'ppd': 10},
    {'tdb': 75.0, 'rh': 66, 'vr': 20 / 60, 'met': 1.1, 'clo': 1, 'pmv': 0.5, 'ppd': 10},
    {'tdb': 78.2, 'rh': 15, 'vr': 20 / 60, 'met': 1.1, 'clo': 1, 'pmv': 0.5, 'ppd': 10},
    {'tdb': 70.2, 'rh': 20, 'vr': 20 / 60, 'met': 1.1, 'clo': 1, 'pmv': -0.5, 'ppd': 10},
    {'tdb': 74.5, 'rh': 67, 'vr': 20 / 60, 'met': 1.1, 'clo': .5, 'pmv': -0.5, 'ppd': 10},
    {'tdb': 80.2, 'rh': 56, 'vr': 20 / 60, 'met': 1.1, 'clo': .5, 'pmv': 0.5, 'ppd': 10},
    {'tdb': 82.2, 'rh': 13, 'vr': 20 / 60, 'met': 1.1, 'clo': .5, 'pmv': 0.5, 'ppd': 10},
    {'tdb': 76.5, 'rh': 16, 'vr': 20 / 60, 'met': 1.1, 'clo': .5, 'pmv': -0.5, 'ppd': 10},
    ]
# fmt: on


def test_pmv_ppd():
    for table in reference_tables["reference_data"]["pmv_ppd"]:
        for entry in table["data"]:
            standard = "ISO"
            if "ASHRAE" in table["source"]:
                standard = "ASHRAE"
            inputs = entry["inputs"]
            outputs = entry["outputs"]
            r = pmv_ppd(
                inputs["ta"],
                inputs["tr"],
                inputs["v"],
                inputs["rh"],
                inputs["met"],
                inputs["clo"],
                standard=standard,
            )
            # asserting with this strange code otherwise face issues with rounding fund
            assert float("%.1f" % r["pmv"]) == outputs["pmv"]
            assert np.round(r["ppd"], 1) == outputs["ppd"]

    for row in data_test_pmv_ip:
        assert (
            abs(
                round(
                    pmv_ppd(
                        row["tdb"],
                        row["tdb"],
                        row["vr"],
                        row["rh"],
                        row["met"],
                        row["clo"],
                        standard="ashrae",
                        units="ip",
                    )["pmv"],
                    1,
                )
                - row["pmv"]
            )
            < 0.011
        )
        assert (
            abs(
                round(
                    pmv_ppd(
                        row["tdb"],
                        row["tdb"],
                        row["vr"],
                        row["rh"],
                        row["met"],
                        row["clo"],
                        standard="ashrae",
                        units="ip",
                    )["ppd"],
                    1,
                )
                - row["ppd"]
            )
            < 1
        )

    assert (
        round(pmv_ppd(67.28, 67.28, 0.328084, 86, 1.1, 1, units="ip")["pmv"], 1)
    ) == -0.5

    np.testing.assert_equal(
        np.around(pmv_ppd([70, 70], 67.28, 0.328084, 86, 1.1, 1, units="ip")["pmv"], 1),
        [-0.3, -0.3],
    )

    # test airspeed limits
    np.testing.assert_equal(
        pmv_ppd(
            [26, 24, 22, 26, 24, 22],
            [26, 24, 22, 26, 24, 22],
            [0.9, 0.6, 0.3, 0.9, 0.6, 0.3],
            50,
            [1.1, 1.1, 1.1, 1.3, 1.3, 1.3],
            [0.5, 0.5, 0.5, 0.7, 0.7, 0.7],
            standard="ashrae",
            airspeed_control=False,
        )["pmv"],
        [np.nan, np.nan, np.nan, -0.14, -0.43, -0.57],
    )

    with pytest.raises(ValueError):
        pmv_ppd(25, 25, 0.1, 50, 1.1, 0.5, standard="random")

    # checking that returns np.nan when outside standard applicability limits
    np.testing.assert_equal(
        pmv_ppd(
            [31, 20, 20, 20, 20, 30],
            [20, 41, 20, 20, 20, 20],
            [0.1, 0.1, 2, 0.1, 0.1, 0.1],
            50,
            [1.1, 1.1, 1.1, 0.7, 1.1, 4.1],
            [0.5, 0.5, 0.5, 0.5, 2.1, 0.1],
            standard="iso",
        ),
        {
            "pmv": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
            "ppd": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        },
    )

    np.testing.assert_equal(
        pmv_ppd(
            [41, 20, 20, 20, 20, 39],
            [20, 41, 20, 20, 20, 39],
            [0.1, 0.1, 2.1, 0.1, 0.1, 0.1],
            50,
            [1.1, 1.1, 1.1, 0.7, 1.1, 3.9],
            [0.5, 0.5, 0.5, 0.5, 2.1, 1.9],
            standard="ashrae",
        ),
        {
            "pmv": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
            "ppd": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        },
    )

    # check results with limit_inputs disabled
    np.testing.assert_equal(
        pmv_ppd(31, 41, 2, 50, 0.7, 2.1, standard="iso", limit_inputs=False),
        {"pmv": 2.4, "ppd": 91.0},
    )

    np.testing.assert_equal(
        pmv_ppd(41, 41, 2, 50, 0.7, 2.1, standard="ashrae", limit_inputs=False),
        {"pmv": 4.48, "ppd": 100.0},
    )

    for table in reference_tables["reference_data"]["pmv_ppd"]:
        standard = "ISO"
        if "ASHRAE" in table["source"]:
            standard = "ASHRAE"
        tdb = np.array([d["inputs"]["ta"] for d in table["data"]])
        tr = np.array([d["inputs"]["tr"] for d in table["data"]])
        v = np.array([d["inputs"]["v"] for d in table["data"]])
        rh = np.array([d["inputs"]["rh"] for d in table["data"]])
        met = np.array([d["inputs"]["met"] for d in table["data"]])
        clo = np.array([d["inputs"]["clo"] for d in table["data"]])
        pmv_exp = np.array([d["outputs"]["pmv"] for d in table["data"]])
        ppd_exp = np.array([d["outputs"]["ppd"] for d in table["data"]])
        results = pmv_ppd(tdb, tr, v, rh, met, clo, standard=standard)
        pmv_r = [float("%.1f" % x) for x in results["pmv"]]

        np.testing.assert_equal(pmv_r, pmv_exp)
        np.testing.assert_equal(results["ppd"], ppd_exp)


def test_pmv_ppd_optimized():
    assert (round(pmv_ppd_optimized(25, 25, 0.3, 50, 1.5, 0.7, 0), 2)) == 0.55

    np.testing.assert_equal(
        np.around(pmv_ppd_optimized([25, 25], 25, 0.3, 50, 1.5, 0.7, 0), 2),
        [0.55, 0.55],
    )


def test_pmv():
    for table in reference_tables["reference_data"]["pmv_ppd"]:
        for entry in table["data"]:
            standard = "ISO"
            if "ASHRAE" in table["source"]:
                standard = "ASHRAE"
            inputs = entry["inputs"]
            outputs = entry["outputs"]
            r = pmv(
                inputs["ta"],
                inputs["tr"],
                inputs["v"],
                inputs["rh"],
                inputs["met"],
                inputs["clo"],
                standard=standard,
            )
            # asserting with this strange code otherwise face issues with rounding fund
            assert float("%.1f" % r) == outputs["pmv"]

    # testing array-like input
    np.testing.assert_equal(
        pmv(
            [41, 20, 20, 20, 20, 20],
            [20, 41, 20, 20, 20, 20],
            [0.1, 0.1, 2.1, 0.1, 0.1, 0.1],
            50,
            [1.1, 1.1, 1.1, 0.7, 1.1, 1.1],
            [0.5, 0.5, 0.5, 0.5, 2.1, 0.5],
            standard="ashrae",
        ),
        [np.nan, np.nan, np.nan, np.nan, np.nan, -1.81],
    )


def test_set():
    for table in reference_tables["reference_data"]["set"]:
        for entry in table["data"]:
            inputs = entry["inputs"]
            outputs = entry["outputs"]
            assert (
                set_tmp(
                    inputs["ta"],
                    inputs["tr"],
                    inputs["v"],
                    inputs["rh"],
                    inputs["met"],
                    inputs["clo"],
                    round=True,
                    limit_inputs=False,
                )
                == outputs["set"]
            )

    # testing SET equation to calculate cooling effect
    assert (set_tmp(25, 25, 1.1, 50, 2, 0.5, calculate_ce=True)) == 20.5
    assert (set_tmp(25, 25, 1.1, 50, 3, 0.5, calculate_ce=True)) == 20.9
    assert (set_tmp(25, 25, 1.1, 50, 1.5, 0.5, calculate_ce=True)) == 20.5
    assert (set_tmp(25, 25, 1.1, 50, 1.5, 0.75, calculate_ce=True)) == 23.1
    assert (set_tmp(25, 25, 1.1, 50, 1.5, 0.1, calculate_ce=True)) == 15.6
    assert (set_tmp(29, 25, 1.1, 50, 1.5, 0.5, calculate_ce=True)) == 23.3
    assert (set_tmp(27, 25, 1.1, 50, 1.5, 0.75, calculate_ce=True)) == 24.5
    assert (set_tmp(20, 25, 1.1, 50, 1.5, 0.1, calculate_ce=True)) == 11.2
    assert (set_tmp(25, 27, 1.1, 50, 1.5, 0.5, calculate_ce=True)) == 21.1
    assert (set_tmp(25, 29, 1.1, 50, 1.5, 0.5, calculate_ce=True)) == 21.7
    assert (set_tmp(25, 31, 1.1, 50, 1.5, 0.5, calculate_ce=True)) == 22.3
    assert (set_tmp(25, 27, 1.3, 50, 1.5, 0.5, calculate_ce=True)) == 20.8
    assert (set_tmp(25, 29, 1.5, 50, 1.5, 0.5, calculate_ce=True)) == 21.0
    assert (set_tmp(25, 31, 1.7, 50, 1.5, 0.5, calculate_ce=True)) == 21.3

    assert (
        set_tmp(
            tdb=77,
            tr=77,
            v=0.328,
            rh=50,
            met=1.2,
            clo=0.5,
            units="IP",
        )
    ) == 75.8

    for row in data_test_set_ip:
        assert (
            set_tmp(
                row["tdb"],
                row["tr"],
                row["v"],
                row["rh"],
                row["met"],
                row["clo"],
                units="IP",
                limit_inputs=False,
            )
            == row["set"]
        )

    # checking that returns np.nan when outside standard applicability limits
    np.testing.assert_equal(
        set_tmp(
            [41, 20, 20, 20, 20, 39],
            [20, 41, 20, 20, 20, 39],
            [0.1, 0.1, 2.1, 0.1, 0.1, 0.1],
            50,
            [1.1, 1.1, 1.1, 0.7, 1.1, 3.9],
            [0.5, 0.5, 0.5, 0.5, 2.1, 1.9],
        ),
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    )

    for table in reference_tables["reference_data"]["set"]:
        tdb = np.array([d["inputs"]["ta"] for d in table["data"]])
        tr = np.array([d["inputs"]["tr"] for d in table["data"]])
        v = np.array([d["inputs"]["v"] for d in table["data"]])
        rh = np.array([d["inputs"]["rh"] for d in table["data"]])
        met = np.array([d["inputs"]["met"] for d in table["data"]])
        clo = np.array([d["inputs"]["clo"] for d in table["data"]])
        set_exp = np.array([d["outputs"]["set"] for d in table["data"]])
        results = set_tmp(tdb, tr, v, rh, met, clo, limit_inputs=False)

        np.testing.assert_equal(set_exp, results)


def test_solar_gain():
    for table in reference_tables["reference_data"]["solar_gain"]:
        for entry in table["data"]:
            inputs = entry["inputs"]
            outputs = entry["outputs"]
            sg = solar_gain(
                inputs["alt"],
                inputs["sharp"],
                inputs["I_dir"],
                inputs["t_sol"],
                inputs["f_svv"],
                inputs["f_bes"],
                inputs["asa"],
                inputs["posture"],
            )
            assert sg["erf"] == outputs["erf"]
            assert sg["delta_mrt"] == outputs["t_rsw"]


def test_transpose_sharp_altitude():
    assert transpose_sharp_altitude(sharp=0, altitude=0) == (0, 90)
    assert transpose_sharp_altitude(sharp=0, altitude=20) == (0, 70)
    assert transpose_sharp_altitude(sharp=0, altitude=45) == (0, 45)
    assert transpose_sharp_altitude(sharp=0, altitude=60) == (0, 30)
    assert transpose_sharp_altitude(sharp=90, altitude=0) == (90, 0)
    assert transpose_sharp_altitude(sharp=90, altitude=45) == (45, 0)
    assert transpose_sharp_altitude(sharp=90, altitude=30) == (60, 0)
    assert transpose_sharp_altitude(sharp=135, altitude=60) == (22.208, 20.705)
    assert transpose_sharp_altitude(sharp=120, altitude=75) == (13.064, 7.435)
    assert transpose_sharp_altitude(sharp=150, altitude=30) == (40.893, 48.590)


def test_use_fans_heatwaves():
    # checking that returns np.nan when outside standard applicability limits
    np.testing.assert_equal(
        use_fans_heatwaves(
            tdb=[41, 60],
            tr=40,
            v=0.1,
            rh=50,
            met=1.1,
            clo=0.5,
        )["e_skin"],
        [65.2, np.nan],
    )

    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=0.7, clo=0.3, body_position="sitting"
        )["heat_strain_w"]
        == False
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=0.7, clo=0.5, body_position="sitting"
        )["q_skin"]
        == 37.6
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=0.7, clo=0.7, body_position="sitting"
        )["m_rsw"]
        == 68.6
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=1.3, clo=0.3, body_position="sitting"
        )["m_rsw"]
        == 118.5
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=1.3, clo=0.5, body_position="sitting"
        )["m_rsw"]
        == 117.3
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=1.3, clo=0.7, body_position="sitting"
        )["m_rsw"]
        == 116.4
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=2, clo=0.3, body_position="sitting"
        )["heat_strain_w"]
        == False
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=2, clo=0.5, body_position="sitting"
        )["w"]
        == 0.5
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=20, met=2, clo=0.7, body_position="sitting"
        )["t_skin"]
        == 36.2
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=40, met=0.7, clo=0.3, body_position="sitting"
        )["heat_strain_blood_flow"]
        == False
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=40, met=0.7, clo=0.5, body_position="sitting"
        )["t_core"]
        == 36.9
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=40, met=0.7, clo=0.7, body_position="sitting"
        )["m_rsw"]
        == 73.9
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=40, met=1.3, clo=0.3, body_position="sitting"
        )["m_rsw"]
        == 126.8
    )
    assert (
        use_fans_heatwaves(
            tdb=39, tr=39, v=0.2, rh=40, met=1.3, clo=0.5, body_position="sitting"
        )["e_rsw"]
        == 84.9
    )


def test_f_svv():
    assert round(f_svv(30, 10, 3.3), 2) == 0.27
    assert round(f_svv(150, 10, 3.3), 2) == 0.31
    assert round(f_svv(30, 6, 3.3), 2) == 0.20
    assert round(f_svv(150, 6, 3.3), 2) == 0.23
    assert round(f_svv(30, 10, 6), 2) == 0.17
    assert round(f_svv(150, 10, 6), 2) == 0.21
    assert round(f_svv(30, 6, 6), 2) == 0.11
    assert round(f_svv(150, 6, 6), 2) == 0.14
    assert round(f_svv(6, 9, 3.3), 2) == 0.14
    assert round(f_svv(6, 6, 3.3), 2) == 0.11
    assert round(f_svv(6, 6, 6), 2) == 0.04
    assert round(f_svv(4, 4, 3.3), 2) == 0.06
    assert round(f_svv(4, 4, 6), 2) == 0.02


def test_t_dp():
    assert t_dp(31.6, 59.6) == 22.6
    assert t_dp(29.3, 75.4) == 24.3
    assert t_dp(27.1, 66.4) == 20.2


def test_t_wb():
    assert t_wb(27.1, 66.4) == 22.4
    assert t_wb(25, 50) == 18.0


def test_enthalpy():
    assert enthalpy(25, 0.01) == 50561.25
    assert enthalpy(27.1, 0.01) == 52707.56


def test_psy_ta_rh():
    assert psy_ta_rh(25, 50, p_atm=101325) == {
        "p_sat": 3169.2,
        "p_vap": 1584.6,
        "hr": 0.009881547577511219,
        "t_wb": 18.0,
        "t_dp": 13.8,
        "h": 50259.66,
    }


def test_cooling_effect():

    t_range = np.arange(10, 40, 10)
    rh_range = np.arange(10, 75, 25)
    v_range = np.arange(0.1, 4, 1)
    all_combinations = list(product(t_range, rh_range, v_range))
    results = [
        0,
        8.19,
        10.94,
        12.54,
        0,
        8.05,
        10.77,
        12.35,
        0,
        7.91,
        10.6,
        12.16,
        0,
        5.04,
        6.62,
        7.51,
        0,
        4.84,
        6.37,
        7.24,
        0,
        4.64,
        6.12,
        6.97,
        0,
        3.64,
        4.32,
        4.69,
        0,
        3.55,
        4.25,
        4.61,
        0,
        3.4,
        4.1,
        4.46,
    ]
    for ix, comb in enumerate(all_combinations):
        pytest.approx(
            cooling_effect(
                tdb=comb[0],
                tr=comb[0],
                rh=comb[1],
                vr=comb[2],
                met=1,
                clo=0.5,
            )
            == results[ix],
            0.1,
        )

    assert (cooling_effect(tdb=25, tr=25, vr=0.05, rh=50, met=1, clo=0.6)) == 0
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=50, met=1, clo=0.6)) == 2.17
    assert (cooling_effect(tdb=27, tr=25, vr=0.5, rh=50, met=1, clo=0.6)) == 1.85
    assert (cooling_effect(tdb=29, tr=25, vr=0.5, rh=50, met=1, clo=0.6)) == 1.63
    assert (cooling_effect(tdb=31, tr=25, vr=0.5, rh=50, met=1, clo=0.6)) == 1.42
    assert (cooling_effect(tdb=25, tr=27, vr=0.5, rh=50, met=1, clo=0.6)) == 2.44
    assert (cooling_effect(tdb=25, tr=29, vr=0.5, rh=50, met=1, clo=0.6)) == 2.81
    assert (cooling_effect(tdb=25, tr=25, vr=0.2, rh=50, met=1, clo=0.6)) == 0.67
    assert (cooling_effect(tdb=25, tr=25, vr=0.8, rh=50, met=1, clo=0.6)) == 2.93
    assert (cooling_effect(tdb=25, tr=25, vr=0.0, rh=50, met=1, clo=0.6)) == 0
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=60, met=1, clo=0.6)) == 2.13
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=80, met=1, clo=0.6)) == 2.06
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=20, met=1, clo=0.6)) == 2.29
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=60, met=1.3, clo=0.6)) == 2.84
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=60, met=1.6, clo=0.6)) == 3.5
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=60, met=1, clo=0.3)) == 2.41
    assert (cooling_effect(tdb=25, tr=25, vr=0.5, rh=60, met=1, clo=1)) == 2.05

    # test what happens when the cooling effect cannot be calculated
    assert (cooling_effect(tdb=0, tr=80, vr=5, rh=60, met=3, clo=1)) == 0

    assert (
        cooling_effect(tdb=77, tr=77, vr=1.64, rh=50, met=1, clo=0.6, units="IP")
    ) == 3.95


def test_running_mean_outdoor_temperature():
    assert (running_mean_outdoor_temperature([20, 20], alpha=0.7)) == 20
    assert (running_mean_outdoor_temperature([20, 20], alpha=0.9)) == 20
    assert (running_mean_outdoor_temperature([20, 20, 20, 20], alpha=0.7)) == 20
    assert (running_mean_outdoor_temperature([20, 20, 20, 20], alpha=0.5)) == 20
    assert (
        running_mean_outdoor_temperature(
            [77, 77, 77, 77, 77, 77, 77], alpha=0.8, units="IP"
        )
    ) == 77
    assert (
        running_mean_outdoor_temperature(
            [77, 77, 77, 77, 77, 77, 77], alpha=0.8, units="ip"
        )
    ) == 77


def test_ip_units_converter():
    assert (units_converter(tdb=77, tr=77, v=3.2, from_units="ip")) == [
        25.0,
        25.0,
        0.975312404754648,
    ]
    assert (units_converter(pressure=1, area=1 / 0.09, from_units="ip")) == [
        101325,
        1.0322474090590033,
    ]

    expected_result = [25.0, 3.047]
    assert np.allclose(units_converter("ip", tdb=77, v=10), expected_result, atol=0.01)

    # Test case 2: Conversion from SI to IP for temperature and velocity
    expected_result = [68, 6.562]
    assert np.allclose(units_converter("si", tdb=20, v=2), expected_result, atol=0.01)

    # Test case 3: Conversion from IP to SI for area and pressure
    expected_result = [9.29, 1489477.5]
    assert np.allclose(
        units_converter("ip", area=100, pressure=14.7), expected_result, atol=0.01
    )

    # Test case 4: Conversion from SI to IP for area and pressure
    expected_result = [538.199, 1]
    assert np.allclose(
        units_converter("si", area=50, pressure=101325), expected_result, atol=0.01
    )


def test_p_sat():
    assert (p_sat(tdb=25)) == 3169.2
    assert (p_sat(tdb=50)) == 12349.9


def test_t_mrt():
    np.testing.assert_equal(
        t_mrt(
            tg=[53.2, 55],
            tdb=30,
            v=0.3,
            d=0.1,
            standard="ISO",
        ),
        [74.8, 77.8],
    )
    np.testing.assert_equal(
        t_mrt(
            tg=[25.42, 26.42, 26.42, 26.42],
            tdb=26.10,
            v=0.1931,
            d=[0.1, 0.1, 0.5, 0.03],
            standard="Mixed Convection",
        ),
        [24.2, 27.0, np.nan, np.nan],
    )


def test_adaptive_ashrae():
    data_test_adaptive_ashrae = (
        [  # I have commented the lines of code that don't pass the test
            {
                "tdb": 19.6,
                "tr": 19.6,
                "t_running_mean": 17,
                "v": 0.1,
                "return": {"acceptability_80": True},
            },
            {
                "tdb": 19.6,
                "tr": 19.6,
                "t_running_mean": 17,
                "v": 0.1,
                "return": {"acceptability_90": False},
            },
            {
                "tdb": 19.6,
                "tr": 19.6,
                "t_running_mean": 25,
                "v": 0.1,
                "return": {"acceptability_80": False},
            },
            {
                "tdb": 19.6,
                "tr": 19.6,
                "t_running_mean": 25,
                "v": 0.1,
                "return": {"acceptability_80": False},
            },
            {
                "tdb": 26,
                "tr": 26,
                "t_running_mean": 16,
                "v": 0.1,
                "return": {"acceptability_80": True},
            },
            {
                "tdb": 26,
                "tr": 26,
                "t_running_mean": 16,
                "v": 0.1,
                "return": {"acceptability_90": False},
            },
            {
                "tdb": 30,
                "tr": 26,
                "t_running_mean": 16,
                "v": 0.1,
                "return": {"acceptability_80": False},
            },
            {
                "tdb": 25,
                "tr": 25,
                "t_running_mean": 23,
                "v": 0.1,
                "return": {"acceptability_80": True},
            },
            {
                "tdb": 25,
                "tr": 25,
                "t_running_mean": 23,
                "v": 0.1,
                "return": {"acceptability_90": True},
            },
        ]
    )
    for row in data_test_adaptive_ashrae:
        print(row)
        assert (
            adaptive_ashrae(row["tdb"], row["tr"], row["t_running_mean"], row["v"])[
                list(row["return"].keys())[0]
            ]
        ) == row["return"][list(row["return"].keys())[0]]

    assert (adaptive_ashrae(77, 77, 68, 0.3, units="ip")["tmp_cmf"]) == 75.2

    # test limit_inputs and array input
    np.testing.assert_equal(
        adaptive_ashrae(tdb=25, tr=25, t_running_mean=[9, 10], v=0.1),
        {
            "tmp_cmf": [np.nan, 20.9],
            "tmp_cmf_80_low": [np.nan, 17.4],
            "tmp_cmf_80_up": [np.nan, 24.4],
            "tmp_cmf_90_low": [np.nan, 18.4],
            "tmp_cmf_90_up": [np.nan, 23.4],
            "acceptability_80": [False, False],
            "acceptability_90": [False, False],
        },
    )
    np.testing.assert_equal(
        adaptive_ashrae(
            tdb=[77, 74], tr=77, t_running_mean=[48, 68], v=0.3, units="ip"
        ),
        {
            "tmp_cmf": [np.nan, 75.2],
            "tmp_cmf_80_low": [np.nan, 68.9],
            "tmp_cmf_80_up": [np.nan, 81.5],
            "tmp_cmf_90_low": [np.nan, 70.7],
            "tmp_cmf_90_up": [np.nan, 79.7],
            "acceptability_80": [False, True],
            "acceptability_90": [False, True],
        },
    )


def test_adaptive_en():
    np.testing.assert_equal(
        adaptive_en(
            tdb=[25, 25, 23.5], tr=[25, 25, 23.5], t_running_mean=[9, 20, 28], v=0.1
        ),
        {
            "tmp_cmf": [np.nan, 25.4, 28.0],
            "acceptability_cat_i": [False, True, False],
            "acceptability_cat_ii": [False, True, False],
            "acceptability_cat_iii": [False, True, True],
            "tmp_cmf_cat_i_up": [np.nan, 27.4, 30.0],
            "tmp_cmf_cat_ii_up": [np.nan, 28.4, 31.0],
            "tmp_cmf_cat_iii_up": [np.nan, 29.4, 32.0],
            "tmp_cmf_cat_i_low": [np.nan, 22.4, 25.0],
            "tmp_cmf_cat_ii_low": [np.nan, 21.4, 24.0],
            "tmp_cmf_cat_iii_low": [np.nan, 20.4, 23.0],
        },
    )


def test_clo_tout():
    assert (clo_tout(tout=80.6, units="ip")) == 0.46
    np.testing.assert_equal(clo_tout(tout=[80.6, 82], units="ip"), [0.46, 0.46])
    assert (clo_tout(tout=27)) == 0.46
    np.testing.assert_equal(clo_tout(tout=[27, 24]), [0.46, 0.48])


def test_vertical_tmp_grad_ppd():
    assert (
        vertical_tmp_grad_ppd(77, 77, 0.328, 50, 1.2, 0.5, 7 / 1.8, units="ip")[
            "PPD_vg"
        ]
    ) == 13.0
    assert (
        vertical_tmp_grad_ppd(77, 77, 0.328, 50, 1.2, 0.5, 7 / 1.8, units="ip")[
            "Acceptability"
        ]
    ) == False
    assert (vertical_tmp_grad_ppd(25, 25, 0.1, 50, 1.2, 0.5, 7)["PPD_vg"]) == 12.6
    assert (vertical_tmp_grad_ppd(25, 25, 0.1, 50, 1.2, 0.5, 4)["PPD_vg"]) == 1.7
    assert (
        vertical_tmp_grad_ppd(25, 25, 0.1, 50, 1.2, 0.5, 4)["Acceptability"]
    ) == True

    with pytest.raises(ValueError):
        vertical_tmp_grad_ppd(25, 25, 0.3, 50, 1.2, 0.5, 7)


def test_ankle_draft():
    assert (ankle_draft(25, 25, 0.2, 50, 1.2, 0.5, 0.3, units="SI")["PPD_ad"]) == 18.5
    assert (
        ankle_draft(77, 77, 0.2 * 3.28, 50, 1.2, 0.5, 0.4 * 3.28, units="IP")["PPD_ad"]
    ) == 23.5

    with pytest.raises(ValueError):
        ankle_draft(25, 25, 0.3, 50, 1.2, 0.5, 7)


@pytest.fixture
def data_test_utci():
    return [  # I have commented the lines of code that don't pass the test
        {"tdb": 25, "tr": 27, "rh": 50, "v": 1, "return": {"utci": 25.2}},
        {"tdb": 19, "tr": 24, "rh": 50, "v": 1, "return": {"utci": 20.0}},
        {"tdb": 19, "tr": 14, "rh": 50, "v": 1, "return": {"utci": 16.8}},
        {"tdb": 27, "tr": 22, "rh": 50, "v": 1, "return": {"utci": 25.5}},
        {"tdb": 27, "tr": 22, "rh": 50, "v": 10, "return": {"utci": 20.0}},
        {"tdb": 27, "tr": 22, "rh": 50, "v": 16, "return": {"utci": 15.8}},
        {"tdb": 51, "tr": 22, "rh": 50, "v": 16, "return": {"utci": np.nan}},
        {"tdb": 27, "tr": 22, "rh": 50, "v": 0, "return": {"utci": np.nan}},
    ]


def test_utci(data_test_utci):
    for row in data_test_utci:
        np.testing.assert_equal(
            utci(row["tdb"], row["tr"], row["v"], row["rh"]),
            row["return"][list(row["return"].keys())[0]],
        )

    assert (utci(tdb=77, tr=77, v=3.28, rh=50, units="ip")) == 76.4

    assert (
        utci(tdb=30, tr=27, v=1, rh=50, units="si", return_stress_category=True)
    ) == {"utci": 29.6, "stress_category": "moderate heat stress"}
    assert (utci(tdb=9, tr=9, v=1, rh=50, units="si", return_stress_category=True)) == {
        "utci": 8.7,
        "stress_category": "slight cold stress",
    }


def test_utci_numpy(data_test_utci):
    tdb = np.array([d["tdb"] for d in data_test_utci])
    tr = np.array([d["tr"] for d in data_test_utci])
    rh = np.array([d["rh"] for d in data_test_utci])
    v = np.array([d["v"] for d in data_test_utci])
    expect = np.array([d["return"]["utci"] for d in data_test_utci])

    np.testing.assert_equal(utci(tdb, tr, v, rh), expect)

    tdb = np.array([25, 25])
    tr = np.array([27, 25])
    v = np.array([1, 1])
    rh = np.array([50, 50])
    expect = {
        "utci": np.array([25.2, 24.6]),
        "stress_category": np.array(["no thermal stress", "no thermal stress"]),
    }

    result = utci(tdb, tr, v, rh, units="si", return_stress_category=True)
    np.testing.assert_equal(result["utci"], expect["utci"])
    np.testing.assert_equal(result["stress_category"], expect["stress_category"])


def test_utci_optimized():
    np.testing.assert_equal(
        np.around(utci_optimized([25, 27], 1, 1, 1.5), 2), [24.73, 26.57]
    )


def test_clo_dynamic():
    assert (clo_dynamic(clo=1, met=1, standard="ASHRAE")) == 1
    assert (clo_dynamic(clo=1, met=0.5, standard="ASHRAE")) == 1
    assert (clo_dynamic(clo=2, met=0.5, standard="ASHRAE")) == 2

    # Test ASHRAE standard
    assert np.allclose(clo_dynamic(1.0, 1.0), np.array(1))
    assert np.allclose(clo_dynamic(1.0, 1.2), np.array(1))
    assert np.allclose(clo_dynamic(1.0, 2.0), np.array(0.8))

    # Test ISO standard
    assert np.allclose(clo_dynamic(1.0, 1.0, standard="ISO"), np.array(1))
    assert np.allclose(clo_dynamic(1.0, 2.0, standard="ISO"), np.array(0.8))

    # Test invalid standard input
    with pytest.raises(ValueError):
        clo_dynamic(1.0, 1.0, standard="invalid")


def test_phs():
    assert phs(tdb=40, tr=40, rh=33.85, v=0.3, met=150, clo=0.5, posture=2) == {
        "d_lim_loss_50": 440.0,
        "d_lim_loss_95": 298.0,
        "d_lim_t_re": 480.0,
        "water_loss": 6166.4,
        "t_re": 37.5,
        "t_cr": 37.5,
        "t_sk": 35.3,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.24,
        "water_loss_watt": 266.1,
    }

    assert phs(tdb=35, tr=35, rh=71, v=0.3, met=150, clo=0.5, posture=2) == {
        "d_lim_loss_50": 385.0,
        "d_lim_loss_95": 256.0,
        "d_lim_t_re": 75.0,
        "water_loss": 6934.6,
        "t_re": 39.8,
        "t_cr": 39.7,
        "t_sk": 36.4,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.1,
        "water_loss_watt": 276.9,
    }

    assert phs(tdb=30, tr=50, posture=2, rh=70.65, v=0.3, met=150, clo=0.5) == {
        "d_lim_loss_50": 380.0,
        "d_lim_loss_95": 258.0,
        "d_lim_t_re": 480.0,
        "water_loss": 7166.2,
        "t_re": 37.7,
        "t_cr": 37.7,
        "t_sk": 35.7,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.22,
        "water_loss_watt": 312.5,
    }
    assert phs(
        tdb=28, tr=58, acclimatized=0, posture=2, rh=79.31, v=0.3, met=150, clo=0.5
    ) == {
        "d_lim_loss_50": 466.0,
        "d_lim_loss_95": 314.0,
        "d_lim_t_re": 57.0,
        "water_loss": 5807.3,
        "t_re": 41.2,
        "t_cr": 41.1,
        "t_sk": 37.8,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.1,
        "water_loss_watt": 250.0,
    }
    assert phs(
        tdb=35, tr=35, acclimatized=0, posture=1, rh=53.3, v=1, met=150, clo=0.5
    ) == {
        "d_lim_loss_50": 480.0,
        "d_lim_loss_95": 463.0,
        "d_lim_t_re": 480.0,
        "water_loss": 3891.8,
        "t_re": 37.6,
        "t_cr": 37.5,
        "t_sk": 34.8,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.24,
        "water_loss_watt": 165.7,
    }
    assert phs(tdb=43, tr=43, posture=1, rh=34.7, v=0.3, met=103, clo=0.5) == {
        "d_lim_loss_50": 401.0,
        "d_lim_loss_95": 271.0,
        "d_lim_t_re": 480.0,
        "water_loss": 6765.1,
        "t_re": 37.3,
        "t_cr": 37.2,
        "t_sk": 35.3,
        "t_cr_eq": 37.0,
        "t_sk_t_cr_wg": 0.26,
        "water_loss_watt": 293.6,
    }
    assert phs(
        tdb=35, tr=35, acclimatized=0, posture=2, rh=53.3, v=0.3, met=206, clo=0.5
    ) == {
        "d_lim_loss_50": 372.0,
        "d_lim_loss_95": 247.0,
        "d_lim_t_re": 70.0,
        "water_loss": 7235.9,
        "t_re": 39.2,
        "t_cr": 39.1,
        "t_sk": 36.1,
        "t_cr_eq": 37.3,
        "t_sk_t_cr_wg": 0.1,
        "water_loss_watt": 295.7,
    }
    assert phs(
        tdb=34, tr=34, acclimatized=0, posture=2, rh=56.3, v=0.3, met=150, clo=1
    ) == {
        "d_lim_loss_50": 480.0,
        "d_lim_loss_95": 318.0,
        "d_lim_t_re": 67.0,
        "water_loss": 5547.7,
        "t_re": 41.0,
        "t_cr": 40.9,
        "t_sk": 36.7,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.1,
        "water_loss_watt": 213.9,
    }
    assert phs(tdb=40, tr=40, rh=40.63, v=0.3, met=150, clo=0.4, posture=2) == {
        "d_lim_loss_50": 407.0,
        "d_lim_loss_95": 276.0,
        "d_lim_t_re": 480.0,
        "water_loss": 6683.4,
        "t_re": 37.5,
        "t_cr": 37.4,
        "t_sk": 35.5,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.24,
        "water_loss_watt": 290.4,
    }
    assert phs(
        tdb=40,
        tr=40,
        rh=40.63,
        v=0.3,
        met=150,
        clo=0.4,
        posture=2,
        theta=90,
        walk_sp=1,
    ) == {
        "d_lim_loss_50": 480.0,
        "d_lim_loss_95": 339.0,
        "d_lim_t_re": 480.0,
        "water_loss": 5379.1,
        "t_re": 37.6,
        "t_cr": 37.5,
        "t_sk": 35.5,
        "t_cr_eq": 37.1,
        "t_sk_t_cr_wg": 0.24,
        "water_loss_watt": 231.5,
    }


def test_check_standard_compliance():
    with pytest.warns(
        UserWarning,
        match="ISO 7933:2004 air temperature applicability limits between 15 and 50 °C",
    ):
        warnings.warn(
            phs(tdb=70, tr=40, rh=33.85, v=0.3, met=150, clo=0.5, posture=2),
            UserWarning,
        )

    with pytest.warns(
        UserWarning,
        match="ISO 7933:2004 t_r - t_db applicability limits between 0 and 60 °C",
    ):
        warnings.warn(
            phs(tdb=20, tr=0, rh=33.85, v=0.3, met=150, clo=0.5, posture=2),
            UserWarning,
        )

    with pytest.warns(
        UserWarning,
        match="ISO 7933:2004 air speed applicability limits between 0 and 3 m/s",
    ):
        warnings.warn(
            phs(tdb=40, tr=40, rh=33.85, v=5, met=150, clo=0.5, posture=2),
            UserWarning,
        )

    with pytest.warns(
        UserWarning,
        match="ISO 7933:2004 met applicability limits between 100 and 450 met",
    ):
        warnings.warn(
            phs(tdb=40, tr=40, rh=33.85, v=2, met=1, clo=0.5, posture=2),
            UserWarning,
        )

    with pytest.warns(
        UserWarning,
        match="ISO 7933:2004 clo applicability limits between 0.1 and 1 clo",
    ):
        warnings.warn(
            phs(tdb=40, tr=40, rh=33.85, v=2, met=150, clo=2, posture=2),
            UserWarning,
        )

    with pytest.warns(
        UserWarning,
        match="ISO 7933:2004 rh applicability limits between 0 and",
    ):
        warnings.warn(
            phs(tdb=40, tr=40, rh=61, v=2, met=150, clo=0.5, posture=2),
            UserWarning,
        )


def test_body_surface_area():
    assert body_surface_area(weight=80, height=1.8) == 1.9917607971689137
    assert body_surface_area(70, 1.8, "dubois") == pytest.approx(1.88, rel=1e-2)
    assert body_surface_area(75, 1.75, "takahira") == pytest.approx(1.91, rel=1e-2)
    assert body_surface_area(80, 1.7, "fujimoto") == pytest.approx(1.872, rel=1e-2)
    assert body_surface_area(85, 1.65, "kurazumi") == pytest.approx(1.89, rel=1e-2)
    with pytest.raises(ValueError):
        body_surface_area(70, 1.8, "invalid_formula")


def test_t_o():
    assert t_o(25, 25, 0.1) == 25
    assert round(t_o(25, 30, 0.3), 2) == 26.83
    assert round(t_o(20, 30, 0.3), 2) == 23.66
    assert t_o(25, 25, 0.1, standard="ASHRAE") == 25
    assert t_o(20, 30, 0.1, standard="ASHRAE") == 25
    assert t_o(20, 30, 0.3, standard="ASHRAE") == 24
    assert t_o(20, 30, 0.7, standard="ASHRAE") == 23


def test_wbgt():
    assert wbgt(25, 30) == 26.5
    assert wbgt(twb=25, tg=32) == 27.1
    assert wbgt(twb=25, tg=32, tdb=20) == 27.1
    assert wbgt(twb=25, tg=32, tdb=20, with_solar_load=True) == 25.9
    with pytest.raises(ValueError):
        wbgt(twb=25, tg=32, with_solar_load=True)
    # data from Table D.1 ISO 7243
    assert wbgt(twb=17.3, tg=40, round=True) == 24.1
    assert wbgt(twb=21.1, tg=55, round=True) == 31.3
    assert wbgt(twb=16.7, tg=40, round=True) == 23.7


def test_at():
    assert at(tdb=25, rh=30, v=0.1) == 24.1
    assert at(tdb=23, rh=70, v=1) == 24.8
    assert at(tdb=23, rh=70, v=1, q=50) == 28.1


def test_heat_index():
    assert heat_index(25, 50) == 25.9
    assert heat_index(77, 50, units="IP") == 78.6
    assert heat_index(30, 80) == 37.7
    assert heat_index(86, 80, units="IP") == 99.8


def test_wc():
    assert wc(tdb=0, v=0.1) == {"wci": 518.6}
    assert wc(tdb=0, v=1.5) == {"wci": 813.5}
    assert wc(tdb=-5, v=5.5) == {"wci": 1255.2}
    assert wc(tdb=-10, v=11) == {"wci": 1631.1}
    assert wc(tdb=-5, v=11) == {"wci": 1441.4}


def test_humidex():
    assert humidex(25, 50) == {"humidex": 28.2, "discomfort": "Little or no discomfort"}
    assert humidex(30, 80) == {
        "humidex": 43.3,
        "discomfort": "Intense discomfort; avoid exertion",
    }
    assert humidex(31.6, 57.1) == {
        "humidex": 40.8,
        "discomfort": "Intense discomfort; avoid exertion",
    }


def test_net():
    assert net(37, 100, 0.1) == 37
    assert net(37, 100, 4.5) == 37
    assert net(25, 100, 4.5) == 20
    assert net(25, 100, 0.1) == 25.4
    assert net(40, 48.77, 0.1) == 33.8
    assert net(36, 50.196, 0.1) == 30.9


def test_two_nodes():
    assert two_nodes(25, 25, 1.1, 50, 2, 0.5)["disc"] == 0.4
    assert two_nodes(tdb=25, tr=25, v=0.1, rh=50, met=1.2, clo=0.5)["disc"] == 0.3
    assert two_nodes(tdb=30, tr=25, v=0.1, rh=50, met=1.2, clo=0.5)["disc"] == 1.0
    assert two_nodes(tdb=30, tr=30, v=0.1, rh=50, met=1.2, clo=0.5)["disc"] == 1.6
    assert two_nodes(tdb=28, tr=28, v=0.4, rh=50, met=1.2, clo=0.5)["disc"] == 0.8

    assert two_nodes(tdb=30, tr=25, v=0.1, rh=50, met=1.2, clo=0.5)["pmv_gagge"] == 0.9
    assert two_nodes(tdb=30, tr=30, v=0.1, rh=50, met=1.2, clo=0.5)["pmv_gagge"] == 1.5
    assert two_nodes(tdb=28, tr=28, v=0.4, rh=50, met=1.2, clo=0.5)["pmv_gagge"] == 0.8

    assert two_nodes(tdb=30, tr=25, v=0.1, rh=50, met=1.2, clo=0.5)["pmv_set"] == 1.0
    assert two_nodes(tdb=30, tr=30, v=0.1, rh=50, met=1.2, clo=0.5)["pmv_set"] == 1.4
    assert two_nodes(tdb=28, tr=28, v=0.4, rh=50, met=1.2, clo=0.5)["pmv_set"] == 0.5

    # testing limiting w_max
    assert two_nodes(40, 40, 1.1, 50, 2, 0.5, w_max=False)["t_core"] == 37.9
    assert two_nodes(40, 40, 1.1, 50, 2, 0.5, w_max=0.2)["t_core"] == 39.0

    # testing limiting max_sweating
    assert two_nodes(45, 45, 1.1, 20, 3, 0.2)["e_rsw"] == 219.3
    assert two_nodes(45, 45, 1.1, 20, 3, 0.2, max_sweating=300)["e_rsw"] == 204.0

    # testing limiting max skin blood flow
    assert two_nodes(45, 45, 1.1, 20, 3, 0.2)["t_core"] == 38.0
    assert two_nodes(45, 45, 1.1, 20, 3, 0.2, max_skin_blood_flow=60)["t_core"] == 38.2


def test_pet():
    assert pet_steady(tdb=20, tr=20, rh=50, v=0.15, met=1.37, clo=0.5) == 18.85
    assert pet_steady(tdb=30, tr=30, rh=50, v=0.15, met=1.37, clo=0.5) == 30.59
    assert pet_steady(tdb=20, tr=20, rh=50, v=0.5, met=1.37, clo=0.5) == 17.16
    assert pet_steady(tdb=21, tr=21, rh=50, v=0.1, met=1.37, clo=0.9) == 21.08
    assert pet_steady(tdb=20, tr=20, rh=50, v=0.1, met=1.37, clo=0.9) == 19.92
    assert pet_steady(tdb=-5, tr=40, rh=2, v=0.5, met=1.37, clo=0.9) == 7.82
    assert pet_steady(tdb=-5, tr=-5, rh=50, v=5.0, met=1.37, clo=0.9) == -13.38
    assert pet_steady(tdb=30, tr=60, rh=80, v=1.0, met=1.37, clo=0.9) == 43.05
    assert pet_steady(tdb=30, tr=30, rh=80, v=1.0, met=1.37, clo=0.9) == 31.69


def test_di():
    np.testing.assert_equal(
        discomfort_index([21, 23.5, 29, 32, 35, 40], 50),
        {
            "di": [19.2, 21.0, 25.0, 27.2, 29.4, 33.0],
            "discomfort_condition": [
                "No discomfort",
                "Less than 50% feels discomfort",
                "More than 50% feels discomfort",
                "Most of the population feels discomfort",
                "Everyone feels severe stress",
                "State of medical emergency",
            ],
        },
    )
    np.testing.assert_equal(
        discomfort_index([35, 35], [10, 90]),
        {
            "di": [24.9, 33.9],
            "discomfort_condition": [
                "More than 50% feels discomfort",
                "State of medical emergency",
            ],
        },
    )


def test_athb():
    np.testing.assert_equal(
        athb(
            tdb=[25, 25, 15, 25],
            tr=[25, 35, 25, 25],
            vr=[0.1, 0.1, 0.2, 0.1],
            rh=[50, 50, 50, 60],
            met=[1.1, 1.5, 1.2, 2],
            t_running_mean=[20, 20, 20, 20],
        ),
        [0.17, 0.912, -0.755, 0.38],
    )


def test_a_pmv():
    np.testing.assert_equal(
        a_pmv([24, 30], 30, vr=0.22, rh=50, met=1.4, clo=0.5, a_coefficient=0.293),
        [0.48, 1.09],
    )


def test_e_pmv():
    np.testing.assert_equal(
        e_pmv([24, 30], 30, vr=0.22, rh=50, met=1.4, clo=0.5, e_coefficient=0.6),
        [0.29, 0.91],
    )


def test_v_relative():
    # Test case when met is equal to or lower than 1
    v = 2.0
    met = 1.0
    expected_result = v
    assert np.allclose(v_relative(v, met), expected_result)

    # Test case when met is greater than 1
    v = np.array([1.0, 2.0, 3.0])
    met = 2.0
    expected_result = np.array([1.3, 2.3, 3.3])
    assert np.allclose(v_relative(v, met), expected_result, atol=1e-6)

    # Test case with negative values for v
    v = -1.5
    met = 1.5
    expected_result = -1.5 + 0.3 * 0.5
    assert np.allclose(v_relative(v, met), expected_result, atol=1e-6)
