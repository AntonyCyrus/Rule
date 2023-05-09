import requests

urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/JOOX/JOOX.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MOOV/MOOV.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/myTVSUPER/myTVSUPER.yaml",
    "https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Clash/NowE.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PCCW/PCCW.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TVB/TVB.yaml",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ViuTV/ViuTV.yaml"
]

results = set()

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_result = response.text
        # 去掉注释和 payload 标记，只保留规则内容
        result_lines = [line.strip() for line in raw_result.split('\n') if line and not line.startswith(('#', 'payload:'))]
        results.update(result_lines)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred when requesting {url}: {e}")

result_text = '\n'.join(['payload:'] + sorted(results))

try:
    with open("./Clash/HKMedia.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
