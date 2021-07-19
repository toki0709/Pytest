import pytest
from inout.readconfig import convertXMLAttributesDictEntry 
import inout.messages as msg
import numpy as np


""" Test routines for convertXMLAttributesDictEntry """


""" TEST FOR Type_id = float """


def test_correct_float1(capfd):
    """ Test for the type_id Float. This test will check if the function can convert the value to float in config_dict[tag][1][attribute]

    Expected: Error Messgage.
    """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'float'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'no'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()
    ''' This test will check the following error message '''
    assert out == "  ERROR: State Vector - Could not convert 'no' in tag STW to float.\n"


def test_correct_float2(capfd):
    """ Test for the type_id Float. This test will check if the function can convert the value to float in config_dict[tag][1][attribute] 
    Expected: return 0.0.
    """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'float'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'no'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()
    ''' This test will check the following return type'''
    assert out == "  ERROR: State Vector - Could not convert 'no' in tag STW to float.\n"
    assert result == 0.0


""" TEST FOR Type_id = int """


def test_correct_int1(capfd):
    """ Test for the type_id int. This test will check if the function can convert the value to int in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'int'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'no'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check the following error message '''
    assert out == "  ERROR: State Vector - Could not convert 'no' in tag STW to int.\n"


def test_correct_int2(capfd):
    """ Test for the type_id int. This test will check if the function can convert the value to int in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'int'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'no'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check the following return type '''
    assert result == 0


""" TEST FOR Type_id = Boolen """


def test_true_bool1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'yes'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning True '''
    assert result == True


def test_true_bool2(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'y'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning True '''
    assert result == True


def test_true_bool3(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'Yes'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning True '''
    assert result == True


def test_true_bool4(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': '1'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning True '''
    assert result == True


def test_true_bool5(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'True'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning True '''
    assert result == True


def test_true_bool6(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 't'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning True '''
    assert result == True


def test_incorrect_true_bool1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'YES'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check the following error message '''
    assert out == "  ERROR: State Vector - Could not convert 'YES' in tag STW to boolean.\n"


def test_false_bool1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'no'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning False '''
    assert result == False


def test_false_bool2(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'n'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning False '''
    assert result == False


def test_false_bool3(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': '0'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning False '''
    assert result == False


def test_false_bool4(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'False'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning False '''
    assert result == False


def test_false_bool5(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'f'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning False '''
    assert result == False


def test_false_bool6(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'false'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check if it is returning False '''
    assert result == False


def test_incorrect_false_bool1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'FALSE'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check the following error message '''
    assert out == "  ERROR: State Vector - Could not convert 'FALSE' in tag STW to boolean.\n"


def test_incorrect_bool1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'bool'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': ''}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check the following error message '''
    assert out == "  ERROR: State Vector - Could not convert '' in tag STW to boolean.\n"


""" TEST FOR Type_id = str """


def test_correct_str1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to str in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'str'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': 'yes'}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

    ''' This test will check the config_dict[tag][1][attributes]'''
    assert result == 'yes'


""" Testing for incorrect str """

'''
def test_incorrect_str1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to str in config_dict[tag][1][attribute] """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'str'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': ''}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id)
    out, err = capfd.readouterr()

   

    assert out == "  ERROR: State Vector - Could not convert '' in tag STW to str.\n"'''



def test_float_vector(capfd):
    """ testing for float vector.
    Expected: return [0.0 0.0 0.0]
    """
    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'float_vec'
    default_value = None
    config_dict = {'STW': ['0.0 1.0 2.0', {'optimize': 'no'}]}
    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id, default_value=None)
    out, err = capfd.readouterr()
    ''' This test will check if it is returning [0.0 0.0 0.0] '''
    assert (result == np.array([0.0, 0.0, 0.0])).all()



def test_float_vector2(capfd):
    """ testing for float vector.
    Expected: Error Message
    """
    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'float_vec'
    default_value = None
    config_dict = {'STW': ['0.0 1.0 2.0', {'optimize': 'no'}]}
    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id, default_value=None)
    out, err = capfd.readouterr()

    ''' This test will check the following error message '''
    assert out == "  ERROR: State Vector - Could not convert 'no' in tag STW to float vector.\n"


def test_default_value1(capfd):
    """ Test for the type_id bool. This test will check if the function can convert the value to bool in config_dict[tag][1].keys() """

    attribute = 'optimize'
    name = 'State Vector'
    tag = 'STW'
    type_id = 'str'
    default_value = None
    config_dict = {'STW': ['10', {'optimize': ''}]}

    result = convertXMLAttributesDictEntry(
        name, config_dict, tag, attribute, type_id, default_value=None)
    out, err = capfd.readouterr()
    ''' This test will check the following empty attributes '''
    assert out == ''
