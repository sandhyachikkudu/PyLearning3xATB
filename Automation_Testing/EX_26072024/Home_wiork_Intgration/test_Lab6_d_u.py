# Trying to Update on a Deleted Id -> 404

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
@allure.title("TC#6-->Integration Scenario6")
@allure.description("verify the booking id is created for integration scenario 6")
@allure.tag("smoke","p0")
@allure.label("TC#6")
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
    return bookingid

@allure.title("TC#2-->Integration Scenario 6")
@allure.description("verify the booking id is deleted for integration scenario 6")
@allure.tag("smoke","p0")
@allure.label("TC#2")
@pytest.mark.regression
def test_delete_id(create_token,test_create_booking_id):
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = test_create_booking_id
        delete_URL = URL+str(booking_id)

        cookie_value = "token="+create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie" :"cookie_value",
             "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="
             }
        
        print(headers)

        response=requests.delete(url=delete_URL,headers=headers)
        responsedata = response.text
        print(responsedata)
        assert response.status_code ==201



        base_url = "https://restful-booker.herokuapp.com"
        base_path ="/booking/"+str(test_create_booking_id)
        URL = base_url+base_path

        cookie ="token=" + create_token
        header = {
             "Content-Type":"application/json","Cookie" : cookie}
        payload = {
            "firstname" : "sand",
            "lastname" : "chikku",
            "totalprice" : 111,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : "2018-01-01",
                "checkout" : "2019-01-01"
                },
            "additionalneeds" : "Breakfast"
        }
        response = requests.put(url=URL,headers=header,json=payload)
        assert response.status_code == 200
        responsedat = response.json()
        print(responsedat)