import inout.readconfig as rc
import pytest
import force_modules.hull_hydro as hull_hydro
import inout.messages as msg
import os
import numpy.testing as npt
from utils import units

@pytest.fixture
def setup_env():
    '--------- Setup --------'
    # changing the directory for file
    rc.unique_id = {}
    root_dir = os.getcwd()
    os.chdir('./tests/CalmWaterResistanceFromFile')
    yield
    '--------- teardown ---------'
    os.chdir(root_dir)

#@pytest.mark.force
def test_force(setup_env, capfd):
    out, err = capfd.readouterr()
    config_dict = {'filename': ['hull_resistance.dat', {}],
                    'STW_ms': [units.convertSI(15.0,'kn'), {}]}
    req_ship_entries = {}
    req_env_entries = {}
   
    force_module = hull_hydro.CalmWaterResistanceFromFile(
            "CWR1", config_dict, req_ship_entries, req_env_entries)
    
    config={}
    ship={
        'Lpp_m' : 100,
        'T_m'   : 10,
    }
    env={}
    fm={}
    F, M = force_module.calc(config, ship, env, fm)
    npt.assert_array_almost_equal(F[0], -545000, decimal=1)



#@pytest.mark.moment
def test_moment(setup_env, capfd):
    out, err = capfd.readouterr()
    config_dict = {'filename': ['hull_resistance.dat', {}],
                   'STW_ms': [units.convertSI(15.0, 'kn'), {}]}
    req_ship_entries = {}
    req_env_entries = {}

    force_module = hull_hydro.CalmWaterResistanceFromFile(
        "CWR1", config_dict, req_ship_entries, req_env_entries)

    config = {}
    ship = {
        'Lpp_m': 100,
        'T_m': 10,
    }
    env = {}
    fm = {}
    F, M = force_module.calc(config, ship, env, fm)
    npt.assert_array_almost_equal(M[1], -2725000.0, decimal=1)


