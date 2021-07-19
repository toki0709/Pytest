import inout.readconfig as rc
import pytest
import force_modules.hull_hydro as hull_hydro
import inout.messages as msg
import os 

@pytest.fixture
def setup_env():
    '--------- Setup --------'
    rc.unique_ids={}
    # changing the directory for file
    root_dir=os.getcwd()
    os.chdir('./tests/CalmWaterResistanceFromFile')
    yield
    '--------- teardown ---------'
    os.chdir(root_dir)

def test_constructor_no_state_id(setup_env,capfd):
    '''
    Setup:
        Expectation:
    '''
    #os.chdir('./tests/CalmWaterResistanceFromFile')
    msg.init_errors()
    config_dict = {'filename': ['hull_resistance.dat', {}],
                   'STW_ms': ['10.0', {}]}
    req_ship_entries = {}
    req_env_entries = {}
    fm=hull_hydro.CalmWaterResistanceFromFile("CWR",config_dict,req_ship_entries,req_env_entries)
    #os.chdir('../..')
    out, err = capfd.readouterr()
    assert out == ""
    assert 'Lpp_m' in req_ship_entries.keys()
    assert 'T_m' in req_ship_entries.keys()
    assert fm.state_variables == {}
    
def test_constructor_with_state_id(setup_env,capfd):
    '''
    Setup:       
    Expectation: 
    '''
    #os.chdir('./tests/CalmWaterResistanceFromFile')
    msg.init_errors()
    config_dict = {'filename': ['hull_resistance.dat', {}],
                   'STW_ms': [None, {'state_id':'STW'}]}
    req_ship_entries = {}
    req_env_entries = {}
    fm=hull_hydro.CalmWaterResistanceFromFile("CWR",config_dict,req_ship_entries,req_env_entries)
    out, err = capfd.readouterr()
    assert out == ""
    assert 'Lpp_m' in req_ship_entries.keys()
    assert 'T_m' in req_ship_entries.keys()
    assert 'STW' in fm.state_variables.keys()
    
