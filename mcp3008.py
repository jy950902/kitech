from spidev import SpiDev
import RPi.GPIO as GPIO
import time

# ADC 컨버터 
class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()

    def open(self):
        self.spi.open(self.bus, self.device)

    def read(self, channel = 0):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def close(self):
        self.spi.close()

LED=16   
pir_s=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(pir_s, GPIO.IN)

adc = MCP3008()

try:
    while True:
        adc_value = adc.read( channel = 0 ) # 조도센서 값 읽어오기
        if GPIO.input(pir_s) == True: # 사람이 pir 센서에 감지되면
            print("Pir On")
            if (adc_value == 0): # 조도센서 값이 0이면 (=>어두우면)
                print("LED ON : PIR %d"%adc_value)
                GPIO.output(LED, True) # 불이 켜짐
                time.sleep(2)
            else:
                print("LED OFF : PIR %d"%adc_value) # 조도센서 값이 0이 아니면 (=>빛이 조금이라도 있으면)
                GPIO.output(LED, False) # 불이 꺼짐
                time.sleep(2)
        else:
            print("Pir Off") # 사람이 감지되지 않음
            GPIO.output(LED, False)


except KeyboardInterrupt:
    adc.close()
    
    
