import pytest
from stuff.liststuff import *

def test_list_keys(example_dict):
    keylist = ["key1", "key2", "key3"]
    assert list_keys(example_dict) == keylist

def test_list_values(example_dict):
    vallist = ['1', '2', '3']
    assert list_values(example_dict) == vallist

def test_conftest(example_dict):
    assert example_dict

if __name__ == '__main__':
    pytest.main()
