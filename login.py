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