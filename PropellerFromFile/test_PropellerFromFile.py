import pytest
import os
#import force_modules.forces as forces
import inout.messages as msg
import inout.readconfig as rc
import force_modules.propellers as propellers


@pytest.fixture
def setup_env():
    '''---------- Setup --------- '''
    rc.unique_id = {}
    root_dir = os.getcwd()
    os.chdir('./tests/PropellerFromFile')
    yield

    '''--------- teardown ---------'''
    os.chdir(root_dir)


#@pytest.mark.propeller
def test_propeller_from_file(setup_env, capfd):
    msg.init_errors()
    tag = "STW_ms"
    type_id = 'str'
    req_ship_entries = {}
    req_env_entries = {}
    config_dict = {'location_m': ['4.000 5.200 0.00', {}],
                   'diameter_m': ['5.1', {'const': 'PSDia'}],
                   'interaction_file': ['hull_interaction.dat', {}],
                   'pot_file': ['pot_8675.dat', {}],
                   'rpm': [None, {'state_id': 'rpm'}],
                   'STW_ms': [None, {'state_id': 'STW'}]}
    fm = propellers.PropellerFromFile('ThrPS', config_dict,
                                      req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()
    assert 'rho_sea_kgm3' in req_env_entries.keys()
    assert fm.state_variables == {
        'STW': 'stw', 'rpm': 'rpm'}


