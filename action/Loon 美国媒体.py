import requests
import pytz
from datetime import datetime

result = []

# 定义需要请求的链接
urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GoogleVoice/GoogleVoice.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/9News/9News.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Americasvoice/Americasvoice.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Bestbuy/Bestbuy.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/CBS/CBS.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/CNN/CNN.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/CWSeed/CWSeed.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Espn/Espn.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/FuboTV/FuboTV.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/HuluUSA/HuluUSA.list",
    "https://raw.githubusercontent.com/HotKids/Rules/master/Surge/RULE-SET/Star%2B%2B.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Sling/Sling.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/NBC/NBC.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Oreilly/Oreilly.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/PBS/PBS.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Peacock/Peacock.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Viki/Viki.list"
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
result_text = "# USMedia.list\n# Generated at " + time_str + "\n\n" + "\n".join(result) + "\n\n# This configuration file has been generated successfully."

# 将字符串写入文件
with open("./Loon/USMedia.list", "w", encoding="utf-8") as f:
    f.write(result_text)
