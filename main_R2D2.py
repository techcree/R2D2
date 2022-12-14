#LED for R2D2 by TechCree 838375
import machine
from machine import Pin
import utime
from machine import Pin, PWM

led25 = Pin(25, Pin.OUT) #mainboard led
led1 = Pin(1, Pin.OUT) #rot
led2 = Pin(2, Pin.OUT) #blau
led3 = Pin(3, Pin.OUT) #gruen

MID = 1100000
MIDB = 1500000

MIN = 300000
MINB = 350000

MAX = 2200000
MAXB = 2500000

pwm = PWM(Pin(15))
pwm.freq(50)
pwm.duty_ns(MID)

while True:
    #servo
    pwm.duty_ns(MAX)
    utime.sleep(1)
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(2)
        
    #led
    #Reset all LED
    led25.value(1)
    led1.value(0) #rot aus
    led2.value(0) #blau aus
    led3.value(0) #gruen aus
    #start sequence
    led1.value(1) #rot an
    utime.sleep(0.5)
    led1.value(0) #rot aus
    utime.sleep(0.3)
    led1.value(1) #rot an
    utime.sleep(0.8)
    led2.value(1) #blau an
    utime.sleep(0.5)
    led3.value(1) #gruen an
    led2.value(0) #blau aus
    utime.sleep(0.3)
    led3.value(0) #gruen aus
    utime.sleep(0.3)
    led3.value(1) #gruen an
    utime.sleep(0.3)
    led3.value(0) #gruen aus
    utime.sleep(0.8)
    led1.value(0) #rot aus
    led2.value(1) #blau an
    utime.sleep(1)
    led1.value(0) #rot aus
    led2.value(0) #blau aus
    utime.sleep(0.3)
    led1.value(1) #rot an
    utime.sleep(0.3)
        
    #servoB
    pwm.duty_ns(MAXB)
    utime.sleep(1)
    pwm.duty_ns(MINB)
    utime.sleep(1)
    pwm.duty_ns(MIDB)
    utime.sleep(2)
    
    led1.value(0) #rot aus
    utime.sleep(0.3)
    led3.value(1) #gruen an
    utime.sleep(0.3)
    led3.value(0) #gruen aus
    led1.value(1) #rot an
    utime.sleep(0.3)
    led1.value(0) #rot aus
    utime.sleep(0.3)
    led3.value(1) #gruen an
    utime.sleep(0.3)
    led3.value(0) #gruen aus
    led2.value(1) #blau an
    utime.sleep(0.3)
    led2.value(0) #blau aus