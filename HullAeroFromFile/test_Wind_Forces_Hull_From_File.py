import pytest
import inout.readconfig as rc
import inout.messages as msg
import os
import force_modules.wind_forces_hull_from_file as hull_from_file
import numpy.testing as npt
from utils import units


@pytest.fixture
def setup_env():
    '--------- Setup --------'
    # changing the directory for file
    rc.unique_id = {}
    root_dir = os.getcwd()
    os.chdir('./tests/HullAeroFromFile')
    yield
    '--------- teardown ---------'
    os.chdir(root_dir)


#@pytest.mark.hull_aero_from_file
def test_WindForcesHullFromFile(setup_env, capfd):
    msg.init_errors()
    out, err = capfd.readouterr()
    config_dict = {'filename': ['hull_aero.dat', {}],
                   'beta_deg': [None, {'state_id': 'beta'}], 'phi_deg': [None, {'state_id': 'phi'}], 'STW_ms': [None, {'state_id': 'STW'}]}
    req_ship_entries = {}
    req_env_entries = {}
    fm = hull_from_file.WindForcesHullFromFile(
        'Wind', config_dict, req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()
    assert 'AL_m2' in req_ship_entries.keys()
    assert 'AF_m2' in req_ship_entries.keys()
    assert 'Loa_m' in req_ship_entries.keys()


#@pytest.mark.hull_aero_from_file_calc
def test_WindForcesHullFromFile_Calc(setup_env, capfd):
    msg.init_errors()
    tag = "STW_ms"
    type_id = 'str'
    req_ship_entries = {}
    req_env_entries = {}
    config_dict = config_dict = {'filename': ['hull_aero.dat', {}],
                                 'beta_deg': [0, {'state_id': 'beta'}], 'phi_deg': [None, {'state_id': 'phi'}], 'STW_ms': [units.convertSI(15.0, 'kn'), {}]}
    Force_module = hull_from_file.WindForcesHullFromFile('Wind', config_dict,
                                                         req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()
    config = {}
    fm = {}
    ship = {
        'Loa_m': 230.0,
        'AL_m2': 6168.0,
        'AF_m2': 1057.0,
    }
    env = {'rho_air_kgm3': 1.2255,
           'TWS_ms': 10,
           'TWD_deg': 30}
    F, M = Force_module.calc(config, ship, env, fm)
    npt.assert_array_almost_equal(F[0], -339962.4, decimal=1)
