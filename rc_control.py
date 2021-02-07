import RPi.GPIO as GPIO
from gpiozero import LED
import time


class Rccontrol():
    intermitttentLeft_port = 17
    
    servoPin=12

    
    def servoControl(self , dutycicle = 7.5):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servoPin,GPIO.OUT)
        pwm=GPIO.PWM(self.servoPin,100)
        pwm.start(0)
        time.sleep(0.1)
        pwm.ChangeDutyCycle(dutycicle) # left -90 deg position
        time.sleep(0.1)
        pwm.stop()
        GPIO.cleanup()
        
    
    
        
"""
    def leftIntermittent( doit = True):
        try:
            print(LED_intermitttentLeft.is_lit)

            if doit is True:
                if LED_intermitttentLeft.is_lit is False:
                    doit = False
                    LED_intermitttentLeft.blink()
                    
            else:
                #if LED_intermitttentLeft.is_lit is True:
                    LED_intermitttentLeft.off()
                
            
        except KeyboardInterrupt:
            GPIO.cleanup()
"""