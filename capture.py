from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException



######### 자동방지 풀기 위한 프레임워크##################################
import glob
import CaptchaCracker as cc

def result_img():
    target_img_path = './isT.png'    #타켓 이미지 경로
    img_width = 130 #타켓 이미지 넓이
    img_height = 35 #타켓 이미지 높이
    img_length = 6  #타켓 이미지가 포함한 문자 수
    img_char = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}   #타켓 이미지안에 포함된 문자들
    weights_path = './test_weights2.h5' #학습 결과 가중치 경로
    AM = cc.ApplyModel(weights_path, img_width, img_height, img_length, img_char)   #결과 가중치를 가지는 모델 생성
    pred = AM.predict(target_img_path)  #결과 도출
    return pred

########################로그인 함수##################################

def loginProcess():
    
    # 요소 클릭


    mobile_login_path = '//*[@id="header"]/div[3]/div[1]/a'
    pc_login_path = "//*[@id='header']/div[1]/form/div/a[1]"

    login_button = driver.find_element_by_xpath(pc_login_path)
    login_button.click()


    id = "p12400"
    password = "p1y2h3!@#"

    login_id_input = driver.find_element_by_id('mmberId')
    login_id_input.send_keys(id)


    login_password_input = driver.find_element_by_id('gnrlMmberPssrd')
    login_password_input.send_keys(password)

    login_password_input.send_keys(Keys.RETURN)
    
    
    
#####################메인 페이지 조건 ####################################

def main_selector():
    #지역 선택 온클릭 자바스크립트 동작 실행
    js_script_location = "fn_setRegion('4','대전/충남')"
    driver.execute_script(js_script_location)

    time.sleep(0.5)

    # 장소 선택 온클릭 자바스크립트 동작 실행
    js_script_place = "fn_setRcfcl('ID02030028','(예산군)봉수산자연휴양림')"
    driver.execute_script(js_script_place)

    ###################  날짜 요소 클릭#######################################################################
    ## 테이블 전 div가 이전달  tbody이후 tr은 주 td는 일
    calendar_label = driver.find_element_by_xpath("//div[@class='s_2_calendar input']//label[@for='calPicker']")
    calendar_label.click()


    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="forestCalPicker"]/div[1]/div[1]/div/div/div[2]/table/tbody/tr[2]/td[4]/a').click()
    driver.find_element_by_xpath('//*[@id="forestCalPicker"]/div[1]/div[1]/div/div/div[2]/table/tbody/tr[2]/td[5]/a').click()

    # 날짜 선택 버튼 클릭
    date_button = driver.find_element_by_css_selector('div.cal_button a.defBtn')
    date_button.click()

    ######################인원 수정########################################################

    # span 요소의 내용 변경
    new_value = '10'
    span_element = driver.find_element_by_id('stng_nofpr')
    driver.execute_script("arguments[0].innerText = arguments[1];", span_element, new_value)

    #########################시간 타이머##################################################

    # 현재 시간 초로 변환
    current_time = int(time.time())

    # 목표 시간 설정 (예: 15시 30분)
    target_hour = 12
    target_minute = 54

    # 현재 날짜와 목표 시간을 이용하여 datetime 객체 생성
    current_datetime = datetime.fromtimestamp(current_time)
    target_datetime = current_datetime.replace(hour=target_hour, minute=target_minute, second=0)

    # 대기할 시간 계산
    time_to_wait = (target_datetime - current_datetime).total_seconds()
    if time_to_wait > 0:
        time.sleep(time_to_wait)


    #####################################################################################


    # 조회버튼 클릭
    button = driver.find_element_by_css_selector('div.s_2_btn button')
    button.click()

#####################자동 방지 #####################################

def capCrack():
    captcha_img = driver.find_element_by_id("captchaImg")
    cap_div = driver.find_element_by_xpath('//*[@id="txt"]/div[1]/div[2]/div[2]')

    # 요소 위치로 스크롤 이동
    driver.execute_script("arguments[0].scrollIntoView();", cap_div)


    # 스크린샷 찍기
    captcha_img.screenshot('./isT.png')
    #스크린샷 해독
    solve_code = result_img()

    # 입력
    code_text_form = driver.find_element_by_id('atmtcRsrvtPrvntChrct')
    code_text_form.send_keys(solve_code)
    
    
########################숙소 선택##############################

def selectRoom():
    
    goods_list_area = driver.find_element_by_class_name("goods_list_area")
    list_boxes = goods_list_area.find_elements_by_class_name("list_box")

    for box in list_boxes:
        room_type = box.find_element_by_class_name("opt2").text
        if(room_type.startswith("20/20인실")):
            box.click()
            break

#################################################################

###################main 함수#################################


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
driver.maximize_window()
driver.get('https://www.foresttrip.go.kr/main.do')

#로그인
loginProcess()

time.sleep(0.15)

# 팝업 요소 숨기기
try:
    popup = driver.find_element_by_id("enterPopup6665")  # 팝업 요소를 찾는 방법에 따라 수정
    driver.execute_script("arguments[0].style.display = 'none';", popup)
    #팝업이 있을 경우 팝업 종료하고 메인 페이지 조건 설정
    main_selector()

except NoSuchElementException:
    main_selector() # 팝업이 없을 경우 메인 페이지 조건 설정


#다음 요소가 나올 때까지 wait //대기열 방지

driver.implicitly_wait(300)

time.sleep(0.15)

# 자동 입력 방지 문자 우회
capCrack()


#약관 동의 체크박스 선택
check_box = driver.find_element_by_xpath('//*[@id="arr_01"]')
check_box.click()

# 숙소 선택
selectRoom()


#예약 버튼
driver.execute_script("fn_clickRsrvtRqest();")


time.sleep(0.1)

###########예약 신청하기 위해 엔터##################
###alert = Alert(driver)
###alert.accept()
######################################################