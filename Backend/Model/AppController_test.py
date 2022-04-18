import unittest
from flask import request
import requests

class APPTest(unittest.TestCase):
    testURL = "http://52.176.47.148:8080"
    all_fund_URL = "{}/funds/all".format(testURL)
    sign_inURL= "{}/signin".format(testURL) 
    find_fund_URL = "{}/funds/HDFC".format(testURL)
    risk_URL = "{}/fundsRisk".format(testURL)
    headers = {'Content-Type': 'application/json', 'authorization': 'Basic dXNlcjphZG1pbg=='}


    jsonsignin={
  "userId": 0,
  "userName": "",
  "userEmail": "vik",
  "userPassword": "vik",
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

    def test_1_fundsall(self):
        r = requests.get(APPTest.all_fund_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 4)

    def test_2_sign_WO_headers(self):
        r = requests.post(APPTest.sign_inURL, json=APPTest.jsonsignin)
        self.assertEqual(r.status_code, 401)

    def test_3_sign_W_headers(self):
        r = requests.post(APPTest.sign_inURL, headers=self.headers,json=APPTest.jsonsignin)
        self.assertEqual(r.status_code, 200)

    def test_4_filter_fundnamd(self):
        r = requests.get(APPTest.find_fund_URL, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), APPTest.response_by_name)
    
    def test_5_fundrisk_list(self):
        r = requests.get(APPTest.risk_URL)
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(r.json(), APPTest.risk_list)

if __name__ == '__main__':
     unittest.main()

     
# /fundsById/<id>
# /fundsHistoryById/<id>
# /funds/<fundname>