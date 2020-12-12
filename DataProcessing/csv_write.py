'''
csv.reader 객체를 생성하려면 open() 함수의 리턴 값에 있는 파일 포인터를 사용하면된다. 
옵션으로 delimiter(구분 문자), quotechar(어떤 기호로 데이터를 감싸고 있는지)를 지정할 수 있다. 
따라서 TSV처럼 다른 특수 문자 형식으로 구분돼 있어도 데이터를 쉽게 읽는 것이 가능하다. 
그리고 데이터를 하나씩 읽을 때는 for 반복문을 사용합니다. 
데이터를 한 줄 한 줄 읽어 들이는 방식이므로 큰 CSV 파일이라도 필요한 곳까지 점진적으로 읽을 수 있다. 

이어서 CSV 파일을 쓸 때는 csv.writer를 사용한다.
csv.writer를 초기화할 때는 open()메소드의 리턴값인 파일 포인터와 delimiter(구분 문자)등을 지정한다.
이후에 writerow() 메소드로 한 줄씩 데이터를 쓰면된다.
'''
import csv
import codecs

with codecs.open("test.csv", "w", "euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["1000", "유선키보드", "10000"])
    writer.writerow(["1002", "무선마우스", "30000"])