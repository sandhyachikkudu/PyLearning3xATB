# fixture - conceot in python
# you can ude the fixture
# context to the test 
# similar ti pre condition and post condition
# setup and tear down - pre and post condition

import pytest

@pytest.fixture()
def is_married():
    return  True

def test_i_need_to_confirm(is_married):
    assert is_married == True




