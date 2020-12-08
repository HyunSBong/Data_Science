import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "--"
PASSWORD = "--"
# 세션 시작
session = requests.session()
# 로그인
login_info = {
    "m_id": USER, # 변수명은 페이지 소스 참고
    "m_passwd": PASSWORD
}

# 개발자도구의 Network에서 분석해본 결과 로그인과 관련된 기능을 처리하는 곳은 login_proc.php
# Request URL 또한 http://www.hanbit.co.kr/member/login_proc.php  이곳에 전달하면 로그인을 할 수 있다

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # 오류가 발생하면 예외가 발생

print("----로그인 성공----")

# 마이페이지에 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html" 
res = session.get(url_mypage)
res.raise_for_status()

print("----접근 성공----")

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, "html.parser")

#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span
mileage = soup.select_one("dl.mileage_section1 > dd > span").get_text()
# mileage = soup.find('dl', 'mileage_section1')
print("----마일리지 가져오기 성공----")

#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span
ecoin = soup.select_one("dl.mileage_section2 > dd > span").get_text()
print("----이코인 가져오기 성공----")
print()
print("마일리지: " + mileage)
print("이코인: " + ecoin)

'''

<div class="w940 wrap_member">
		<!-- 로그인 영역 -->	
		<form name="frm"  id="frm"  action="#" method="post">
		<input name="retun_url" id="retun_url" type="hidden" value="" class="i_text" size="100" >
		<div class="login_left">		
			<fieldset>
				<legend>한빛출판네트워크 로그인</legend>
				
				<label class="i_label" for="login_id"><strong></strong>
					<input name="m_id" id="m_id" type="text" value="" class="i_text" placeholder="아이디" onkeydown="javascript:if(event.keyCode==13){login_proc(); return false;}">
				</label> 

				<label class="i_label" for="login_pw"><strong></strong>
					<input name="m_passwd"  id="m_passwd" type="password" value="" class="i_text" placeholder="비밀번호" onkeydown="javascript:if(event.keyCode==13){login_proc(); return false;}">
				</label>
				
				<label>
					<input  type="button" name="login_btn"  id="login_btn" value="로그인" class="btn_login" >					
				</label>
				
				<label class="i_label2">
					<input type="checkbox" name="keepid" id="keepid" value="1" class="i_check"><strong>아이디 저장</strong>
				</label>
			</fieldset>
			
			<ul class="login_btn">
				<li><a href="https://www.hanbit.co.kr/member/find_id.html" class="btn_idc">아이디 찾기</a></li>
				<li><a href="https://www.hanbit.co.kr/member/find_pw.html" class="btn_pwc">비밀번호 찾기</a></li>
				<li><a href="https://www.hanbit.co.kr/member/member_agree.html" class="btn_joinc">회원가입</a></li>
			</ul>
		</div>
		</form>
		<!-- //로그인 영역 -->

'''

'''

<!-- Contents -->
<div id="container">

	<div class="myhanbit_wrap">
		<!-- 회원등급 -->
		<div class="sm_myinfo">
			<div class="my_rating">
				<div class="icon">
										
					<img src="https://www.hanbit.co.kr/images/myhanbit/rating_icon1.png" alt="" />	
				</div>
				<p>(홍길동)님의<br />회원 등급은 <span>일반</span> 입니다.</p>				
			</div>
		</div>
		<!-- //회원등급 -->
		
		<!-- 마일리지/이코인 -->
		<div class="sm_mymileage">
			<dl class="mileage_section1">
				<dt>마일리지</dt>
				<dd><span>3,000</span> 점</dd>
			</dl>
			<dl class="mileage_section2">
				<dt>한빛이코인</dt>
				<dd><span>0</span> 원</dd>
			</dl>
		</div>
		<!-- //마일리지/이코인 -->

'''