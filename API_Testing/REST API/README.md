**API TESTING - REST**

**Project Name: BOOKING ID**


**Project URL:**

https://restful-booker.herokuapp.com/apidoc/index.html


**Project Description:**

This project involves testing the Rest API for Booking Id. The API Create the booking and gives booking id details, update the booking id and delete the booking id. The testing focuses on validating the functionality of the API endpoint and handling various input scenarios.

**Test Cases:**

A set of Postman test cases have been created to cover different scenarios for the creating,updating,geting and delete booking id API. These include positive and negative test cases to ensure robustness and accuracy in booking id results.

[Testcases_Rest API.xlsx](https://github.com/user-attachments/files/16329380/Testcases_Rest.API.xlsx)

**Running Tests with Newman:**

Newman is a command-line collection runner for Postman. It allows you to run and test a Postman collection directly from the command line.

**Prerequisites:**

Node.js installed on your system.

Newman installed globally via npm.

**Installation**

1.Install Node.js.

2.Install Newman globally using npm:

    npm install -g newman

**Execution of Testcases:**

Open commandline:
newman run "https://api.postman.com/collections/36343203-64da35a8-2c42-4927-86bb-50ff4f92e7f3?access_key" -r cli,htmlextra


**Newman Report**


![newmanreport](https://github.com/user-attachments/assets/a7643609-7412-4e4d-a32f-58dc462d9603)
