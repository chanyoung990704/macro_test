from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys




options = webdriver.ChromeOptions()



# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 위치 경로 입력
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get('https://www.foresttrip.go.kr/main.do')



###################로그인 ############################

# 요소 클릭
login_button = driver.find_element_by_xpath('//*[@id="header"]/div[3]/div[1]/a')
login_button.click()


id = "p12400"
password = "p1y2h3!@#"

login_id_input = driver.find_element_by_id('mmberId')
login_id_input.send_keys(id)


login_password_input = driver.find_element_by_id('gnrlMmberPssrd')
login_password_input.send_keys(password)

login_password_input.send_keys(Keys.RETURN)



#######################################################


time.sleep(0.3)

########################################################


#지역 선택 온클릭 자바스크립트 동작 실행
js_script_location = "fn_setRegion('4','대전/충남')"
driver.execute_script(js_script_location)

time.sleep(0.5)

# 장소 선택 온클릭 자바스크립트 동작 실행
js_script_place = "fn_setRcfcl('ID02030028','(예산군)봉수산자연휴양림')"
driver.execute_script(js_script_place)

# 날짜 요소 클릭
## 테이블 전 div가 이전달  tbody이후 tr은 주 td는 일
calendar_label = driver.find_element_by_xpath("//div[@class='s_2_calendar input']//label[@for='calPicker']")
calendar_label.click()


time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="forestCalPicker"]/div[1]/div[1]/div/div/div[2]/table/tbody/tr[3]/td[4]/a').click()
driver.find_element_by_xpath('//*[@id="forestCalPicker"]/div[1]/div[1]/div/div/div[2]/table/tbody/tr[3]/td[5]/a').click()

# 날짜 선택 버튼 클릭
date_button = driver.find_element_by_css_selector('div.cal_button a.defBtn')
date_button.click()

# 인원 수정

# span 요소의 내용 변경
new_value = '5'
span_element = driver.find_element_by_id('stng_nofpr')
driver.execute_script("arguments[0].innerText = arguments[1];", span_element, new_value)


# 조회버튼 클릭
button = driver.find_element_by_css_selector('div.s_2_btn button')
button.click()

################################################################