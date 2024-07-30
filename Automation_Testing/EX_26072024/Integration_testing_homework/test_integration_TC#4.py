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




@allure.title("TC#1--> get booking id in integration scenario4")
@allure.description("verify that booking id is getting in integration scenario 4")
@allure.tag("smoke","p0")
@allure.label("TC#1")
@pytest.mark.smoke
def test_Get_booking_id():
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"
    URL = base_url+base_path
    headers = {
        "Content-Type":"application/json",
        }
    response = requests.get(url=URL,headers=headers)
    assert response.status_code == 200
    responsedata = response.json()
    bookingid = responsedata[0]
    print(bookingid)
    print("response data:-------")
    # print(responsedata)
    return bookingid


@allure.title("Update Booking Curd Positive")
@allure.description("Tc#2-> Verify the Booking Id is uodate with valid id")
@allure.tag("regression","p0")
@allure.label("Tc#2")
@pytest.mark.smoke
def test_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/booking/"+str(test_Get_booking_id())
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




# @allure.title("TC#2-->Integration Scenario 4")
# @allure.description("verify the booking id is upadted in integration scenario 4")
# @allure.tag("smoke","p0")
# @allure.label("TC#2")
# @pytest.mark.smoke
# def test_update_booking_id():
#     base_url = "https://restful-booker.herokuapp.com"
#     base_path ="/booking/"+ str(test_Get_booking_id())
#     update_URL = base_url+base_path

#     cookie ="token=" + create_token()


#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Cookie": cookie,
#         "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
#         }
#     payload = {
#         "firstname" : "pramod",
#         "lastname" : "chikku",
#         "totalprice" : 111,
#         "depositpaid" : True,
#         "bookingdates" : {
#             "checkin" : "2018-01-01",
#             "checkout" : "2019-01-01"
#             },
#         "additionalneeds" : "Breakfast"
#         }
#     response = requests.put(url=update_URL,headers=headers,json=payload)
#     assert response.status_code == 200
#     responsedata = response.json()
#     print(responsedata)



# @allure.title("TC#3--> get booking id in integration scenario4")
# @allure.description("verify that booking id is getting in integration scenario 4")
# @allure.tag("smoke","p0")
# @allure.label("TC#3")
# @pytest.mark.smoke
# def test_Get_booking_id():
#     base_url = "https://restful-booker.herokuapp.com"
#     base_path ="/booking/"+ str(test_Get_booking_id())
#     URL = base_url+base_path
#     headers = {
#         "Content-Type":"application/json",
#         }
#     response = requests.get(url=URL,headers=headers)
#     assert response.status_code == 200
#     responsedata = response.json()
#     print(responsedata)
