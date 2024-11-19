import requests

rawGoogleVoice = ""
raw9News = ""
rawAmericasvoice = ""
rawBestbuy = ""
rawCBS = ""
rawCNN = ""
rawCWSeed = ""
rawEspn = ""
rawFuboTV = ""
rawHuluUSA = ""
rawStarPlus = ""
rawSling = ""
rawNBC = ""
rawOreilly = ""
rawPBS = ""
rawPeacock = ""
rawViki = ""

try:
  rawGoogleVoice= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleVoice/GoogleVoice.yaml").text
  raw9News= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/9News/9News.yaml").text
  rawAmericasvoice=requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Americasvoice/Americasvoice.yaml").text
  rawBestbuy= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bestbuy/Bestbuy.yaml").text
  rawCBS= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/CBS/CBS.yaml").text
  rawCNN= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/CNN/CNN.yaml").text
  rawCWSeed= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/CWSeed/CWSeed.yaml").text
  rawEspn= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Espn/Espn.yaml").text
  rawFuboTV= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/FuboTV/FuboTV.yaml").text
  rawHuluUSA= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HuluUSA/HuluUSA.yaml").text
  rawStarPlus= requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Star%2B%2B.yaml").text
  rawSling= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Sling/Sling.yaml").text
  rawNBC= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NBC/NBC.yaml").text
  rawOreilly= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Oreilly/Oreilly.yaml").text
  rawPBS= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PBS/PBS.yaml").text
  rawPeacock= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Peacock/Peacock.yaml").text
  rawViki= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Viki/Viki.yaml").text

except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
unique_lines = set()
for rawresult in [rawGoogleVoice, raw9News, rawAmericasvoice, rawBestbuy, rawCBS, rawCNN, rawCWSeed, rawEspn, rawFuboTV, rawHuluUSA, rawStarPlus, rawSling, rawNBC, rawOreilly, rawPBS, rawPeacock, rawViki]:
    for item in rawresult.split('\n'):
        if item.startswith('#') or item.startswith('payload:') or item in unique_lines:
            continue
        result.append(item.rstrip())
        unique_lines.add(item)
result_text = '\n'.join(result)

try:
    with open("./Clash/USMedia.yaml", "w") as f:
        f.write("\n".join(result))
except IOError as e:
    print("Error occurred when writing to file:", e)
