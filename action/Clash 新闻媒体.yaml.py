import requests

rawAFP = ""
rawBloomberg = ""
rawFlipBoard = ""
rawHuffpost = ""
rawInitium_Media = ""
rawNYPost = ""
rawNYTimes = ""
rawVOA = ""
rawWSJ = ""

print("Fetching remote resources")

try:
    rawAFP = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AFP/AFP.yaml").text
    rawBloomberg = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bloomberg/Bloomberg.yaml").text
    rawFlipBoard = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/FlipBoard/FlipBoard.yaml").text
    rawHuffpost = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Huffpost/Huffpost.yaml").text
    rawInitium_Media = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Clash/Initium_Media.yaml").text
    rawNYPost = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NYPost/NYPost.yaml").text
    rawNYTimes = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NYTimes/NYTimes.yaml").text
    rawVOA = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/VOA/VOA.yaml").text
    rawWSJ = requests.get("https://raw.githubusercontent.com/AntonyCyrus/Rule/main/Clash/WSJ.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

print("Processing fetched resources and writing to file")

result = ['payload:']
unique_lines = set()
for rawresult in [rawAFP, rawBloomberg, rawFlipBoard, rawHuffpost, rawInitium_Media, rawNYPost, rawNYTimes, rawVOA, rawWSJ]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

try:
    with open("./Clash/News.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
