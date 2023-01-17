from machine import ADC, Pin
import time

adc_0 = ADC(Pin(26))
adc_1 = ADC(Pin(27))
bp = Pin(16,Pin.IN, Pin.PULL_UP)

while (True):
    print(adc_0.read_u16())
    print(adc_1.read_u16())
    print('   ')
    time.sleep_ms(1000)