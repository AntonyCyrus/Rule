import requests

rawJOOX = ""
rawMOOV = ""
rawmyTVSUPER = ""
rawNowE = ""
rawPCCW = ""
rawTVB = ""
rawViuTV = ""

try:
    rawJOOX = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/JOOX/JOOX.yaml").text
    rawMOOV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MOOV/MOOV.yaml").text
    rawmyTVSUPER = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/myTVSUPER/myTVSUPER.yaml").text
    rawNowE = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Clash/NowE.yaml").text
    rawPCCW = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PCCW/PCCW.yaml").text
    rawTVB = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TVB/TVB.yaml").text
    rawViuTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ViuTV/ViuTV.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
unique_lines = set()
for rawresult in [rawJOOX, rawMOOV, rawmyTVSUPER, rawNowE, rawPCCW, rawTVB, rawViuTV]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

try:
    with open("./Clash/HKMedia.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
