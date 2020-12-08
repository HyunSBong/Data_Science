import requests

r = requests.get("http://api.aoikujira.com/time/get.php")

# 텍스트 형식으로 추출
text = r.text
print(text)

# 바이너리 형식으로 추출
bin = r.content
print(bin)