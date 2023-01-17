from machine import Pin
import time
import ultrasonic

trig = 0
echo = 1

sensor = ultrasonic.Ultrasonic(trig, echo)

while True:
    try:
        dist = sensor.distance_in_cm()
        print("Dist = {}".format(dist))

    except ultrasonic.MeasurementTimeout as e:
        print("{}".format(e))
    time.sleep(1)