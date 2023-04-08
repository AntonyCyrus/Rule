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
for rawresult in [rawMail, rawProtonmail]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/Mail.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
