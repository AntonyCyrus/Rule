import requests

rawAmazon = ""
rawApkpure = ""
rawBiliBiliIntl = ""
raw币安交易所 = ""
rawCIBN互联网电视 = ""
rawCableTV = ""
rawCake = ""
rawCrunchyroll = ""
rawCloudflare = ""
rawCryptocurrency = ""
rawDAZN = ""
rawDailymotion = ""
rawDiscoveryPlus = ""
rawDisqus = ""
rawDubox = ""
rawDropbox = ""
raweBay = ""
rawEmojipedia = ""
rawFOXNOW = ""
rawFOXPlus = ""
rawFox = ""
rawGitBook = ""
rawGitHub = ""
rawIMDB = ""
rawiQIYIIntl = ""
rawITV = ""
rawImgur = ""
rawLastFM = ""
rawMEGA = ""
rawMozilla = ""
rawMUBI = ""
rawNTPService = ""
rawOvercast = ""
rawParamountPlus = ""
rawPikPak = ""
rawShopee = ""
rawShopify = ""
rawSpeedtest = ""
rawStarPlus = ""
rawThomsonReuters = ""
rawTikTok = ""
rawTwitch = ""
rawViuTV = ""
rawWeTV = ""
rawWikimedia = ""
rawWikipedia = ""
rawYandex = ""

print("Fetching remote resources")

try:
    rawAFP = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AFP/AFP.yaml").text
    rawAmazon = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Amazon/Amazon.yaml").text
    rawApkpure = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Apkpure/Apkpure.yaml").text
    rawBiliBiliIntl = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BiliBiliIntl/BiliBiliIntl.yaml").text
    raw币安交易所 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Binance/Binance.yaml").text
    rawCIBN互联网电视 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/CIBN/CIBN.yaml").text
    rawCableTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/CableTV/CableTV.yaml").text
    rawCake = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Cake/Cake.yaml").text
    rawCrunchyroll = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Crunchyroll.yaml").text
    rawCloudflare = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Cloudflare/Cloudflare.yaml").text
    rawCryptocurrency = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Cryptocurrency/Cryptocurrency.yaml").text
    rawDAZN = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/DAZN/DAZN.yaml").text
    rawDailymotion = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Dailymotion/Dailymotion.yaml").text
    rawDiscoveryPlus = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/DiscoveryPlus/DiscoveryPlus.yaml").text
    rawDisqus = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disqus/Disqus.yaml").text
    rawDubox = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Dubox/Dubox.yaml").text
    rawDropbox = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Dropbox/Dropbox.yaml").text
    raweBay = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/eBay/eBay.yaml").text
    rawEmojipedia = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Emojipedia/Emojipedia.yaml").text
    rawFOXNOW = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/FOXNOW/FOXNOW.yaml").text
    rawFOXPlus = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/FOXPlus/FOXPlus.yaml").text
    rawFox = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Fox/Fox.yaml").text
    rawGitBook = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitBook/GitBook.yaml").text
    rawGitHub = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitHub/GitHub.yaml").text
    rawIMDB = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/IMDB/IMDB.yaml").text
    rawiQIYIIntl = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/iQIYIIntl/iQIYIIntl.yaml").text
    rawITV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ITV/ITV.yaml").text
    rawImgur = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Imgur/Imgur.yaml").text
    rawLastFM = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/LastFM/LastFM.yaml").text
    rawMEGA = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MEGA/MEGA.yaml").text
    rawMozilla = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Mozilla/Mozilla.yaml").text
    rawMUBI = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/MUBI.yaml").text
    rawNTPService = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/NTPService/NTPService.yaml").text
    rawOvercast = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Overcast/Overcast.yaml").text
    rawParamountPlus = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ParamountPlus/ParamountPlus.yaml").text
    rawPikPak = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PikPak/PikPak.yaml").text
    rawShopee = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Shopee/Shopee.yaml").text
    rawShopify = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Shopify/Shopify.yaml").text
    rawSpeedtest = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Speedtest/Speedtest.yaml").text
    rawStarPlus = requests.get("https://raw.githubusercontent.com/HotKids/Rules/master/Clash/RuleSet/Star%2B.yaml").text
    rawThomsonReuters = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ThomsonReuters/ThomsonReuters.yaml").text
    rawTikTok = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok.yaml").text
    rawTwitch = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitch/Twitch.yaml").text
    rawViuTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ViuTV/ViuTV.yaml").text
    rawWeTV = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/WeTV/WeTV.yaml").text
    rawWikimedia = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikimedia/Wikimedia.yaml").text
    rawWikipedia = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikipedia/Wikipedia.yaml").text
    rawYandex = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Yandex/Yandex.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

print("Processing fetched resources and writing to file")

result = ['payload:']
for rawresult in [rawAmazon, rawApkpure, rawBiliBiliIntl, raw币安交易所, rawCIBN互联网电视, rawCableTV, rawCake, rawCrunchyroll, rawCloudflare, rawCryptocurrency, rawDAZN, rawDailymotion, rawDiscoveryPlus, rawDisqus, rawDubox, rawDropbox, raweBay, rawEmojipedia, rawFOXNOW, rawFOXPlus, rawFox, rawGitBook, rawGitHub, rawIMDB, rawiQIYIIntl, rawITV, rawImgur, rawLastFM, rawMEGA, rawMozilla, rawMUBI, rawNTPService, rawOvercast, rawParamountPlus, rawPikPak, rawShopee, rawShopify, rawSpeedtest, rawStarPlus, rawThomsonReuters, rawTikTok, rawTwitch, rawViuTV, rawWeTV, rawWikimedia, rawWikipedia, rawYandex]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/GlobalMedia.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
