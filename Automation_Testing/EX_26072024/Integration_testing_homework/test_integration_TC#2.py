import pytest
import allure
import requests


def create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload ={
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url=URL,headers=headers,json=payload)
    return response.json()["token"]



@allure.title("TC#1-->Integration Scenario2")
@allure.description("verify the booking id is created for integration scenario2")
@allure.tag("smoke","p0")
@allure.label("TC#1")
@pytest.mark.smoke
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



@allure.title("TC#1-->Integration Scenario2")
@allure.description("verify the booking id is created for integration scenario2")
@allure.tag("smoke","p0")
@allure.label("TC#2")
@pytest.mark.regression
def test_delete_id():
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = test_create_booking_id()
        delete_URL = URL+str(booking_id)

        cookie_value = "token="+create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie" :"cookie_value",
             "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM=",
             }
        
        print(headers)

        response=requests.delete(url=delete_URL,headers=headers)
        responsedata = response.text
        response.status_code == 201
        print(responsedata)
        
        



@allure.title("TC#3--> get the deleted booking id in integration scenario2")
@allure.description("verify that deleted booking id is gettin in integration scenario2")
@allure.tag("smoke","p0")
@allure.label("TC#3")
@pytest.mark.smoke
def test_Get_booking_id():
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(test_create_booking_id())
    URL = base_url+base_path
    headers = {
        "Content-Type":"application/json",
        }
    response = requests.get(url=URL,headers=headers)
    assert response.status_code == 200

    responsedata = response.json()
    responsedata1 = response.text
    print(responsedata)       