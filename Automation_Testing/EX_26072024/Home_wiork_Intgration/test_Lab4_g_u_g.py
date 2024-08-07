# Get an Existing Booking from Get All Bookings Ids , Update a Booking and Verify using GET by id.

import pytest
import allure
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"  
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token



@pytest.fixture()
def get_existing_id():
    url="https://restful-booker.herokuapp.com/booking"
    response=requests.get(url=url)
    data = response.json()
    booking_id = data[0]["bookingid"]
    return booking_id



@allure.title("TC#4-->Integration Scenario 4")
@allure.description("verify that  booking id is updated for integration scenario 4")
@allure.tag("smoke","p0")
@allure.label("TC#4")
def test_update_req(create_token,get_existing_id):
    print("Token ->", create_token)
    print("Bookingid ->", get_existing_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(get_existing_id)
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "krishna",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    #to get the updated id
    response = requests.get(url=PUT_URL, headers=headers)
    assert response.status_code == 200