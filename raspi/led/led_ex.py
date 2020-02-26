# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

#핀 번호로 제어 : 핀 번호 할당 -> 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀 번호 : chanel 번호
LED_W = 11

# 11번 채널(핀번호)을 출력 핀으로 설정, 초기 출력은 로우 레벨
GPIO.setup(LED_W, GPIO.OUT, initial = GPIO.LOW)


# 예외 처리
try:

    # 무한반복
    while 1:
        # 하이레벨 출력 
        GPIO.output(LED_W, GPIO.HIGH)

        # 0.5s 대기
        time.sleep(0.5)

        # 로우 레벨 출력
        GPIO.output(LED_W, GPIO.LOW)

        # 0.5s 대기
        time.sleep(0.5)

# 키보드 예외를 검출
except KeyboardInterrupt:
    pass

# GPIO 개방
GPIO.cleanup()