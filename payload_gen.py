import pandas as pd
import os
import json


def write_data(data):
    with open(f"{os.getcwd()}/jsondata/PayloadTest.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def convert_fiaCharge_to_percentage(num):
    value = int(num*100)
    return value


def convert_growthrate_to_valid_percentage(num):
    value = round(num*100, 1)
    return value


excel_data_df = pd.read_excel(
    'test_premium_cases.xlsm', sheet_name='SSP Test Cases', skiprows=2, dtype=object).fillna(0)

data = excel_data_df.to_dict('records')

# print(data)
case_list = []

for record in data[2:102]:
    print(convert_growthrate_to_valid_percentage(
        record["Illustrative Growth Rate"]), "66666666666666666666")

    if "Sex" in record:
        if record["Sex"] == 1:
            l1_gender = "M"
        else:
            l1_gender = "F"

    if "Sex.1" in record:
        if record["Sex.1"] == 1:
            l2_gender = "M"
        else:
            l2_gender = "F"

    if "Smoker" in record:
        if record["Smoker"] == 1:
            l1_smoker = "N"
        else:
            l1_smoker = "Y"

    if "Smoker.1" in record:
        if record["Smoker.1"] == 1:
            l2_smoker = "N"
        else:
            l2_smoker = "Y"

    flag = False
    if "VP Flag" in record:
        if record["VP Flag"] == 1:
            Vanishing_Term = flag
        else:
            flag = True
            Vanishing_Term = flag

    if record["Policy Term Basis"] == "Minimum":
        record["Policy Term Basis"] = "MinimumPremium"

    if record["Policy Term Basis"] == "Whole of life":
        record["Policy Term Basis"] = "WholeOfLife"

    result = {}
    payload = {
        "Product Name": "Futura",
        "Product Version": "FUTU5",
        "Policy Start Date": "01/11/2022",
        "Currency": record["Currency"],
        "Duration": record["VP Term"],
        "Vanishing Term": Vanishing_Term,
        "Life Basis": record["Policy Basis"],
        "Premium Basis": record["Policy Term Basis"],
        "WoP Basis": record['WOP Basis'],
        "Payment Frequency": record["Premium Frequency"],
        "Special Offer": record['Enhanced Allocation Flag'],
        "Single Premium": 0,
        "Regular Premium": 0,
        "Mode": "Monthly",
        "FMC": 1.6,
        "FIA Charge": convert_fiaCharge_to_percentage(record["FIA Charge"]),
        "SA Interest": 0,
        "RateList": [
            0,
            5.5,
            4.5
        ],
        "Growth Rate": convert_growthrate_to_valid_percentage(record['Illustrative Growth Rate']),
        "Insured Details": {
            "Life1": {
                "DateOfBirth": str(record["DOB"].strftime('%d/%m/%Y')),
                "Gender": l1_gender,
                "Smoker":  l1_smoker,
                "title": "Mr.",
                "Name": "Test One",
                "SumInsuredTerm": record["Sum Insured\nLife Cover"],
                "SumInsuredCI": record["Sum Insured\nCI / Cancer"],
                "CancerCover": False,
                "FTIBIncome": record["Sum Insured\nFTIB"],
                "FTIBTerm": record["Term\nFTIB"],
                "FIBIncome": record["Sum Insured\nFIB"],
                "FIBTerm": record["Term\nFIB"],
                "SumInsuredAccidentalDeath": record["Sum Insured\nAccDth"],
                "SumInsuredDismemberment": record["Sum Insured\nDismem"],
                "SumInsuredHospitalization": record["Sum Insured\nHosp"],
                "SumInsuredPTD": record["Sum Insured\nPTD"]
            },
            "Life2": {
                "DateOfBirth": str(record["DOB.1"].strftime('%d/%m/%Y')),
                "Gender": l2_gender,
                "Smoker": l2_smoker,
                "title": "Mr.",
                "Name": "Test One",
                "SumInsuredTerm": record["Sum Insured\nLife Cover.1"],
                "SumInsuredCI": record["Sum Insured\nCI / Cancer.1"],
                "CancerCover": False,
                "FTIBIncome": record["Sum Insured\nFTIB.1"],
                "FTIBTerm": record["Term\nFTIB.1"],
                "FIBIncome": record["Sum Insured\nFIB.1"],
                "FIBTerm": record["Term\nFIB.1"],
                "SumInsuredAccidentalDeath": record["Sum Insured\nAccDth.1"],
                "SumInsuredDismemberment": record["Sum Insured\nDismem.1"],
                "SumInsuredHospitalization": record["Sum Insured\nHosp.1"],
                "SumInsuredPTD": record["Sum Insured\nPTD.1"]
            }
        },
        "Loadings": {
            "Life1": {
                "Permanent": {
                    "PerMille": {
                        "Life Cover": 0,
                        "Critical Illness": 0,
                        "PTD": 0,
                        "Hospitalization": 0,
                        "FIB": 0,
                        "FTIB": 0,
                        "AccidentalDeath": 0,
                        "Dismemberment": 0,
                        "WoP": 0
                    },
                    "Percentage": {
                        "Life Cover": 0,
                        "Critical Illness": 0,
                        "PTD": 0,
                        "Hospitalization": 0,
                        "FIB": 0,
                        "FTIB": 0,
                        "AccidentalDeath": 0,
                        "Dismemberment": 0,
                        "WoP": 0
                    },
                    "Exclusions": {
                        "Life Cover": [],
                        "Critical Illness": [],
                        "PTD": [],
                        "Hospitalization": [],
                        "FIB": [],
                        "FTIB": [],
                        "AccidentalDeath": [],
                        "Dismemberment": [],
                        "WoP": []
                    }
                },
                "Temporary": {
                    "PerMille": {
                        "Life Cover": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Critical Illness": {
                            "Value": 0,
                            "Time": 0
                        },
                        "PTD": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Hospitalization": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FTIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "AccidentalDeath": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Dismemberment": {
                            "Value": 0,
                            "Time": 0
                        },
                        "WoP": {
                            "Value": 0,
                            "Time": 0
                        }
                    },
                    "Percentage": {
                        "Life Cover": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Critical Illness": {
                            "Value": 0,
                            "Time": 0
                        },
                        "PTD": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Hospitalization": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FTIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "AccidentalDeath": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Dismemberment": {
                            "Value": 0,
                            "Time": 0
                        },
                        "WoP": {
                            "Value": 0,
                            "Time": 0
                        }
                    }
                }
            },
            "Life2": {
                "Permanent": {
                    "PerMille": {
                        "Life Cover": 0,
                        "Critical Illness": 0,
                        "Hospitalization": 0,
                        "PTD": 0,
                        "FIB": 0,
                        "FTIB": 0,
                        "AccidentalDeath": 0,
                        "Dismemberment": 0,
                        "WoP": 0
                    },
                    "Percentage": {
                        "Life Cover": 0,
                        "Critical Illness": 0,
                        "Hospitalization": 0,
                        "PTD": 0,
                        "FIB": 0,
                        "FTIB": 0,
                        "AccidentalDeath": 0,
                        "Dismemberment": 0,
                        "WoP": 0
                    }
                },
                "Temporary": {
                    "PerMille": {
                        "Life Cover": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Critical Illness": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Hospitalization": {
                            "Value": 0,
                            "Time": 0
                        },
                        "PTD": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FTIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "AccidentalDeath": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Dismemberment": {
                            "Value": 0,
                            "Time": 0
                        },
                        "WoP": {
                            "Value": 0,
                            "Time": 0
                        }
                    },
                    "Percentage": {
                        "Life Cover": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Critical Illness": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Hospitalization": {
                            "Value": 0,
                            "Time": 0
                        },
                        "PTD": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "FTIB": {
                            "Value": 0,
                            "Time": 0
                        },
                        "AccidentalDeath": {
                            "Value": 0,
                            "Time": 0
                        },
                        "Dismemberment": {
                            "Value": 0,
                            "Time": 0
                        },
                        "WoP": {
                            "Value": 0,
                            "Time": 0
                        }
                    }
                }
            }
        },
        "Escalation Percentage": 0,
        "Single Premium Term": record["Single Premium Term"]
    }
    result["TestCaseNo."] = record["Test Case No."]
    result["payload"] = payload
    case_list.append(result)
# print(case_list)
write_data(case_list)
# final = json.dumps(case_list, indent=2)
# print(final)
