# IP주소, UserAgent 등의 클라이언트 접속 정보 출력
import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
# 바이너리를 문자열로 변환
text = data.decode("utf-8")
print(text)