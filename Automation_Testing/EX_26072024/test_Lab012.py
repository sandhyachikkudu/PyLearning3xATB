import pytest
import allure
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type":"application/json"}
    payload = {
        "username" : "admin",
        "password" : "password123"
        }
    
    response = requests.post(url=url,headers=headers,json=payload)

    token = response.json()["token"] 
    return token



@pytest.fixture()
def create_booking_id():
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
    print(response)
    bookingid = response.json()["bookingid"]
    return bookingid




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



# def test_get_booking_id(create_token,create_booking_id):
#     base_url = "https://restful-booker.herokuapp.com"
#     base_path ="/booking/"+str(create_booking_id)
#     get_URL = base_url+base_path

#     cookie ="token=" + create_token


#     header = {
#         "Content-Type":"application/json",
#         "Cookie" : cookie
#         }
    
#     response = requests.get(url=get_URL,headers=header)

#     assert response.status_code == 200
#     responsedata = response.json()
#     print(responsedata)