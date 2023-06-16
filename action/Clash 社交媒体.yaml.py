import requests

# 定义变量
rawClubhouse = ""
rawClubhouseIP = ""
rawDiscord = ""
rawFacebook = ""
rawInstagram = ""
rawKakaoTalk = ""
rawLine = ""
rawPinterest = ""
rawPotatoChat = ""
rawReddit = ""
rawSnap = ""
rawStackexchange = ""
rawTumblr = ""
rawTwitter = ""
rawVK = ""
rawWhatsapp = ""

# 请求远程资源
try:
    rawClubhouse = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Clubhouse/Clubhouse.yaml").text
    rawClubhouseIP = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ClubhouseIP/ClubhouseIP.yaml").text
    rawDiscord = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Discord/Discord.yaml").text
    rawFacebook = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.yaml").text
    rawInstagram = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.yaml").text
    rawKakaoTalk = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/KakaoTalk/KakaoTalk.yaml").text
    rawLine = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Line/Line.yaml").text
    rawPinterest = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pinterest/Pinterest.yaml").text
    rawPotatoChat = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PotatoChat/PotatoChat.yaml").text
    rawReddit = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Reddit/Reddit.yaml").text
    rawSnap = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Snap/Snap.yaml").text
    rawStackexchange = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Stackexchange/Stackexchange.yaml").text
    rawTumblr = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Tumblr/Tumblr.yaml").text
    rawTwitter = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.yaml").text
    rawVK = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/VK/VK.yaml").text
    rawWhatsapp = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Whatsapp/Whatsapp.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

# 合并结果
result = ['payload:']
unique_lines = set()
for rawresult in [rawClubhouse, rawClubhouseIP, rawDiscord, rawFacebook, rawInstagram, rawKakaoTalk, rawLine, rawPinterest, rawPotatoChat, rawReddit, rawSnap, rawStackexchange, rawTumblr, rawTwitter, rawVK, rawWhatsapp]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

try:
    with open("./Clash/SocialMedia.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)
