import requests
import pytz
from datetime import datetime

result = []

# 定义需要请求的链接
urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Amazon/Amazon.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Apkpure/Apkpure.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/BiliBiliIntl/BiliBiliIntl.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Binance/Binance.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/CIBN/CIBN.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/CableTV/CableTV.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Cake/Cake.list",
    "https://raw.githubusercontent.com/HotKids/Rules/master/Surge/RULE-SET/Crunchyroll.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Cloudflare/Cloudflare.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Cryptocurrency/Cryptocurrency.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/DAZN/DAZN.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Dailymotion/Dailymotion.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/DiscoveryPlus/DiscoveryPlus.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Disqus/Disqus.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Dubox/Dubox.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Dropbox/Dropbox.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/eBay/eBay.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Emojipedia/Emojipedia.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/FOXNOW/FOXNOW.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/FOXPlus/FOXPlus.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Fox/Fox.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GitBook/GitBook.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/GitHub/GitHub.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/IMDB/IMDB.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/iQIYIIntl/iQIYIIntl.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/ITV/ITV.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Imgur/Imgur.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/LastFM/LastFM.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/MEGA/MEGA.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Mozilla/Mozilla.list",
    "https://raw.githubusercontent.com/HotKids/Rules/master/Surge/RULE-SET/MUBI.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/NTPService/NTPService.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Overcast/Overcast.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/ParamountPlus/ParamountPlus.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/PikPak/PikPak.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Shopee/Shopee.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Shopify/Shopify.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Speedtest/Speedtest.list",
    "https://raw.githubusercontent.com/HotKids/Rules/master/Surge/RULE-SET/Star%2B.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/ThomsonReuters/ThomsonReuters.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/TikTok/TikTok.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Twitch/Twitch.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/ViuTV/ViuTV.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/WeTV/WeTV.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Wikimedia/Wikimedia.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Wikipedia/Wikipedia.list"
]

# 遍历链接列表，依次请求链接内容并将结果保存到 result 列表中
for url in urls:
    try:
        raw = requests.get(url).text
        result.extend([item for item in raw.split("\n") if item.strip() and not item.startswith('#')])
    except requests.exceptions.RequestException as e:
        print("Error getting data:", e)

# 获取当前时间并格式化
tz = pytz.timezone('Asia/Shanghai')
now = datetime.now(tz)
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# 拼接要写入文件的字符串
result_text = "# GlobalMedia.list\n# Generated at " + time_str + "\n\n" + "\n".join(result) + "\n\n# This configuration file has been generated successfully."

# 将字符串写入文件
with open("./Loon/GlobalMedia.list", "w", encoding="utf-8") as f:
    f.write(result_text)
