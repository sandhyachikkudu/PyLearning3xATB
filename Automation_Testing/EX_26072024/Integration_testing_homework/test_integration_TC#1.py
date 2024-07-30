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
    print(bookingid)
    return bookingid
    




@allure.title("TC#2-->Integration Scenario1")
@allure.description("verify the booking id is upadted in integration scenario1")
@allure.tag("smoke","p0")
@allure.label("TC#2")
@pytest.mark.smoke
def test_update_booking_id():
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(test_create_booking_id())
    update_URL = base_url+base_path

    cookie ="token=" + create_token()


    header = {
        "Content-Type":"application/json",
        "Cookie" : cookie
        }
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
    response = requests.put(url=update_URL,headers=header,json=payload)
    assert response.status_code == 200
    responsedata = response.json()
    print(responsedata)


    # Get the updated data
    # base_url = "https://restful-booker.herokuapp.com"
    # base_path ="/booking/"+str(test_create_booking_id())
    # URL = base_url+base_path
    headers = {
        "Content-Type":"application/json",
        }
    response = requests.get(url=update_URL,headers=headers)
    assert response.status_code == 200
    responsedata = response.json()
    print(responsedata)


