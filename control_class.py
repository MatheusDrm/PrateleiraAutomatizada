import RPi.GPIO as GPIO # Controle dos motores 
import time # Obter tempo de execução
import sys
from motor_class import motor


class control():
    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        self.sensor_configuration()
        # Configurando os motores
        self.motorX = motor(1,2)
        self.motorY = motor(3,4)
        self.motorZ = motor(5,6)
        # Calibrando eixo x
        self.tx = 0 
        self.tzA = 2 # Tempo em z para armazenar  PRECISA CALIBRAR O TEMPO
        self.tzR = 6
        self.calibration_x()


    def sensor_configuration(self):

        self.sensorX1_pin = 17
        self.sensorX2_pin = 27
        self.sensorY1_pin = 5
        self.sensorY2_pin = 5
        self.sensorZ1_pin = 5
        self.sensorZ2_pin = 5
 
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


    def armazenar(self, compartimento):

        # Pegar a gaveta de um apoio na frente da posição inicial da garra
        self.motorZ.move(True)
        while (self.sensorZ1_state!=1):
            time.sleep(0.1)
        print("Tocou na gaveta")
        self.motorZ.fast_stop()
        self.motorY.move(True)
        time.sleep(0.5)
        self.motorY.fast_stop()

        #Ajeitar posição em Y para primeira fileira
        self.motorY.move(True)
        time.sleep(0.5)
        self.motorY.fast_stop()        
        
        # Garra estará com gaveta presa
        if (compartimento == 'c1'):
            self.c1('armazenar')
        elif (compartimento == 'c2'):
            self.c2('armazenar')
        elif (compartimento == 'c3'):
            self.c3('armazenar')
        elif (compartimento == 'c4'):
            self.c4('armazenar')
        elif (compartimento == 'c5'):
            self.c5('armazenar')
        elif (compartimento == 'c6'):
            self.c6('armazenar')


    def retirar(self, compartimento):

        #Ajeitar posição em Y para primeira fileira
        self.motorY.move(True)
        time.sleep(0.5)
        self.motorY.fast_stop()        
        
        # Garra estará com gaveta presa
        if (compartimento == 'c1'):
            self.c1('retirar')
        elif (compartimento == 'c2'):
            self.c2('retirar')
        elif (compartimento == 'c3'):
            self.c3('retirar')
        elif (compartimento == 'c4'):
            self.c4('retirar')
        elif (compartimento == 'c5'):
            self.c5('retirar')
        elif (compartimento == 'c6'):
            self.c6('retirar')


    def soltarGaveta(self):
        # Procedimento de soltar a gaveta
        self.motorZ.move(True)
        time.sleep(self.tzA)
        self.motorZ.brake()
        self.motorY.move(False)
        time.sleep(1)
        self.motorY.fast_stop()
        self.motorZ.move(False)
        time.sleep(self.tzA)


    def pegarGaveta(self):
        # Procedimento para pegar a gaveta -> Assume-se que já esteja em uma altura adequada para pegar a gaveta
        # Avança em Z até tocar na gaveta
        self.motorZ.move(True)
        tempo_inicial = time.time()
        while (self.sensorZ1_state!=1):
            time.sleep(0.1)
        tempo_final = time.time()
        print("Tocou na gaveta")
        self.motorZ.fast_stop()
        # Sobe em Y para prender no encaixe
        self.motorY.move(True)
        time.sleep(0.5)
        self.motorY.fast_stop()
        # Voltar em Z
        self.motorZ.move(False)
        time.sleep(tempo_final-tempo_inicial)
        self.motorZ.fast_stop()


    def c1(self, procedimento):
        tx = self.tx
        # código para o caso 1
        if(procedimento=='armazenar'):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y -> Já está alinhado
            self.soltarGaveta()

            #Voltar na posição inicial
            self.motorX.move(False)
            time.sleep(tx)
            self.motorX.fast_stop()            

        elif(procedimento=="retirar"):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y -> Já está alinhado
            self.pegarGaveta()
            # Voltar para posição inicial
            self.motorX.move(False)
            time.sleep(tx)
            self.motorX.fast_stop()

            
        else:
            print("Procedimento inválido")    


    def c2(self, procedimento):
        tx = 2*self.tx
        # código para o caso 2
        if(procedimento=='armazenar'):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y -> Já está alinhado
            self.soltarGaveta()

            #Voltar na posição inicial
            self.motorX.move(False)
            time.sleep(tx)
            self.motorX.fast_stop()    
            

        elif(procedimento=="retirar"):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y -> Já está alinhado
            self.pegarGaveta()
            #Voltar na posição inicial
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()


        else:
            print("Procedimento inválido")            

    def c3(self, procedimento):
        tx = 3*self.tx
        # código para o caso 3
        if(procedimento=='armazenar'):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y -> Já está alinhado
            self.soltarGaveta()

            #Voltar na posição inicial
            self.motorX.move(False)
            time.sleep(tx)
            self.motorX.fast_stop()    
            

        elif(procedimento=="retirar"):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y -> Já está alinhado
            self.pegarGaveta()
            #Voltar na posição inicial
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()            

        else:
            print("Procedimento inválido")            

    def c4(self, procedimento):
        tx = self.tx
        # código para o caso 4
        if(procedimento=='armazenar'):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(tx)
            self.motorX.fast_stop()
            # Y
            self.motorY.move(True)
            while (self.sensorY2_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()

            self.soltarGaveta()

            #Voltar na posição inicial
            self.motorY.move(False)
            while (self.sensorY1_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()
            self.motorX.move(False)
            time.sleep(tx)
            self.motorX.fast_stop()    
            

        elif(procedimento=="retirar"):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(self.tx)
            self.motorX.fast_stop()
            # Y 
            self.motorY.move(True)
            while (self.sensorY2_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()

            self.pegarGaveta()

            #Voltar na posição inicial
            self.motorY.move(False)
            while (self.sensorY1_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()
            self.motorX.move(False)
            time.sleep(self.tx)
            self.motorX.fast_stop()    

        else:
            print("Procedimento inválido")            

    def c5(self, procedimento):
        # código para o caso 5
        if(procedimento=='armazenar'):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(self.tx)
            self.motorX.fast_stop()
            # Y
            self.motorY.move(True)
            while (self.sensorY2_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()

            self.soltarGaveta()

            #Voltar na posição inicial
            self.motorY.move(False)
            while (self.sensorY1_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()
            self.motorX.move(False)
            time.sleep(self.tx)
            self.motorX.fast_stop()    
            

        elif(procedimento=="retirar"):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(self.tx)
            self.motorX.fast_stop()
            # Y 
            self.motorY.move(True)
            while (self.sensorY2_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()

            self.pegarGaveta()

            #Voltar na posição inicial
            self.motorY.move(False)
            while (self.sensorY1_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()
            self.motorX.move(False)
            time.sleep(self.tx)
            self.motorX.fast_stop()    

        else:
            print("Procedimento inválido")    

    def c6(self, procedimento):
        # código para o caso 6
        if(procedimento=='armazenar'):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(self.tx)
            self.motorX.fast_stop()
            # Y
            self.motorY.move(True)
            while (self.sensorY2_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()

            self.soltarGaveta()

            #Voltar na posição inicial
            self.motorY.move(False)
            while (self.sensorY1_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()
            self.motorX.move(False)
            time.sleep(self.tx)
            self.motorX.fast_stop()    
            

        elif(procedimento=="retirar"):
            # Alinhar em x
            self.motorX.move(True)
            time.sleep(self.tx)
            self.motorX.fast_stop()
            # Y 
            self.motorY.move(True)
            while (self.sensorY2_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()

            self.pegarGaveta()

            #Voltar na posição inicial
            self.motorY.move(False)
            while (self.sensorY1_state!=1):
              time.sleep(0.1)
            self.motorY.fast_stop()
            self.motorX.move(False)
            time.sleep(self.tx)
            self.motorX.fast_stop()    

        else:
            print("Procedimento inválido")   
        


