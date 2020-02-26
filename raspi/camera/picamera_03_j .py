# coding: utf-8

import picamera
import time
import datetime

# picamera Object 생성
with picamera.PiCamera() as camera:

    #해상도 설정
    # camera.resolution = (320, 240)

    now = datetime.datetime.now()

    file_name = '{}{}{}{}{}{}.jpg'.format(now)


    camera.start_preview()

    camera.start_recording(output = file_name + '.h264')

    camera.wait_recording(5)

    camera.stop_preview()

    camera.stop_recoding()
