import pytest
import allure
import requests




@allure.title("TC#2-->Integration Scenario2")
@allure.description("verify the booking id is created for integration scenario2")
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
             "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM=",
             }
        
        print(headers)

        response=requests.delete(url=delete_URL,headers=headers)
        responsedata = response.text
        response.status_code == 201
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
        responsedata1 = response.text
        print(responsedata)       