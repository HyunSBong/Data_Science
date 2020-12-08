import sys
import urllib.request as req
import urllib.parse as parse

# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print("USAGE: download_kma_argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 아래 주소는 기상청 RSS (지역변수를 지정하면 해당 지역 정보를 보여줌)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL로 인코딩 (여기서 매개변수는 지역번호)
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

# 다운로드
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)