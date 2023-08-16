from gpiozero import MotionSensor, LED
from time import sleep

pir = MotionSensor(4)
led = LED(26)

led.off()
print("waiting for PIR sattle")
pir.wait_for_no_motion()
sleep(5)

while True:
    print("Ready")
    pir.wait_for_motion()
    print("motiondetected")
    led.on()
    sleep(3)
    led.off()
