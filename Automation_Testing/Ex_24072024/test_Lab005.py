import pytest
import allure
import requests

@allure.title("Test GET Request - RestFul Booker Priject#1")
@allure.description("TC#1 -> Verify that GET Request work with ID")
@allure.tag("regression","p0","smoke")
@allure.label("owner","Pramod")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responsedata =requests.get(url)
    print(responsedata.json())
    assert responsedata.status_code == 200



@allure.title("Tst Get Request -> RestFul Booker Project#1")
@allure.description("Tc#2 -> Verify that Get Request Work with invalid bookingid ID")
@allure.tag("regression","p1","smoke")
@allure.label("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_invalid_id():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responsdata = requests.get(url)
    print(responsdata.text)
    assert responsdata.status_code == 200


@allure.title("Test GET Request -> RestFul Booker Project#1")
@allure.description("TC#2 -> verify that GET Request with invalid BOokingId")
@allure.tag("regression","p0","smoke")
@allure.label("TC#3")
@pytest.mark.smoke
def test_get_request_invalid_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responsedata = requests.get(url)
    print(responsedata.json())
    assert responsedata.status_code == 404
