from selenium import webdriver
'''

네이버에서 selenium을 이용한 로그인을 차단함
다른 방법을 찾아야함

'''
naver_id = "--"
naver_pw = "--"

driver = webdriver.Chrome('/Users/hyunsubong/Developer/chromedriver')

# 로그인 페이지에 접근
print("----네이버 페이 웹페이지에 로그인을 시도합니다.-----")
url_login = "https://nid.naver.com/nidlogin.login"
driver.get(url_login)

# 로그인
input_id = driver.find_element_by_css_selector("#id")
input_pw = driver.find_element_by_css_selector("#pw")

input_id.send_keys(naver_id)
input_pw.send_keys(naver_pw)

login_btn = driver.find_element_by_css_selector("#log\.login")
login_btn.click()
driver.implicitly_wait(3)

# 자동입력 방지문자를 사용자가 직접 입력하기 위해 1분동안 대기
print("------------------로그인 성공!----------------------")
driver.implicitly_wait(60)

input_pw = driver.find_element_by_css_selector("#pw")
login_btn = driver.find_element_by_css_selector("#l5f\.login")
login_btn.click()
print("------------------로그인 성공!----------------------")

# 결제내역 페이지의 데이터 가져오기
url_payList = "https://order.pay.naver.com/home"
driver.get(url_payList)
print("-------------결제내역 페이지로 이동합니다.---------------")
driver.implicitly_wait(3)

# 쇼핑 목록 출력하기
products2 = driver.find_elements_by_css_selector(".p_info span")
products = driver.find_elements_by_css_selector("#_rowLi20201203013850CHK2020120378792631 > div.goods_item > div > a > p")
print("---------------결제내역을 불러왔습니다.----------------")
print()
for product in products:
  print("--> ", product.text)