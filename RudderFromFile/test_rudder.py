import pytest
import os
#import force_modules.forces as forces
import inout.messages as msg
import inout.readconfig as rc
import force_modules.rudders as rudder


@pytest.fixture
def setup_env():
    '''---------- Setup --------- '''
    rc.unique_id = {}
    root_dir = os.getcwd()
    os.chdir('./tests/RudderFromFile')
    yield

    '''--------- teardown ---------'''
    os.chdir(root_dir)


#@pytest.mark.rudder
def test_rudder_from_file(setup_env, capfd):
    msg.init_errors()
    tag = "STW_ms"
    type_id = 'str'
    req_ship_entries = {}
    req_env_entries = {}
    config_dict = {'filename': ['rudder_lift_and_drag.dat', {}],
                   'location_m': ['0.000 5.200 2.70', {}], 'rotAxis': ['0 0 1', {}], 'neutralAxis': ['1 0 0', {}], 'area_m2': ['22.416', {}], 'rudder_height_m': ['6', {}], 'Propeller': ['ThrPS', {}], 'delta_offset_deg': ['0', {}], 'delta_deg': ['0.0', {'state_id': 'delta'}], 'beta_deg': [None, {'state_id': 'beta'}], 'STW_ms': [None, {'state_id': 'STW'}], 'propeller': ['ThrPS', {}]}
    fm = rudder.RudderFromFile('RudderPS', config_dict,
                               req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()
    assert 'rho_sea_kgm3' in req_env_entries.keys()
    #assert 'STW_ms' in fm.state_variables.keys()
    assert fm.state_variables == {
        'STW': 'stw', 'beta': 'beta', 'delta': 'delta'}
