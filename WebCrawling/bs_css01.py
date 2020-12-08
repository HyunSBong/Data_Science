from bs4 import BeautifulSoup 
html = """
<html><body>
<div id="meigen">
  <h1>크롤링 공부중</h1>
  <ul class="items">
    <li>크롤링입문</li>
    <li>머신러닝도</li>
    <li>딥러닝도</li>
  </ul>
</div>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
# 필요한 부분을 CSS 쿼리로 추출
# 타이틀 부분 추출 
# <div id="meigen">에서 h1까지
h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)

# 목록 부분 추출
# <ul class="items">에서 li까지
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
  print("li =", li.string)