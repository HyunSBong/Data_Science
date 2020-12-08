import urllib.request
# URL과 저장 경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
# urlretrieve() 모듈을 이용해 파일 다운로드
urllib.request.urlretrieve(url, savename)
print("저장되었습니다.")

# urlopen() 함수를 사용하면 데이터를 곧바로 파이썬 메모리 위에 올릴 수 있음
# --> 변수에 저장하는 것이 가능하는 것
# urlopen() 함수로 url 리소스를 열고 read() 메소드로 데이터 읽기
temp = urllib.request.urlopen(url).read()
# open() 함수로 파일을 여는데 이때, 파일을 읽고 쓰기 모드를 나타내는 mode로 염
with open(savename, mode="wb") as f: # w는 쓰기모드, b는 바이너리 모드
    f.write(temp) # write() 메소드로 다운로드한 바이너리 데이터를 파일에 저장하였음
    print("저장되었습니다.")