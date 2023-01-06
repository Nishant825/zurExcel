import httpx
import json
import os
import asyncio
import time


def write_data(data):
    with open(f"{os.getcwd()}/jsondata/premium_test_case_result.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


with open('jsondata/payloadTest.json') as json_file:
    data = json.load(json_file)


async def get_test_case_result(record):
    async with httpx.AsyncClient() as client:
        print(f"test case running for {record['TestCaseNo.']}")
        url = "http://127.0.0.1:8001/premium_calculator"
        resp = await client.post(url, json=record["payload"])
        print(f"test case compeleted for {record['TestCaseNo.']}")
        resp_dict = {}
        resp_dict["payload"] = record['payload']
        resp_dict["Response"] = resp.json()
        test_dict = {}
        test_dict["TestCaseNo."] = record['TestCaseNo.']
        test_dict["Payload and Response"] = resp_dict
        print(resp.status_code)


async def main():
    task_list = []
    for record in data:
        task_list.append(get_test_case_result(record))
    await asyncio.gather(*task_list)


if __name__ == '__main__':
    start_time = time.monotonic()
    asyncio.run(main())
    print(f"Time Taken:{time.monotonic() - start_time}")
  
    # write_data(test_result)
