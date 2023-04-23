import requests

rawHotstar = ""
rawZeeTV = ""
try:
    rawZeeTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ZeeTV/ZeeTV.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
for rawresult in [rawZeeTV]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/INMedia.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)
