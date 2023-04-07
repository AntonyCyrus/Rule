import requests

rawBahamut = ""
rawCatchplay = ""
rawFriDay = ""
rawHBOAsia = ""
rawHamiVideo = ""
rawKKBOX = ""
rawKKTV = ""
rawLiTV = ""
rawLineTV = ""
rawMOMOShop = ""
rawmyVideo = ""
rawTaiWanGood = ""

try:
    rawBahamut = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bahamut/Bahamut.yaml").text
    rawCatchplay = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/CATCHPLAY%2B.yaml").text
    rawFriDay = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/friDay/friDay.yaml").text
    rawHBOAsia = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HBOAsia/HBOAsia.yaml").text
    rawHamiVideo = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HamiVideo/HamiVideo.yaml").text
    rawKKBOX = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/KKBOX/KKBOX.yaml").text
    rawKKTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/KKTV/KKTV.yaml").text
    rawLiTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/LiTV/LiTV.yaml").text
    rawLineTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/LineTV/LineTV.yaml").text
    rawMOMOShop = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MOMOShop/MOMOShop.yaml").text
    rawmyVideo = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/myVideo.yaml").text
    rawTaiWanGood = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TaiWanGood/TaiWanGood.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
for rawresult in [rawBahamut, rawCatchplay, rawFriDay, rawHBOAsia, rawHamiVideo, rawKKBOX, rawKKTV, rawLiTV, rawLineTV, rawMOMOShop, rawmyVideo, rawTaiWanGood]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/TWMedia.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)
