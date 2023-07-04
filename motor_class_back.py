import RPi.GPIO as GPIO # Controle dos motores 
import time # Obter tempo de execução
import sys

class motor():
    def __init__(self, In1, In2, pwm_pin,):

        self.In1 = In1
        self.In2 = In2
        self.pwm_pin = pwm_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.In1, GPIO.OUT) #in1
        GPIO.setup(self.In2, GPIO.OUT) #in2
        GPIO.setup(self.pwm_pin, GPIO.OUT) # pin enable

        self.pwm = GPIO.PWM(self.pwm_pin, 100)
        self.pwm.start(0)
    
    def move(self, dir=True, vel=50, t=0): #Direção true -> Ir para frente
        GPIO.output(self.In1, dir)
        GPIO.output(self.In2, not dir)
        self.pwm.ChangeDutyCycle(vel)
        time.sleep(t)

    def stop(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        time.sleep(t)
