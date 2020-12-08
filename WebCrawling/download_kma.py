import urllib.request
import urllib.parse

# 아래 주소는 기상청 RSS (지역변수를 지정하면 해당 지역 정보를 보여줌)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL로 인코딩 (여기서 매개변수는 지역번호)
values = {
    'stnId': '133' # 충청남도
}
params = urllib.parse.urlencode(values)

# 요청 전용 URL 생성 (여러 개의 매개변수를 사용할 때는 & 으로 구분)
url = API + "?" + params
print("url= ", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)