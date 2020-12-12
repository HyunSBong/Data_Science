from bs4 import BeautifulSoup 
import urllib.request as req
import os.path
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "kma_forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser') 
# html.parser는 HTML을 분석하기 위해 만들어졌는데 그래서 XML데이터의 태그가 대문자라 하더라도 소문자로 변환해버린다.
# 따라서 요소에 접근할 때는 반드시 태그 이름을 소문자로 입력해서 사용해야한다.
# 지역확인
info = {}
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)
# 각 지역의 날씨를 구분해서 출력
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("| - ", name)