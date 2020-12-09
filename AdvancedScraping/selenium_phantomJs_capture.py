'''
Selenium은 주로 웹앱을 테스트하는데 이용하는 프레임워크다. 
webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어하게 된다.
브라우저를 직접 동작시킨다는 것은 JavaScript를 이용해 비동기적으로 혹은 뒤늦게 불러와지는 컨텐츠들을 가져올 수 있다는 것이다. 
즉, '눈에 보이는' 컨텐츠라면 모두 가져올 수 있다는 뜻이다. 
requests에서 사용했던 .text의 경우 브라우저에서 '소스보기'를 한 것과 같이 동작하여, JS등을 통해 동적으로 DOM이 변화한 이후의 HTML을 보여주지 않는다. 
반면 Selenium은 실제 웹 브라우저가 동작하기 때문에 JS로 렌더링이 완료된 후의 DOM결과물에 접근이 가능하다.
'''

from selenium import webdriver

url = "https://www.naver.com/"

# 다운로드 받은 크롬 드라이버의 위치 지정
driver = webdriver.Chrome('/Users/hyunsubong/Developer/chromedriver')
# PhantopmJS의 위치 지정도 동일
# driver = webdriver.PhantomJS('/usr/local/Caskroom/phantomjs/2.1.1/phantomjs-2.1.1-macosx/bin/phantomjs')

# Selenium은 기본적으로 웹 자원들이 모두 로드될때까지 기다려주지만, 
# 암묵적으로 모든 자원이 로드될때 까지 기다리게 하는 시간을 직접 implicitly_wait을 통해 지정할 수 있다.
driver.implicitly_wait(3)

driver.get(url)
driver.save_screenshot("naver_screenShot.png")

driver.quit()