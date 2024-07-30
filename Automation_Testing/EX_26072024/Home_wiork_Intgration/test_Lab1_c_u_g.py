import pytest
import allure
import requests

@allure.title("TC#2-->Integration Scenario1")
@allure.description("verify the booking id is upadted in integration scenario1")
@allure.tag("smoke","p0")
@allure.label("TC#2")
@pytest.mark.smoke

def test_update_booking_id(create_token,test_create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(test_create_booking_id)
    update_URL = base_url+base_path

    cookie ="token=" + create_token


    header = {
        "Content-Type":"application/json",
        "Cookie" : cookie,
        "Accept": "application/json"
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
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(test_create_booking_id)
    URL = base_url+base_path
    headers = {
        "Content-Type":"application/json",
        }
    response = requests.get(url=URL,headers=headers)
    assert response.status_code == 200
    responsedata = response.json()
    print(responsedata)




