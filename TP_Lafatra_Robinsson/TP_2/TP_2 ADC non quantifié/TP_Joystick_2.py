from machine import ADC, Pin
import time

adc_0 = ADC(Pin(26))
adc_1 = ADC(Pin(27))
bp = Pin(16,Pin.IN, Pin.PULL_UP)

while True:
    xValue = adc_0.read_u16()
    yValue = adc_1.read_u16()
    buttonValue = bp.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    if xValue <= 600:
        xStatus = "left"
    elif xValue >= 60000:
        xStatus = "right"
    if yValue <= 600:
        yStatus = "up"
    elif yValue >= 60000:
        yStatus = "down"
    if buttonValue == 0:
        buttonStatus = "pressed"
    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    time.sleep_ms(2000)
