import pytest
import allure
import requests



# For post
# url
# path
# bookingid
# token
# payload

def create_token():
    # token 
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type":"application/json"}
    payload = {
        "username" : "admin",
        "password" : "password123"
        }
    
    response = requests.post(url=url,headers=headers,json=payload)

    token = response.json()["token"] 
    return token


@allure.title("Create booking for CRUD")
@allure.description("Tc#1 -> verify the create booking for valid data")
@allure.tag("smoke","p0")
@allure.label("owner","sandhya")
@pytest.mark.smoke
def test_create_booking():
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

@allure.title("Update Booking Curd Positive")
@allure.description("Tc#2-> Verify the Booking Id is uodate with valid id")
@allure.tag("regression","p0")
@allure.label("Tc#2")
@pytest.mark.smoke
def test_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(test_create_booking())
    URL = base_url+base_path

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
    response = requests.put(url=URL,headers=header,json=payload)
    assert response.status_code == 200

    responsedata = response.json()
    print(responsedata)
    assert responsedata["firstname"] == "sand"
    assert responsedata["lastname"] == "chikku"



    def test_delete_id():
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = test_create_booking()
        delete_URL = URL+booking_id

        cookie_value = "token="+create_token()
        headers = {
            "Content-Type": "application/json",
                   "Cookie" :"cookie_value" }
        
        print(headers)

        response=requests.delete(url=delete_URL,headers=headers)
        
    


    










