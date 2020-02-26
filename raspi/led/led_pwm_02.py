# coding: utf-8

import RPi.GPIO as GPIO

import time

# GPIO 핀번호 할당
GPIO.setmode(GPIO.BOARD)

# pin 번호 chanel
LED = 11

# 밝기 목록 ( 0.0 ~ 100 )
dc = [0,1,2,3,4,5,6,7,8,9,10,12,13,15,20,30,50,70,100]

# 핀 설정
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 생성 : 11번 핀, 주파수 100Hz 
p = GPIO.PWM(LED, 100)

import tkinter as tk

window = tk.Tk()

# window size
window.geometry('300x300')

# 변수 설정
led_value = tk.DoubleVar()
led_value.set(0)

p.start(0)

# duty 값을 변경 함수
def change_duty(dc):
    p.ChangeDutyCycle(led_value.get())

# 슬라이드 객체 생성
# 레이블(LED 밝기 조정), 숫자 범위(0 ~ 100)
slide = tk.Scale(window, label='LED 밝기 조정', orient='h', from_=0, to=100, variable=led_value, command=change_duty)

slide.pack()

window.mainloop()


# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
