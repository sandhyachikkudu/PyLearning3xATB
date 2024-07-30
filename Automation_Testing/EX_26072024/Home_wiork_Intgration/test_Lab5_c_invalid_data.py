# Invalid Creation - enter a wrong payload or Wrong JSON.-----completed


import pytest
import requests
import allure


@allure.title("TC#5-->Integration Scenario 5")
@allure.description("verify the booking id is created or not for inavlid data for integration scenario 5")
@allure.tag("smoke","p0")
@allure.label("TC#5")
@pytest.mark.smoke
def test_create_booking_id():
    basic_url ="https://restful-booker.herokuapp.com"
    basic_path ="/booking"
    URL = basic_url+basic_path

    headers = { "Content-Type": "application/json" }
    payload = {
        "firstname" : 12345,
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : False,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
            },
            
        "additionalneeds" : "Breakfast"
        }

    response =requests.post(url= URL,headers = headers,json=payload)
    bookingid = response.json()["bookingid"]

    assert response.status_code == 200
    return bookingid