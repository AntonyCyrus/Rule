import requests

rawJOOX = ""
rawMOOV = ""
rawmyTVSUPER = ""
rawNowE = ""
rawPCCW = ""
rawTVB = ""
try:
    rawJOOX = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/JOOX/JOOX.yaml").text
    rawMOOV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MOOV/MOOV.yaml").text
    rawmyTVSUPER = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/myTVSUPER/myTVSUPER.yaml").text
    rawNowE = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Clash/NowE.yaml").text
    rawPCCW = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PCCW/PCCW.yaml").text
    rawTVB = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TVB/TVB.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
for rawresult in [rawJOOX, rawMOOV, rawmyTVSUPER, rawNowE, rawPCCW, rawTVB]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./HKMedia.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)
