import pytest

@pytest.fixture(autouse=True)
def example_dict():
    keylist = ["key1", "key2", "key3"]
    vallist = ['1', '2', '3']
    testdict = dict(zip(keylist, vallist))
    return testdict
