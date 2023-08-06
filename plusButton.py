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





# span 요소의 내용 변경
new_value = '5'
span_element = driver.find_element_by_id('stng_nofpr')
driver.execute_script("arguments[0].innerText = arguments[1];", span_element, new_value)