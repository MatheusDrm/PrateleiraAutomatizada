import RPi.GPIO as GPIO # Controle dos motores 
import time # Obter tempo de execução
import sys


class motor():
    def __init__(self, In1, In2):

        self.In1 = In1
        self.In2 = In2

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.In1, GPIO.OUT) #in1 enable 
        GPIO.setup(self.In2, GPIO.OUT) #in2
    
    def move(self, dir=True,t=0): #Direção True -> Ir para frente e False ir para trás
        GPIO.output(self.In1, dir)
        GPIO.output(self.In2, not dir)
        # time.sleep(t)

    def fast_stop(self, t=0):
        GPIO.output(self.In1, 0)
        GPIO.output(self.In2, 0)
        # time.sleep(t)

    def brake(self, t=0):
        GPIO.output(self.In1, 1)
        GPIO.output(self.In2, 1)
        # time.sleep(t)

