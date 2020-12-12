'''
YAML 은 들여쓰기를 통해 계층 구조를 표현하는 것이 특징인 데이터 형식입니다.
텍스트 데이터이므로 에디터로 편집이 가능하며 XML보다 간단하고 JSON과 거의 비슷하다.
JSON의 대용으로 사용되기도 하며 애플리케이션 설정 파일을 작성할 때 많이 사용된다.
대표적으로 웹 프레임워크인 Rudy와 PHP의 설정 파일 형식으로 사용되고 있다.

[ 배열 ]
배열을 나타낼 때는 하이픈(-)을 붙이고 한칸의 공백을 추가한다음 작성한다. ex) - banana
이때 공백에 들여쓰기가 있으면 중첩 배열을 표현할 수 있다. 다만 들여쓰기 바로 앞은 빈 요소여야 한다.
ex) - Yellow
    - 
        - Banana
        - Orange
    - Red
    - 
        - Apple
YAML은 플로우 스타일 (한 줄에 표현하는 것) 이 제공되어 이를 이용하면 배열과 해시를 괄호로 표현할 수 있다.
다만 쉼표(,)와 콜론(:) 위에는 반드시 공백이 있어야한다.
ex) name: Taro
        favorites: ["Banana", "Monky"]

[ 여러줄의 문자열 ]
multi line: |
    Hi.
    Hello

[ 해시 ]
자바스크립트의 객체와 같다. <키>:<값>
ex) name: Hyunsu
이때도 들여쓰기로 계층 구조를 표현할 수 있다.
ex) name: Hyunsu
    property:
        age: 21
        color: white

[ 앵커와 별칭(Alias) ]
$<이름> 형태로 변수를 선언하고 *<이름> 형태로 참조한다. 이때 전자를 앵커, 후자를 별칭이라 부른다.
ex) 
color_define:
    - $color1 "#FF0000"
    - $color2 "#00FF00"

frame_color:
    title: *color1
    back: *color2

ex) - name: Hyunsu
      age: 21
      color: white
      favorites:
        - Apple
        - Orange

[ 복합 ]
배열과 해시를 조합하면 복잡한 데이터를 표현할 수 있다.
ex) - name: Hyunsu
      age: 21
      color: white
      favorites:
        - Apple
        - Orange
'''

import yaml

yaml_str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""
data = yaml.load(yaml_str)
# 이름과 가격 출력
for item in data['PriceList']:
    print(item["name"], item["price"])

print()
print("-----------------------------")
print()

# 앵커와 별칭 활용하기
yaml_str = """
# 정의
color_def:
  - &color1 "#FF0000"
  - &color2 "#00FF00"
  - &color3 "#0000FF"
# 별칭 테스트
color:
  title: *color1
  body: *color2
  link: *color3
"""

data = yaml.load(yaml_str)

# 별칭이 전개됐는지 테스트하기
print("title=", data["color"]["title"])
print("body=", data["color"]["body"])
print("link=", data["color"]["link"])