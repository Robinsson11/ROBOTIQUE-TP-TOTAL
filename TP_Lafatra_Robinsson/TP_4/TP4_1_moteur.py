import machine
from machine import Pin
from machine import PWM
import time

IN1 = Pin(0, Pin.OUT)
IN2 = Pin(1, Pin.OUT)    
ENA = Pin(2, Pin.OUT)

def sens1():
    ENA.on()
    IN1.on()               
    IN2.off()               
    print('sens 1')
def sens2():
    ENA.on()
    IN1.off()
    IN2.on()
    print('sens 2')
    time.sleep_ms(10000)
    demarre()
def demarre():
    sens1()
    time.sleep_ms(10000)
    sens2()
demarre()
