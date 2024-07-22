**SOAP API TESTING**
**Project Name: Number Conversion Service**

**Project URL:**

https://www.dataaccess.com/webservicesserver/NumberConversion.wso

**Project Description:**

This project involves testing the SOAP API for number to words conversion. The API converts numerical input into its English word equivalent. The testing focuses on validating the functionality of the API endpoint and handling various input scenarios.

**Test Cases:**

A set of Postman test cases have been created to cover different scenarios for the number to words conversion API. These include positive and negative test cases to ensure robustness and accuracy in conversion results.

[SOAP API TEST CASES.xlsx](https://github.com/user-attachments/files/16332146/SOAP.API.TEST.CASES.xlsx)


**Running Tests with Newman:**

Newman is a command-line collection runner for Postman. It allows you to run and test a Postman collection directly from the command line.

**Prerequisites:**

Node.js installed on your system.

Newman installed globally via npm.

**Installation:**

1.Install Node.js.

2.Install Newman globally using npm:

  npm install -g newman
  
**Execution of Testcases:**

Open commandline: newman run "https://api.postman.com/collections/36343203-64da35a8-2c42-4927-86bb-50ff4f92e7f3?access_key" -r cli,htmlextra


**Newman Report:**

![newman_report](https://github.com/user-attachments/assets/21356c43-d890-4f00-8e65-48f128a86146)
