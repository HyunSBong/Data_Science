from bs4 import BeautifulSoup 

fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# html에서 아보카도 추출해보기
# CSS 선택자로 추출 
print(soup.select_one("li:nth-of-type(8)").string)  # 모든 <li>태그 중에서 8번째 요소 추출
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)  # id가 ve-list인 요소 바로 아래에 있는 <li>태그 중에 4번째 요소를 추출
print(soup.select("#ve-list > li[data-lo='us']")[1].string)  # select()메소드를 사용해 id가 ve-list인 요소 바로 아래에 있는 <li>태그 중에서 
                                                             # data-li속성이 "us"인 것을 모두 추출하고 그중에서 선택
print(soup.select("#ve-list > li.black")[1].string)  # select()메소드를 사용해 class 속성이 "black"인 요소 가운데 인덱스1번째 요소를 선택

# find 메서드로 추출 - 여러 개의 조건을 한 번에 지정할 수 있음!!!
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)

# find 메서드를 연속적으로 사용 - 정밀 탐색 가능
print(soup.find(id="ve-list")
           .find("li", cond).string)