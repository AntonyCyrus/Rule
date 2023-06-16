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
unique_lines = set()
for rawresult in [rawMail, rawProtonmail]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

try:
    with open("./Clash/Mail.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
