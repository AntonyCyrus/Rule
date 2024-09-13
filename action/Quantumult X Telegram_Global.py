import requests
import pytz
from datetime import datetime

result = []

# 定义需要请求的链接
telegram_url = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Quantumult X/Telegram/Telegram.list"
region_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Quantumult X/TelegramUS/TelegramUS.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Quantumult X/TelegramSG/TelegramSG.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Quantumult X/TelegramNL/TelegramNL.list"
]

# 获取 Telegram Global 的规则文件内容
try:
    rawTelegram = requests.get(telegram_url).text
except requests.exceptions.RequestException as e:
    print("Error getting Telegram Global data:", e)
    rawTelegram = ""

# 获取各个地区的规则文件内容并合并
region_rules = set()
for url in region_urls:
    try:
        raw = requests.get(url).text
        # 将每个规则文件中的有效内容（过滤掉注释和空行）添加到集合中
        region_rules.update([item.strip() for item in raw.split("\n") if item.strip() and not item.startswith('#')])
    except requests.exceptions.RequestException as e:
        print(f"Error getting data from {url}: {e}")

# 对比出 Global 文件中不包含在 US、SG、NL 中的内容
for line in rawTelegram.split("\n"):
    stripped_line = line.strip()
    if stripped_line and not stripped_line.startswith('#') and stripped_line not in region_rules:
        result.append(stripped_line)

# 获取当前时间并格式化
tz = pytz.timezone('Asia/Shanghai')
now = datetime.now(tz)
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# 拼接要写入文件的字符串
result_text = "# Telegram_Global.list\n# Generated at " + time_str + "\n\n" + "\n".join(result) + "\n\n# This configuration file has been generated successfully."

# 将字符串写入文件
try:
    with open("./Quantumult X/Telegram_Global.list", "w", encoding="utf-8") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
