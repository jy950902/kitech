# coding: utf-8

# GPIO 모듈
import RPi.GPIO as GPIO

import time
import tkinter as tk

# 핀 번호 할당으로 처리 : 핀번호 설정 
GPIO.setmode(GPIO.BOARD)

# 핀 번호 설정 : chanel
LED_W = 11

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0 False
GPIO.setup(LED_W, GPIO.OUT, initial=GPIO.LOW)


print('=====>LED_W:',GPIO.input(LED_W))

def func():
    GPIO.output(LED_W, not GPIO.input(LED_W))
    time.sleep(3)

func()
print('=====>LED_W:',GPIO.input(LED_W))

GPIO.cleanup()