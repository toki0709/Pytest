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
    yield
    '--------- teardown ---------'

#@pytest.mark.drift
def test_constructor_no_state_id(setup_env,capfd):
    '''
        Setup: To test req_ship_entries and req_env_entries dictionary
        Expectation: To find if lpp_m, B_m, T_m, CB, rho_sea_kgm3 are in req_ship_entries and req_env_entries dictionary
    '''

    msg.init_errors()
    config_dict = {'STW_ms': ['1.0', {}], 'beta_deg': ['2.0', {}]}
    req_ship_entries = {}
    req_env_entries = {}
    fm = hull_hydro.DriftForceFromEqn(
        "Drift", config_dict, req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()

    # assert out == ""
    assert 'rho_sea_kgm3' in req_env_entries.keys()
    assert 'Lpp_m' in req_ship_entries.keys()
    assert 'B_m' in req_ship_entries.keys()
    assert 'T_m' in req_ship_entries.keys()
    assert 'CB' in req_ship_entries.keys()

    assert fm.state_variables == {}


#@pytest.mark.drift
def test_constructor_with_state_id(setup_env,capfd):
    '''
        Setup: To test the function with state_id
        Expectation: To find if lpp_m, B_m, T_m, CB, rho_sea_kgm3 are in req_ship_entries and req_env_entries dictionary
    '''
    msg.init_errors()
    config_dict = {'STW_ms': [None, {'state_id': 'STW'}],
                   'beta_deg': [None, {'state_id': 'beta'}]}

    req_ship_entries = {}
    req_env_entries = {}
    fm = hull_hydro.DriftForceFromEqn(
        "Drift", config_dict, req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()

    assert out == ""
    assert 'rho_sea_kgm3' in req_env_entries.keys()
    assert 'Lpp_m' in req_ship_entries.keys()
    assert 'B_m' in req_ship_entries.keys()
    assert 'T_m' in req_ship_entries.keys()
    assert 'CB' in req_ship_entries.keys()


#@pytest.mark.drift
def test_constructor_with_same_id(setup_env,capfd):
    '''
        Setup: To test Unique ID.
        Expectation: To find the if similar Name/Id has been used before
    '''
    msg.init_errors()
    config_dict = {'STW_ms': [None, {'state_id': 'STW'}],
                   'beta_deg': [None, {'state_id': 'beta'}]}

    req_ship_entries = {}
    req_env_entries = {}
    rc.unique_ids["Drift"]="Force module"
    fm = hull_hydro.DriftForceFromEqn(
        "Drift", config_dict, req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()

    assert out == "  ERROR: Force module -  Id Drift must be unique but was used before (Force module)\n"
    assert 'rho_sea_kgm3' in req_env_entries.keys()
    assert 'Lpp_m' in req_ship_entries.keys()
    assert 'B_m' in req_ship_entries.keys()
    assert 'T_m' in req_ship_entries.keys()
    assert 'CB' in req_ship_entries.keys()



#@pytest.mark.drift
def test_constructor_with_value(setup_env,capfd):
    '''
        Setup: To test state variable when different inouts given.
        Expectation: To find the content of the fm.state_variables
    '''
    msg.init_errors()
    config_dict = {'STW_ms': ['1.2', {'state_id': 'STW'}],
                   'beta_deg': ['2.0', {'state_id': 'beta'}]}

    req_ship_entries = {}
    req_env_entries = {}
    fm = hull_hydro.DriftForceFromEqn(
        "Drift", config_dict, req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()

    #assert out == '   INFO: Drift3 - The given value will be overwritten by the state vector entry.\n'
    assert 'rho_sea_kgm3' in req_env_entries.keys()
    assert 'Lpp_m' in req_ship_entries.keys()
    assert 'B_m' in req_ship_entries.keys()
    assert 'T_m' in req_ship_entries.keys()
    assert 'CB' in req_ship_entries.keys()
    assert fm.state_variables == {'STW': 'STW', 'beta': 'beta'}

