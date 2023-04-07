import requests
import pytz
from datetime import datetime

result = []

try:
    rawJOOX = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/JOOX/JOOX.list").text
    result.extend([item for item in rawJOOX.split("\n") if item.strip() and not item.startswith('#')])
except requests.exceptions.RequestException as e:
    print("Error getting JOOX data:", e)

try:
    rawMOOV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/MOOV/MOOV.list").text
    result.extend([item for item in rawMOOV.split("\n") if item.strip() and not item.startswith('#')])
except requests.exceptions.RequestException as e:
    print("Error getting MOOV data:", e)

try:
    rawmyTVSUPER = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/myTVSUPER/myTVSUPER.list").text
    result.extend([item for item in rawmyTVSUPER.split("\n") if item.strip() and not item.startswith('#')])
except requests.exceptions.RequestException as e:
    print("Error getting myTVSUPER data:", e)

try:
    rawNowE = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Surge/NowE.list").text
    result.extend([item for item in rawNowE.split("\n") if item.strip() and not item.startswith('#')])
except requests.exceptions.RequestException as e:
    print("Error getting NowE data:", e)

try:
    rawPCCW = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PCCW/PCCW.list").text
    result.extend([item for item in rawPCCW.split("\n") if item.strip() and not item.startswith('#')])
except requests.exceptions.RequestException as e:
    print("Error getting PCCW data:", e)

try:
    rawTVB = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/TVB/TVB.list").text
    result.extend([item for item in rawTVB.split("\n") if item.strip() and not item.startswith('#')])
except requests.exceptions.RequestException as e:
    print("Error getting TVB data:", e)

tz = pytz.timezone('Asia/Shanghai')
now = datetime.now(tz)
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

result_text = "# HKMedia.list\n# Generated at " + time_str + "\n\n" + "\n".join(result) + "\n\n# This configuration file has been generated successfully."

with open("./Surge/HKMedia.list", "w", encoding="utf-8") as f:
    f.write(result_text)
