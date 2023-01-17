from machine import Pin
import time

led_r= Pin(15,mode=Pin.OUT,value=0)
led_v = Pin(14,mode=Pin.OUT,value=0)
led_b = Pin(13,mode=Pin.OUT,value=0)
bp1 = Pin(0,mode=Pin.IN,pull=Pin.PULL_UP)
bp2 = Pin(16,mode=Pin.IN,pull=Pin.PULL_UP)
print(bp1.value())
print(bp2.value())

Grr=1
Grv=0
Grb=1

while True:
    if bp2.value()==1:
        
        if bp1.value()==0 and Grr==0:
            led_r.on()
            print("led rouge")
            led_b.off()
            Grr=1
            Grv=0
            time.sleep(0.2)
        
        if bp1.value()==0 and Grv==0:
            led_r.off()
            print("led vert")
            led_v.on()
            Grv=1
            Grb=0
            time.sleep(0.2)
            
        if bp1.value() == 0 and Grb ==0:
            led_r.off()
            led_v.off()
            led_b.on()
            print("led bleu")
            Grb=1
            Grr=0
            time.sleep(0.2)
    else:
        led_r.on()
        print("led bleu")
        led_v.off()
        led_b.off()
        Grr=1
        Grv=0
        Grb=1