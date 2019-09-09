from machine import Pin, ADC, PWM
from time import sleep

led = PWM(Pin(5), freq=5000)

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

while True:
    print(ldr.read())
    sleep(0.1)
    led.duty(1023 - (ldr.read()//4))




