import requests

rawAFP = ""
rawBloomberg = ""
rawFlipBoard = ""
rawHuffpost = ""
rawNYPost = ""
rawNYTimes = ""
rawVOA = ""

print("Fetching remote resources")

try:
    rawAFP = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AFP/AFP.yaml").text
    rawBloomberg = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bloomberg/Bloomberg.yaml").text
    rawFlipBoard = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/FlipBoard/FlipBoard.yaml").text
    rawHuffpost = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Huffpost/Huffpost.yaml").text
    rawNYPost = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NYPost/NYPost.yaml").text
    rawNYTimes = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NYTimes/NYTimes.yaml").text
    rawVOA = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/VOA/VOA.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

print("Processing fetched resources and writing to file")

result = ['payload:']
for rawresult in [rawAFP, rawBloomberg, rawFlipBoard, rawHuffpost, rawNYPost, rawNYTimes, rawVOA]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/News.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
