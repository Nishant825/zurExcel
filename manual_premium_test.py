import json
import requests


with open('jsondata/payloadTest.json') as json_file:
    data = json.load(json_file)


test_case_num = int(input("Enter Test Case Number: "))
def get_test_result(test_case_num):
    for i in data:
        if i["TestCaseNo."] == test_case_num:
            # print(i["payload"])
            url = "http://10.238.17.61:8001/premium_calculator"
            response = requests.post(url,json=i["payload"])
            print(response.json())


get_test_result(test_case_num)