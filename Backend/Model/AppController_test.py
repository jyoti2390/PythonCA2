import unittest
from flask import request
import requests

class APPTest(unittest.TestCase):
    testURL = "http://52.176.47.148:8080"
    all_fund_URL = "{}/funds/all".format(testURL)
    sign_upURL= "{}/user/add".format(testURL) 
    sign_inURL= "{}/signin".format(testURL) 
    find_fund_URL = "{}/funds/HDFC".format(testURL)
    risk_URL = "{}/fundsRisk".format(testURL)
    fundbyid_URL = "{}/fundsById/1".format(testURL)
    headers = {'Content-Type': 'application/json', 'authorization': 'Basic dXNlcjphZG1pbg=='}

    jsonsignup={
  "userId": 0,
  "userName": "test9",                              #imp change user name
  "userEmail": "test9@xya.com",                     #imp change user email
  "userPassword": "test9",                          #imp change pass
  "userPhoneNumber": "108497858",
  "userAge": "81",
  "imgSrc": ""
}

    jsonsignin={
  "userId": 0,
  "userName": "",
  "userEmail": "test5@xya.com",
  "userPassword": "test5",
  "userPhoneNumber": "",
  "userAge": "",
  "imgSrc": ""
}

    response_by_name = [
    {
        "fundId": 1,
        "fundName": "HDFC",
        "fundAmc": 2300000,
        "fundRisk": "HDFC BANK",
        "fundType": "HDFC",
        "fundAum": "HDFC",
        "fundNav": 23.66,
        "fundMgr": "low",
        "fundDesc": "Equity",
        "imgSrc": "https://imageio.forbes.com/i-forbesimg/media/lists/companies/hdfc-bank_416x416.jpg?format=jpg&height=416&width=416&fit=bounds"
    }
]

    risk_list = [
    "low",
    "high",
    "medium"
]

    def test_1_fundsall(self):  #fetch and check quantity of json document for all funds and check for status
        r = requests.get(APPTest.all_fund_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 4)

    def test_2_sign_WO_auth(self):  #sign in wo auth
        r = requests.post(APPTest.sign_inURL, json=APPTest.jsonsignin)
        self.assertEqual(r.status_code, 401)

    def test_3_sign_W_headers(self):   #sign in with auth
        r = requests.post(APPTest.sign_inURL, headers=self.headers,json=APPTest.jsonsignin)
        self.assertEqual(r.status_code, 200)
    
    def test_4_signup_WO_auth(self):   #sign up without auth
        r = requests.post(APPTest.sign_upURL, json=APPTest.jsonsignup)
        self.assertEqual(r.status_code, 401)

    def test_5_signup_W_headers(self):   #sign up with auth
        r = requests.post(APPTest.sign_upURL, headers=self.headers,json=APPTest.jsonsignup)
        self.assertEqual(r.status_code, 200)

    def test_6_filter_fundnamd(self):      #fund name filter
        r = requests.get(APPTest.find_fund_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), APPTest.response_by_name)
    
    def test_7_fundrisk_list(self):         #fund risk return list
        r = requests.get(APPTest.risk_URL)
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(r.json(), APPTest.risk_list)

    def test_8_fundsById(self):                  #one id in req to one response 
        r = requests.get(APPTest.fundbyid_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)



if __name__ == '__main__':
     unittest.main()

     
