import pytest
import allure
import requests

@allure.title("Test GET REquest -> RestFul booker Project#1")
@allure.description("verify the Get request with valid booking id")
@allure.tag("regression","p0","smoke")
@allure.tag("TC#4")
@pytest.mark.smoke
def test_get_request_valid_bookingid():
    url = "https://restful-booker.herokuapp.com/booking/1"

    responsedata = requests.get(url)
    print(responsedata.text)
    print(responsedata.headers)
    print(responsedata.cookies)
    print(responsedata.json())
    assert responsedata.status_code==200

