import requests
import json
import os
from payload_gen import write_data




def write_data(data):
    with open(f"{os.getcwd()}/jsondata/premium_test_case_result.json", "w") as outfile:
        json.dump(data,outfile,indent=4)


with open('jsondata/payloadTest.json') as json_file:
    data = json.load(json_file)


test_result = []
for record in data:
    try:
        print(f"test case running for {record['TestCaseNo.']}")
        url = ""
        # response = requests.post(url,json=record["payload"])
        resp_dict = {}
        resp_dict["payload"] = record['payload']
        # resp_dict["result"] = response.json()
        resp_dict["Response"] = "yoo"
        test_dict = {}
        test_dict["TestCaseNo."] = record['TestCaseNo.']
        test_dict["Payload and Response"] = resp_dict
        test_result.append(test_dict)
        print(f"test case compeleted for {record['TestCaseNo.']}")
    except Exception as e:
        print(str(e))
        print(f"test case stopped for {record['TestCaseNo.']}")

write_data(test_result)

