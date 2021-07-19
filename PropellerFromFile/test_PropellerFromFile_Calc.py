import pytest
import os
import inout.messages as msg
import inout.readconfig as rc
import force_modules.propellers as propellers
import numpy.testing as npt
from utils import units

@pytest.fixture
def setup_env():
    '''---------- Setup --------- '''
    rc.unique_id = {}
    root_dir = os.getcwd()
    os.chdir('./tests/PropellerFromFile')
    yield

    '''--------- teardown ---------'''
    os.chdir(root_dir)


#@pytest.mark.propeller_calc
def test_propeller_from_file_Calc(setup_env, capfd):
    msg.init_errors()
    tag = "STW_ms"
    type_id = 'str'
    req_ship_entries = {}
    req_env_entries = {}
    config_dict = {'location_m': ['4.000 5.200 0.00', {}],
                   'diameter_m': ['5.1', {'const': 'PSDia'}],
                   'interaction_file': ['hull_interaction.dat', {}],
                   'pot_file': ['pot_8675.dat', {}],
                   'rpm': [units.convertSI(100.0, 'rpm'), {}],
                   'STW_ms': [units.convertSI(15.0, 'kn'), {}]}
    Force_module = propellers.PropellerFromFile('ThrPS', config_dict,
                                                req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()
    config = {}
    fm = {}
    ship = {
        'T': 0.0,
        't': 0.106 ,  }
    env = {'rho_sea_kgm3': 1025}
    F, M = Force_module.calc(config, ship, env, fm)
    npt.assert_array_almost_equal(F[0], -1843.6, decimal=1)
    #assert out == F[0]