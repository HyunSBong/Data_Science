from bs4 import BeautifulSoup 

fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

'''
books.html 의 상세내용은 다음과 같음 

<ul id="bible">
    <li id="ge">Genesis</li>
    <li id="ex">Exodus</li>
    <li id="le">Leviticus</li>
    <li id="nu">Numbers</li>
    <li id="de">Deuteronomy</li>
  </ul>

'''
# CSS 선택자로 검색하는 다양한 방법

sel = lambda q : print(soup.select_one(q).string)
sel("#nu")  # id  속성이 nu 인 것을 추출
sel("li#nu")  #  <li> 태그 추가
sel("ul > li#nu")  # <ul> 태그의 자식이라는 것을 지정
sel("#bible #nu")  #  id 속성을 사용해 #bible 아래의 #nu 선택
sel("#bible > #nu")  # 23번 코드처럼 부모 자식 관계에 있음을 나타냄
sel("ul#bible > li#nu")  # id가 bible인 <nu>태그 바로 아래에 있는 id가 nu인 <li>태그를 선택
sel("li[id='nu']")  # 속성 검색으로 id가 nu인 <li>태그를 지정하는 것
sel("li:nth-of-type(4)")  # 4 번째 <li>태드 추출
# 그 밖의 방법
print(soup.select("li")[3].string)   # li 태그 모두 추출
print(soup.find_all("li")[3].string) # 위와 동일