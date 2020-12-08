from bs4 import BeautifulSoup 
import re # 정규 표현식 사용

html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")

# 정규 표현식으로 href에서 https 프로토콜로 통신하는 링크인 것만을 추출
li = soup.find_all(href=re.compile(r"^https://")) # compile은 정규 표현식의 함수
for e in li: print(e.attrs['href']) # href 속성