import requests
import pytz
from datetime import datetime

result = []

# 定义需要请求的链接
urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Clubhouse/Clubhouse.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/ClubhouseIP/ClubhouseIP.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Discord/Discord.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Facebook/Facebook.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Instagram/Instagram.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/KakaoTalk/KakaoTalk.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Line/Line.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Pinterest/Pinterest.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/PotatoChat/PotatoChat.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Reddit/Reddit.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Snap/Snap.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Stackexchange/Stackexchange.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Tumblr/Tumblr.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Twitter/Twitter.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/VK/VK.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Whatsapp/Whatsapp.list"
]

# 遍历链接列表，依次请求链接内容并将结果保存到 result 列表中
for url in urls:
    try:
        raw = requests.get(url).text
        result.extend([item for item in raw.split("\n") if item.strip() and not item.startswith('#')])
    except requests.exceptions.RequestException as e:
        print("Error getting data:", e)

# 去除重复的行
result = list(set(result))

# 获取当前时间并格式化
tz = pytz.timezone('Asia/Shanghai')
now = datetime.now(tz)
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# 拼接要写入文件的字符串
result_text = "# SocialMedia.list\n# Generated at " + time_str + "\n\n" + "\n".join(result) + "\n\n# This configuration file has been generated successfully."

# 将字符串写入文件
with open("./Shadowrocket/SocialMedia.list", "w", encoding="utf-8") as f:
    f.write(result_text)
