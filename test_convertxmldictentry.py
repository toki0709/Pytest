import pytest
from inout.readconfig import convertXMLDictEntry 
import inout.messages as msg
import numpy as np


def test_correct_float1(capfd):
    '''
    Setup:       Correct value string
    Expectation: Correctly converted value, no message
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['3.2', {}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == 3.2

def test_correct_float2(capfd):
    '''
    Setup:       Correct value string
    Expectation: Correctly converted value, no message
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['-3.2', {}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == -3.2
    
def test_correct_float3(capfd):
    '''
    Setup:       Correct value string
    Expectation: Correctly converted value, no message
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['3.2e-2', {}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == 3.2e-2
    
def test_correct_float4(capfd):
    '''
    Setup:       Correct value plus a state_id coupling
    Expectation: INFO message that the given value will be ignored 
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['3.2e-2', {'state_id':'STW'}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == "   INFO: CWR - The given value will be overwritten by the state vector entry.\n"
    assert result == 0.0
    
def test_incorrect_float1(capfd):
    '''
    Setup:       Incorrect value which can not be converted, no state_id
    Expectation: ERROR message
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['3.2o-2', {}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == "  ERROR: CWR - Could not convert '3.2o-2' in tag STW_ms to float.\n"
    assert result == 0.0
    
def test_incorrect_float2(capfd):
    '''
    Setup:       Incorrect value plus a state_id coupling
    Expectation: INFO message that the value given in the dictionary will be ignored
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['3.2o-2', {'state_id':'STW'}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == "   INFO: CWR - The given value will be overwritten by the state vector entry.\n"
    assert result == 0.0
    
def test_default_float1(capfd):
    '''
    Setup:       A default value is passed to the routine, dictionary also contains a correct value
    Expectation: Correctly converted value from dictionary, no message
    '''
    name = 'CWR'
    config_dict = {'STW_ms': ['-3.2', {}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id, 5.0)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == -3.2
    
def test_default_float2(capfd):
    '''
    Setup:       Empty config dictionary, default value passed to the routine
    Expectation: Return the default value and issue an INFO message
    '''
    name = 'CWR'
    config_dict = {}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id, 5.0)
    out, err = capfd.readouterr()
    assert out == "   INFO: CWR - Using default value for STW_ms (5.0)\n"
    assert result == 5.0
    
def test_nonetype_float1(capfd):
    '''
    Setup:       Tag content if of NoneType, no state_id given
    Expectation: ERROR message that the user must either provide a proper value
                 or define a state_id.
    '''
    name = 'CWR'
    config_dict = {'STW_ms': [None, {}]}
    tag = 'STW_ms'
    type_id = 'float'
    result=convertXMLDictEntry(name, config_dict, tag, type_id, 5.0)
    out, err = capfd.readouterr()
    assert out == "  ERROR: CWR - Omitting a value requires a state_id attribute\n"
    assert result == 0.0
    
def test_correct_int1(capfd):
    '''
    Setup:       Correct integer string
    Expectation: Correctly converted value, no message
    '''
    name = 'integer'
    config_dict = {'n': ['2', {}]}
    tag = 'n'
    type_id = 'int'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == 2
    
def test_correct_int2(capfd):
    '''
    Setup:       Correct integer string
    Expectation: Correctly converted value, no message
    '''
    name = 'integer'
    config_dict = {'n': ['100000', {}]}
    tag = 'n'
    type_id = 'int'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == 100000
    
def test_correct_int3(capfd):
    '''
    Setup:       Correct integer string
    Expectation: Correctly converted value, no message
    '''
    name = 'integer'
    config_dict = {'n': ['-2', {}]}
    tag = 'n'
    type_id = 'int'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == -2
    
def test_correct_int4(capfd):
    '''
    Setup:       Correct integer string
    Expectation: Correctly converted value, no message
    '''
    name = 'integer'
    config_dict = {'n': ['-100000', {}]}
    tag = 'n'
    type_id = 'int'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == -100000
    
def test_default_int1(capfd):
    '''
    Setup:       Empty dictionary
    Expectation: Value determined from default value, INFO message
    '''
    name = 'integer'
    config_dict = {}
    tag = 'n'
    type_id = 'int'
    result=convertXMLDictEntry(name, config_dict, tag, type_id,default_value=5)
    out, err = capfd.readouterr()
    assert result == 5
    assert out == "   INFO: integer - Using default value for n (5)\n"
    
def test_incorrect_int1(capfd):
    '''
    Setup:       Incorrect integer string
    Expectation: Result of 0 and an ERROR message
    '''
    name = 'integer'
    config_dict = {'n': ['1e5', {}]}
    tag = 'n'
    type_id = 'int'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == "  ERROR: integer - Could not convert '1e5' in tag n to int.\n"
    assert result == 0
    
def test_correct_unsigned1(capfd):
    '''
    Setup:       Correct string
    Expectation: Correctly converted value, no message
    '''
    name = 'unsigned'
    config_dict = {'n': ['2', {}]}
    tag = 'n'
    type_id = 'unsigned'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == 2
    
def test_incorrect_unsigned1(capfd):
    '''
    Setup:       String with a negative integer value
    Expectation: ERROR message
    '''
    name = 'unsigned'
    config_dict = {'n': ['-2', {}]}
    tag = 'n'
    type_id = 'unsigned'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == "  ERROR: unsigned - Could not convert '-2' in tag n to unsigned (value is negative).\n"
    assert result == 0
    
def test_incorrect_unsigned2(capfd):
    '''
    Setup:       String which can not be connverted to an integer
    Expectation: ERROR message
    '''
    name = 'unsigned'
    config_dict = {'n': ['a5', {}]}
    tag = 'n'
    type_id = 'unsigned'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == "  ERROR: unsigned - Could not convert 'a5' in tag n to unsigned.\n"
    assert result == 0
    
def test_default_unsigned1(capfd):
    '''
    Setup:       Empty dictionary, default value
    Expectation: Value determined from default value, INFO message
    '''
    name = 'unsigned'
    config_dict = {}
    tag = 'n'
    type_id = 'unsigned'
    result=convertXMLDictEntry(name, config_dict, tag, type_id, 5)
    out, err = capfd.readouterr()
    assert out == "   INFO: unsigned - Using default value for n (5)\n"
    assert result == 5
    
def test_default_unsigned2(capfd):
    '''
    Setup:       Correct unsigned integer value, redundant default value
    Expectation: Converted result, no message
    '''
    name = 'unsigned'
    config_dict = {'n': ['2', {}]}
    tag = 'n'
    type_id = 'unsigned'
    result=convertXMLDictEntry(name, config_dict, tag, type_id, 5)
    out, err = capfd.readouterr()
    assert out == ""
    assert result == 2
    
def test_correct_floatvec1(capfd):
    '''
    Setup:       Correct vector string
    Expectation: Correctly converted vector, no message
    '''
    name = 'test_floatvec1'
    config_dict = {'testvector': ['0.0 1.0 2.0', {}]}
    tag = 'testvector'
    type_id = 'float_vec'
    result=convertXMLDictEntry(name, config_dict, tag, type_id)
    out, err = capfd.readouterr()
    assert out == ""
    assert (result == np.array([0.0, 1.0, 2.0])).all()
