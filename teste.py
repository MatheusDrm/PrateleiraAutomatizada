import RPi.GPIO as GPIO # Controle dos motores 
import time # Obter tempo de execução
import sys
from motor_class import motor

class teste():

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        self.sensor_configuration()
        # Configurando os motores
        self.motorX = motor(2,3)
        self.motorY = motor(17,27)
        self.motorZ = motor(10,9)


    def calibration_x(self):

        print("Iniciando calibração em x")
        tempo_inicial = time.time()
        self.motorX.move(True)
        while (self.sensorX2_state != 1):
            time.sleep(0.1)  # Tempo de espera entre as leituras do sensor 
        print("Tocou no sensox2")
        self.motorX.fast_stop()
        tempo_final = time.time()
        tempo_decorrido = tempo_final - tempo_inicial
        self.tx = tempo_decorrido/6 #compartimento 1 -> tx ;  compartimento 2 -> 3tx ; compartimento 5 -> 5tx
        print(f"Tempo decorrido: {tempo_decorrido} segundos")

        # Voltar para posição inicial
        self.motorX.move(False)
        while(self.sensorX1_state !=1):
            time.sleep(0.1)
        self.motorX.fast_stop()

    def sensor_configuration(self):

        self.sensorX1_pin = 5
        self.sensorX2_pin = 6
        self.sensorY1_pin = 13
        self.sensorY2_pin = 19
        self.sensorZ1_pin = 23
        self.sensorZ2_pin = 24

        GPIO.setup(self.sensorX1_pin, GPIO.IN)
        GPIO.setup(self.sensorX2_pin, GPIO.IN)
        GPIO.setup(self.sensorX3_pin, GPIO.IN)
        GPIO.setup(self.sensorX4_pin, GPIO.IN)
        GPIO.setup(self.sensorX5_pin, GPIO.IN)
        GPIO.setup(self.sensorX6_pin, GPIO.IN)

        self.sensorX1_state = GPIO.input(self.sensorX1_pin)
        self.sensorX2_state = GPIO.input(self.sensorX1_pin)
        self.sensorY1_state = GPIO.input(self.sensorX1_pin)
        self.sensorY2_state = GPIO.input(self.sensorX1_pin)
        self.sensorZ1_state = GPIO.input(self.sensorX1_pin)
        self.sensorZ2_state = GPIO.input(self.sensorX1_pin)

    def return_sensorState(self):
        print(f'Estado do botão x1: ', self.sensorX1_state)

    def motor_test(self, motor):
        if motor=='x':
            self.motorX.move(True)
            time.sleep(3)
            print('Brake no motor x')
            self.motorX.brake()
            time.sleep(1)
            self.motorX.move(False)
            time.sleep(3)
            print('Fast stop no motor x')
            self.motorX.fast_stop()

        elif motor=='y':
            self.motorY.move(True)
            time.sleep(3)
            self.motorY.fast_stop()
            time.sleep(1)
            self.motorY.move(False)
            time.sleep(3)
            self.motorY.fast_stop()

        elif motor=='z':
            self.motorZ.move(True)
            time.sleep(3)
            self.motorZ.fast_stop()
            time.sleep(1)
            self.motorZ.move(False)
            time.sleep(3)
            self.motorZ.fast_stop()

        else: 
            print("Parâmetro do motor passado incorretamente")

    def motor_test_SENSOR(self, motor):
        if motor=='x':
            self.motorX.move(True)
            while (self.sensorX1_state != 1):
                time.sleep(0.1)  # Tempo de espera entre as leituras do sensor 
            self.motorX.fast_stop()
            time.sleep(1)
            self.motorX.move(False)
            while (self.sensorX2_state != 1):
              time.sleep(0.1)  # Tempo de espera entre as leituras do sensor             
            self.motorX.fast_stop()

        elif motor=='y':
            self.motorY.move(True)
            while (self.sensorY1_state != 1):
                time.sleep(0.1)  # Tempo de espera entre as leituras do sensor             
            self.motorY.fast_stop()
            time.sleep(1)
            self.motorY.move(False)
            while (self.sensorY2_state != 1):
                time.sleep(0.1)  # Tempo de espera entre as leituras do sensor             
            self.motorY.fast_stop()

        elif motor=='z':
            self.motorZ.move(True)
            while (self.sensorz1_state != 1):
                time.sleep(0.1)  # Tempo de espera entre as leituras do sensor 
            self.motorZ.fast_stop()
            time.sleep(1)
            self.motorZ.move(False)
            while (self.sensorZ2_state != 1):
                time.sleep(0.1)  # Tempo de espera entre as leituras do sensor             
            self.motorZ.fast_stop()

        else: 
            print("Parâmetro do motor passado incorretamente")        



def main():

    test = teste()
    t0 = time.time()
    tf = 0
    print("Teste dos sensores (duração de 10 seg), aperte ou solte o clicker 1(pino5)")
    while(tf-t0<10):
        test.return_sensorState()
        time.sleep(0.1)
        tf = time.time()
    print("Teste de movimento do motorx")
    teste.motor_test('x')
    print("Teste de movimento do motory")
    teste.motor_test('y')
    print("Teste de movimento do motorz")
    teste.motor_test('z')
    print("Teste de calibração do tempo em x: ")
    teste.calibration_x()

    print("Teste de parada dos motores com o sensor")
    print("Motor X")


    


if __name__ == "__main__":
    main()

