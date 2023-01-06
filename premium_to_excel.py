import json
import pandas as pd


with open('jsondata/premium_test_case_result.json') as json_file:
    data = json.load(json_file)

resp_list = []
for i in data:
    resp_dict = {}
    resp_dict["Test Case No."] = i["TestCaseNo."]
    if "response" in i["Payload and Response"]["Response"]["result"]:
        resp_dict["local premium"] = i["Payload and Response"]["Response"]["result"]["response"]["premium"]
    elif "errorList" in i["Payload and Response"]["Response"]["result"]:
        resp_dict["local premium"] = i["Payload and Response"]["Response"]["result"]["errorList"][0]["message"]
    else:
        resp_dict["local premium"] = ""

    resp_list.append(resp_dict)

df = pd.DataFrame.from_dict(resp_list)
df.index.name = "Sr No."
df.index += 1

df.to_excel('premium_excel/TestCaseResult.xlsx')
