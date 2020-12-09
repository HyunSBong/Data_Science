import requests
import json

apikey = "None"
cities = ["Seoul,KR"]
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 켈빈 온도를 섭씨 온도로 변환 (OpenWeatherMap의 api 가이드 참고)
k2c = lambda k: k - 273.15


for name in cities:
    url = api.format(city=name, key=apikey)
    # api에 요청
    r = requests.get(url)

    # JSON 형식으로 받기
    data = json.loads(r.text)    
    
    print("+ 도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print("| 습도 =", data["main"]["humidity"])
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"])
    print("")