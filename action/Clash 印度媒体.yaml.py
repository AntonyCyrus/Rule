import requests

rawZeeTV = ""

try:
    rawZeeTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ZeeTV/ZeeTV.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
unique_lines = set()  # 存储唯一行的集合
seen_lines = set()    # 存储已经看到的行的集合

for rawresult in [rawZeeTV]:
    for item in rawresult.split('\n'):
        item = item.rstrip()  # 去除尾部的空白字符
        if item.startswith('#') or item.startswith('payload:') or item in seen_lines:
            continue
        result.append(item)
        seen_lines.add(item)
        unique_lines.add(item)

result_text = '\n'.join(result)

try:
    with open("./Clash/INMedia.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
