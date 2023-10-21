import requests
import pytz
from datetime import datetime

result = []

# 定义需要请求的链接
urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Mail/Mail.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Protonmail/Protonmail.list"
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

# 检查是否已存在DOMAIN-SUFFIX,mail.me.com，如果不存在，则添加该行
if 'DOMAIN-SUFFIX,mail.me.com' not in result:
    result.append('DOMAIN-SUFFIX,mail.me.com')

# 获取当前时间并格式化
tz = pytz.timezone('Asia/Shanghai')
now = datetime.now(tz)
time_str = now.strftime("%Y-%m-d %H:%M:%S")

# 拼接要写入文件的字符串
result_text = "# Mail.list\n# Generated at " + time_str + "\n\n" + "\n".join(result) + "\n\n# This configuration file has been generated successfully."

# 将字符串写入文件
with open("./Surge/Mail.list", "w", encoding="utf-8") as f:
    f.write(result_text)
