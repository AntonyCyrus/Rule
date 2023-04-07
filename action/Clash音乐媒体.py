import requests

rawDeezer = ""
rawQobuz = ""
rawSpotify = ""
rawTIDAL = ""
try:
    rawDeezer = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Deezer/Deezer.yaml").text
    rawQobuz = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Qobuz/Qobuz.yaml").text
    rawSpotify = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Spotify/Spotify.yaml").text
    rawTIDAL = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TIDAL/TIDAL.yaml").text
except requests.exceptions.RequestException as e:
    print("Error occurred when requesting remote resources:", e)

result = ['payload:']
for rawresult in [rawDeezer, rawQobuz, rawSpotify, rawTIDAL]:
    result.extend([item.rstrip() for item in rawresult.split('\n') if not (item.startswith('#') or item.startswith('payload:'))])
result_text = '\n'.join(result)

try:
    with open("./Clash/Music.yaml", "w") as f:
        f.write(result_text)
except IOError as e:
    print("Error occurred when writing to file:", e)
