import requests

rawDuckduckgo = ""
rawYandex = ""
try:
    rawDuckduckgo = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Duckduckgo/Duckduckgo.yaml").text
    rawYandex = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Yandex/Yandex.yaml").text
    rawOtherSearchEngie = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Clash/OtherSearchEngie.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
for rawresult in [rawDuckduckgo, rawYandex,rawOtherSearchEngie]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/SearchEngine.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)
