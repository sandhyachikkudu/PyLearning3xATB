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

@pytest.fixture()
def read_csv_file_data():
    pass



@pytest.fixture()
def read_mysql_data():
    pass



@pytest.fixture()
def launch_browser():
    pass




@pytest.fixture()
def close_browser():
    pass




@pytest.fixture()
def read_xcel_url_file():
    pass
