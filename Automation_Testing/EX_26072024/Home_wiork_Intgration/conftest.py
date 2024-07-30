import pytest
import allure
import requests


@pytest.fixture()
def create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload ={
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url=URL,headers=headers,json=payload)
    return response.json()["token"]

@pytest.fixture()
@allure.title("TC#1-->Integration Scenario1")
@allure.description("verify the booking id is created for integration scenario1")
@allure.tag("smoke","p0")
@allure.label("TC#1")
def test_create_booking_id():
    basic_url ="https://restful-booker.herokuapp.com"
    basic_path ="/booking"
    URL = basic_url+basic_path

    headers = { "Content-Type": "application/json" }
    payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
            },
            
        "additionalneeds" : "Breakfast"
        }

    response =requests.post(url= URL,headers = headers,json=payload)
    bookingid = response.json()["bookingid"]
    assert response.status_code == 200
    print(bookingid)
    return bookingid