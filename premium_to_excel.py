import json
import pandas as pd

# pd.read_json("jsondata/premium_test_case_result.json").to_excel("premium_excel/premiumTest.xlsx")

with open('jsondata/premium_test_case_result.json') as json_file:
    data = json.load(json_file)
print(data)

resp_list = []
for i in data:
    resp_dict = {}
    resp_dict["Test Case No."]
    pass
df = pd.DataFrame.from_dict(resp_list)
print (df)
df.to_excel('players.xlsx',index=False)
