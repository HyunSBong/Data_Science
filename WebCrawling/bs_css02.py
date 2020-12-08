from urllib.parse import urljoin

# 기본 url을 기반으로 상대 경로를 절대 경로로 변환

base = "http://example.com/html/a.html"

print( urljoin(base, "b.html") )
print( urljoin(base, "sub/c.html") )
print( urljoin(base, "../index.html") )
print( urljoin(base, "../img/hoge.png") )
print( urljoin(base, "../css/hoge.css") )

# 첫 번째 매개변수로 기본 url, 두 번째 매개변수로 상대 경로를 지정
# 만약 상대 경로(path)가 http:// 등으로 시작한다면 기본 url(base)을 무시하고
# 두 번째 매개변수에 지정한 url을 리턴함 
print()
print("---------")
base = "http://example.com/html/a.html"

print( urljoin(base, "/hoge.html") )
print( urljoin(base, "http://otherExample.com/wiki") )
print( urljoin(base, "//anotherExample.org/test") )