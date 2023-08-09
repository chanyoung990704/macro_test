import time
from datetime import datetime, timedelta


current_time = time.localtime()
target_hour = 21
target_minute = 31

print(current_time)

# 현재 시간 초로 변환
current_time = int(time.time())

# 목표 시간 설정 (예: 15시 30분)
target_hour = 21
target_minute = 32

# 현재 날짜와 목표 시간을 이용하여 datetime 객체 생성
current_datetime = datetime.fromtimestamp(current_time)
target_datetime = current_datetime.replace(hour=target_hour, minute=target_minute, second=0)

# 대기할 시간 계산
time_to_wait = (target_datetime - current_datetime).total_seconds()
if time_to_wait > 0:
    time.sleep(time_to_wait)