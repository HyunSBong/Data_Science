from urllib.parse import urljoin

# 첫 번째 매개변수로 기본 url, 두 번째 매개변수로 상대 경로를 지정
# 만약 상대 경로(path)가 http://등으로 시작한다면 기본 url(base)을 무시하고
# 두 번째 매개변수에 지정한 url을 리턴함 

base = "http://example.com/html/a.html"

print( urljoin(base, "/hoge.html") )
print( urljoin(base, "http://otherExample.com/wiki") )
print( urljoin(base, "//anotherExample.org/test") )