import requests

rawMail = ""
rawProtonmail = ""

print("Fetching remote resources")

try:
    rawMail = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Mail/Mail.yaml").text
    rawProtonmail = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Protonmail/Protonmail.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

print("Processing fetched resources and writing to file")

result = ['payload:']
unique_lines = set()  # 存储唯一行的集合
seen_lines = set()    # 存储已经看到的行的集合
has_domain_suffix_mail_me = False

for rawresult in [rawMail, rawProtonmail]:
    for item in rawresult.split('\n'):
        item = item.rstrip()  # 去除尾部的空白字符
        if item.startswith('#') or item.startswith('payload:') or item in seen_lines:
            continue
        if item == '- DOMAIN-SUFFIX,mail.me.com':
            has_domain_suffix_mail_me = True
        result.append(item)
        seen_lines.add(item)
        unique_lines.add(item)

# 如果文件中没有 `- DOMAIN-SUFFIX,mail.me.com`，则添加这一行
if not has_domain_suffix_mail_me:
    result.append('- DOMAIN-SUFFIX,mail.me.com')

result_text = '\n'.join(result)

try:
    with open("./Clash/Mail.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
