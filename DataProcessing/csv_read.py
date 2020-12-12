'''
[ CSV/TSV ]
CSV/TSV 는 앱에서 굉장히 사용되며 XML보다도 많이 사용되고 있다. 
구조가 굉장히 단순하고 역설로 쉽게 만들 수 있으며, 수많은 데이터베이스와 데이터 도구 등에서 CSV 형식을 지원하고 있기 때문이다. 
CSV(Comma. -Separated Values) 파일은 각 필드를 쉽표로 구분한다. 
기본적으로 텍스트 파일이므로 텍스트 에디터를 사용해 간편하게 수정할 수 있으며 
다양한 스프레드시트 소프트웨어, 전화번호부, 데이터베이스 등이 데이터 교환에 CSV 파일을 사용하고 있다.  

CSV와 비슷하지만 쉽표가 아닌 탭으로 필드를 구분하는 TSV(Tab-Separated Values), 
공백으로 필드를 구분하는 SSV(Space-Separated Values) 등도 사용되고 있습니다. 
참고로 구분 기호만 다르고 형식이 거의 차이가 없기 때문에 CSV 형식이라고 말할 때 문맥에 따라 TSV와 SSV 등을 모두 포함하는 경우도 있다.

단순한 데이터를 다룰 때는 줄바꿈과 쉼표로만 구분하면 되지만 큰따옴표가 포함되는 등의 복잡한 데이터를 다룰 때는 csv모듈을 사용하는 것이 좋다.
[ 구조 ]
CSV파일은 1개 이상의 레코드로 구성되며 레코드는 줄바꿈으로 구분된다.
또, 각각의 레코드들은 같은 구성을 가지며 각각 1개 이상의 필드로 구성된다.
이때 각 필드는 쉼표(,)로 구분된다. 첫번쨰 레코드는 헤더로 사용될 수도 있다.
필드 내부에 따옴표를 붙일 수도 있으며 따옴표를 표시하고 싶다면 ""또는 ''으로 표기하면된다.
ex) ID,이름,가격
    1000,비누,300
    "1001","장갑","150"
    "1002","제주에서 온 ""삼다수"","300"
'''

import csv
import codecs

# EUC_KR로 저장된 CSV 파일 읽기
filename = "list-euckr.csv"
csv = codecs.open(filename, "r", "euc_kr").read() # 인코딩 방식에 주의

# CSV을 파이썬 리스트로 변환하기
data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)

# 결과 출력하기
for c in data:
    print(c[1], c[2])

# 한 줄씩 읽어 들이기
reader = csv.reader(csv, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])