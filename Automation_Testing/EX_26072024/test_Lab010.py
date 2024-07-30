
import pytest

@pytest.fixture()
def sample_data():
    data = [1,2,3,4,5]
    return True

@pytest.fixture()
def sample_data2():
    return True

def test_data(sample_data,sample_data2):
    print(sample_data)
    print(sample_data2)


    