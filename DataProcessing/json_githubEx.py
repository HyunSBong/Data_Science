'''
JSON(JavaScript Object Notation)은 자바스크립트에서 사용하는 객체 표기 방법을 기반으로 한다. 
그렇다고 해서 자바 스크립트 전용 데이터 형식은 아니며 다양한 소프트웨어와 프로그래밍 언어끼리 데이터를 교환할 때 사용한다.

JSON은 구조가 단순하다는 것이 장점이다. 그래서 수많은 프로그래밍 언어에서 인코딩/디코딩 표준으로 사용하고 API에서도 
JSON 형식으로 데이터를 제공하고 있다.

JSON은 파이썬으로 다루기 간편하다. ->> JSON의 배열과 객체는 각각 파이썬의 리스트와 딕셔너리와 같다.
'''

import urllib.request as req
import os.path, random
import json

url = "https://api.github.com/repositories"
savename = "repo.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, "r", encoding="utf-8"))
'''
또는
s = open(savename, "r", encoding="utf-8").read()
items = json.loads(s)
'''
# 출력
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])