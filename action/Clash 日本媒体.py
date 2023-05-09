import requests

rawAbemaTV = ""
rawDMM = ""
rawHuluJP = ""
rawNiconico = ""
rawNikkei = ""
rawNintendo = ""
rawParavi = ""
rawPixiv = ""
rawPixnet = ""
rawTver = ""
rawU_NEXT = ""

# 获取变量数据
try:
    rawAbemaTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AbemaTV/AbemaTV.yaml").text
    rawDMM = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/DMM/DMM.yaml").text
    rawHuluJP = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HuluJP/HuluJP.yaml").text
    rawNiconico = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Niconico/Niconico.yaml").text
    rawNikkei = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nikkei/Nikkei.yaml").text
    rawNintendo = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nintendo/Nintendo.yaml").text
    rawParavi = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Paravi.yaml").text
    rawPixiv = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixiv/Pixiv.yaml").text
    rawPixnet = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixnet/Pixnet.yaml").text
    rawTver = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/TVer.yaml").text
    rawU_NEXT = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/U-NEXT.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

# 处理变量数据
result = ['payload:']
unique_lines = set()
for rawresult in [rawAbemaTV, rawDMM, rawHuluJP, rawNiconico, rawNikkei, rawNintendo, rawParavi, rawPixiv, rawPixnet, rawTver, rawU_NEXT]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

# 写入文件
try:
    with open("./Clash/JPMedia.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
