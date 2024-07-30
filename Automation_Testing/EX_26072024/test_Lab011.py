import pytest 

@pytest.fixture()
def create_token():
    return "adf"


@pytest.fixture()
def create_booking():
    return 123


def test_consume(create_booking,create_token):
    print("token=",create_token)
    print("booing_id",create_booking)



    