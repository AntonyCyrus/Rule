import requests
import pytz
from datetime import datetime

result = []

# 定义需要请求的链接
urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Clubhouse/Clubhouse.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/ClubhouseIP/ClubhouseIP.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Discord/Discord.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Facebook/Facebook.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Instagram/Instagram.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/KakaoTalk/KakaoTalk.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Line/Line.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Pinterest/Pinterest.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PotatoChat/PotatoChat.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Reddit/Reddit.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Snap/Snap.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Stackexchange/Stackexchange.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Tumblr/Tumblr.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitter/Twitter.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/VK/VK.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Whatsapp/Whatsapp.list"
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
with open("./Surge/SocialMedia.list", "w", encoding="utf-8") as f:
    f.write(result_text)
