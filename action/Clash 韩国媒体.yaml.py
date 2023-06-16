import requests

rawNaver = ""
rawNaverTV = ""
rawPandoraTV = ""
try:
    rawNaver = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Naver/Naver.yaml").text
    rawNaverTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NaverTV/NaverTV.yaml").text
    rawPandoraTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PandoraTV/PandoraTV.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
unique_lines = set()
for rawresult in [rawNaver, rawNaverTV, rawPandoraTV]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

try:
    with open("./Clash/KRMedia.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
