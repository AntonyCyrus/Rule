import requests

# Telegram 规则文件
rawTelegramGlobal = ""

# Telegram 各地区规则文件
rawTelegramUS = ""
rawTelegramSG = ""
rawTelegramNL = ""

# 从 GitHub 获取规则文件
try:
    rawTelegramGlobal = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram_No_Resolve.yaml").text
    rawTelegramUS = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TelegramUS/TelegramUS_No_Resolve.yaml").text
    rawTelegramSG = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TelegramSG/TelegramSG_No_Resolve.yaml").text
    rawTelegramNL = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TelegramNL/TelegramNL_No_Resolve.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

# 处理规则：删除与 US、SG、NL 相同的内容
result = ['payload:']
unique_lines = set()

# 将 US、SG、NL 三个文件的内容都存储到一个集合中
for region_rule in [rawTelegramUS, rawTelegramSG, rawTelegramNL]:
    for line in region_rule.split('\n'):
        if line and not line.startswith('#') and not line.startswith('payload:'):
            unique_lines.add(line.rstrip())

# 保留 Global 文件中不重复的内容
for item in rawTelegramGlobal.split('\n'):
    if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
        continue
    result.append(item.rstrip())

# 将处理后的内容写入到 TelegramGlobal.yaml
try:
    with open("./Clash/Telegram_Global.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)

print("TelegramGlobal.yaml 文件已生成")
