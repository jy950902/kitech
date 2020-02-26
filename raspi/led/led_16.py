# coding: utf-8

# GPIO 모듈
import RPi.GPIO as GPIO

import time
import tkinter as tk

# 핀 번호 할당으로 처리 : 핀번호 설정 
GPIO.setmode(GPIO.BOARD)

# 핀 번호 설정 : chanel
LED_W = 11
LED_R = 16

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0 False
GPIO.setup(LED_W, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)


print('=====>LED_W:',GPIO.input(LED_W))

def on():
    GPIO.output(LED_W, 1)

def off():
    GPIO.output(LED_W, 0)

def onn():
    GPIO.output(LED_R, 1)

def offf():
    GPIO.output(LED_R, 0)


# 윈도우 객체
window = tk.Tk()
window.geometry('400x400')

# label 객체 생성
label = tk.Label(window, text='버튼을 눌러서 LED 점등을 하세요')

# button 객체 생성
btn = tk.Button(window, text='11 ON', command=on)
btn2 = tk.Button(window, text='11 OFF', command=off)

btn3 = tk.Button(window, text='16 ON', command=onn)
btn4 = tk.Button(window, text='16 OFF', command=offf)

# 위젯 배치 
label.pack()
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()

# 윈도우 출력
window.mainloop()

# GPIO 개방
GPIO.cleanup()