import pytest
import allure
import requests

def test_update_booking_1(create_token,create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(create_booking_id)
    URL = base_url+base_path

    cookie ="token=" + create_token


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
    response = requests.put(url=URL,headers=header,json=payload)
    assert response.status_code == 200

    responsedata = response.json()
    print(responsedata)





def test_update_booking_2(create_token,create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(create_booking_id)
    URL = base_url+base_path

    cookie ="token=" + create_token


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
    response = requests.put(url=URL,headers=header,json=payload)
    assert response.status_code == 200

    responsedata = response.json()
    print(responsedata)