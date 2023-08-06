from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
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

# 창 최대화
driver.get('https://www.naver.com')
output_filename = "captcha_image.png"  # 저장될 파일명

    
def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    
    
    
    

try:
    # 캡챠 이미지 요소 찾기
    captcha_img = driver.find_element_by_xpath('//*[@id="account"]/div')
    driver.execute_script("arguments[0].scrollIntoView();", captcha_img)




finally:
    # 웹 드라이버 종료
    driver.quit()        
    
    
    