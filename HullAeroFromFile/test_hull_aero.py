import pytest
import force_modules.hull_aero as hull_aero
import inout.messages as msg
import inout.readconfig as rc


#@pytest.mark.hull_aero
def test_hull_aero(capfd):
    msg.init_errors()
    out, err = capfd.readouterr()
    config_dict = {'filename': ['hull_aero.dat', {}],
                   'beta_deg': [None, {'state_id': 'beta'}], 'phi_deg': [None, {'state_id': 'phi'}], 'STW_ms': [None, {'state_id': 'STW'}]}
    req_ship_entries = {}
    req_env_entries = {}
    fm = hull_aero.HullAero('Wind', config_dict,
                            req_ship_entries, req_env_entries)
    out, err = capfd.readouterr()
    assert 'rho_air_kgm3' in req_env_entries.keys()
    assert 'TWS_ms' in req_env_entries.keys()
    assert 'TWD_deg' in req_env_entries.keys()
    assert fm.state_variables == {'beta': 'beta', 'STW': 'STW'}
