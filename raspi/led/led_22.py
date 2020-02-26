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
LED_T = 22

# 핀 출력 핀으로 등록, 초기 출력은 LOW = 0 False
GPIO.setup(LED_W, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_T, GPIO.OUT, initial=GPIO.LOW)


print('=====>LED_W:',GPIO.input(LED_W))

def on_W():
    GPIO.output(LED_W, 1)

def off_W():
    GPIO.output(LED_W, 0)

def on_R():
    GPIO.output(LED_R, 1)

def off_R():
    GPIO.output(LED_R, 0)

def on_T():
    GPIO.output(LED_T, 1)

def off_T():
    GPIO.output(LED_T, 0)


# 윈도우 객체
window = tk.Tk()
window.geometry('400x400')

# label 객체 생성
label = tk.Label(window, text='버튼을 눌러서 LED 점등을 하세요')

# button 객체 생성
btn = tk.Button(window, text='11 ON', command=on_W)
btn2 = tk.Button(window, text='11 OFF', command=off_W)

btn3 = tk.Button(window, text='16 ON', command=on_R)
btn4 = tk.Button(window, text='16 OFF', command=off_R)

btn5 = tk.Button(window, text='22 ON', command=on_T)
btn6 = tk.Button(window, text='22 OFF', command=off_T)

# 위젯 배치 
label.pack()
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()

# 윈도우 출력
window.mainloop()

# GPIO 개방
GPIO.cleanup()