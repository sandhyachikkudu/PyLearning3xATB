# creating CRUD for Booking Id

# for creation 
    # -url
    # data
    # header - Content-Type=Application/json
    # method
    # auth-no
# for update -url,data,auth,booking id
# for get -url,bookingid
# for delete -url,bookingid

import pytest
import allure
import requests


@allure.title("Create Booking CRUD positive")
@allure.description("TC#1-> Verify the Booking is create with valid data")
@allure.tag("smoke","p0")
@allure.label("owner","sandhya")
@pytest.mark.smoke
def test_create_booking_id_positive():
    basic_url ="https://restful-booker.herokuapp.com"
    basic_path ="/booking"
    # Url = "https://restful-booker.herokuapp.com/booking"
    URL = basic_url+basic_path
    headers = {"Content-Type": "application/json"}
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
    
    response = requests.post(url=URL,headers=headers,json=payload)
   
    assert response.status_code == 200
    
    responsedata = response.json()
    # print(responsedata.headers)
    
    assert responsedata["bookingid"] is not None
    assert responsedata["bookingid"] > 0
    assert responsedata["booking"]["firstname"] == "Jim"
    assert responsedata["booking"]["lastname"] == "Brown"
    assert responsedata["booking"]['totalprice'] is not None
    assert responsedata["booking"]["depositpaid"] == True
    assert responsedata["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert responsedata["booking"]["bookingdates"]["checkout"] == "2019-01-01"




@allure.title("Create Booking CRUD negative")
@allure.description("TC#2-> verify the booking is not created with this {}")
@allure.tag("regression","p1")
@allure.label("owner","sandhya")
@pytest.mark.regression
def test_create_booking_id_negative():
    basic_url ="https://restful-booker.herokuapp.com"
    basic_path ="/booking"
    URL = basic_url+basic_path
    headers = {"Content-Type": "application/json"}
    payload = { }


    response = requests.post(url=URL,headers=headers,json=payload)

    assert response.status_code == 200










