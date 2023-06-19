import RPi.GPIO as GPIO # Controle dos motores 
import time # Obter tempo de execução
import sys
import getch  # Biblioteca para ler uma tecla pressionada no terminal

from motor_class import motor

motorx = motor(pinx,piny,pin_pwm)
motory = motor(pinx,piny,pin_pwm)
motorz = motor(pinx,piny,pin_pwm)


# Definir os pinos utilizados para controlar os motores
# motorx_pin1 = 18  # Pino para a direção do motor 1
# motorx_pin2 = 23  # Pino para a direção do motor 1
# motorx_pwm_pin = 24  # Pino para a velocidade do motor 1

# motory_pin1 = 25  # Pino para a direção do motor 2
# motory_pin2 = 8  # Pino para a direção do motor 2
# motory_pwm_pin = 7  # Pino para a velocidade do motor 2

# motorz_pin1 = 25  # Pino para a direção do motor 2
# motorz_pin2 = 8  # Pino para a direção do motor 2
# motorz_pwm_pin = 7  # Pino para a velocidade do motor 2

# Configurações das conexões dos motores
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(motorx_pin1, GPIO.OUT) #in1
# GPIO.setup(motorx_pin2, GPIO.OUT) #in2
# GPIO.setup(motorx_pwm_pin, GPIO.OUT) # pin enable

# GPIO.setup(motory_pin1, GPIO.OUT)
# GPIO.setup(motory_pin2, GPIO.OUT)
# GPIO.setup(motory_pwm_pin, GPIO.OUT)

# GPIO.setup(motorz_pin1, GPIO.OUT)
# GPIO.setup(motorz_pin2, GPIO.OUT)
# GPIO.setup(motorz_pwm_pin, GPIO.OUT)


# Função para calibrar o tempo de movimento em um eixo específico
def time_calibration(eixo):
    print(f"Calibrando tempo de movimento no eixo {eixo}...")
    tempo = 0
    t0 = time.time()
    if eixo == 'X':
        while True:
            motorx.move() #Padrão é para frente com 50% de vel
            if getch.kbhit():  # Verificar se uma tecla foi pressionada no terminal
                tecla = getch.getch()  # Ler a tecla pressionada
                tf = time.time()
                break
            # time.sleep(0.05)
            # tempo += 0.1  # Ajuste o valor conforme a precisão necessária
            # time.sleep(0.1)  # Tempo de espera entre as verificações
        motorx.stop  # Parar o motor
        tempo = tf - t0
        print(f"Tempo de movimento no eixo {eixo}: {tempo:.2f} segundos")
        return tempo
    
    elif eixo == 'Y':
        while True:
            motorx.move() #Padrão é para frente com 50% de vel
            if getch.kbhit():  # Verificar se uma tecla foi pressionada no terminal
                tecla = getch.getch()  # Ler a tecla pressionada
                tf = time.time()
                break
            # time.sleep(0.05)
            # tempo += 0.1  # Ajuste o valor conforme a precisão necessária
            # time.sleep(0.1)  # Tempo de espera entre as verificações
        motorx.stop  # Parar o motor
        tempo = tf - t0
        print(f"Tempo de movimento no eixo {eixo}: {tempo:.2f} segundos")
        return tempo
    
    elif eixo == 'Z':
        while True:
            motorx.move() #Padrão é para frente com 50% de vel
            if getch.kbhit():  # Verificar se uma tecla foi pressionada no terminal
                tecla = getch.getch()  # Ler a tecla pressionada
                tf = time.time()
                break
            # time.sleep(0.05)
            # tempo += 0.1  # Ajuste o valor conforme a precisão necessária
            # time.sleep(0.1)  # Tempo de espera entre as verificações
        motorx.stop  # Parar o motor
        tempo = tf - t0
        print(f"Tempo de movimento no eixo {eixo}: {tempo:.2f} segundos")
        return tempo



# Função principal
def main():

    tempo_x = time_calibration('X')
    tempo_y = time_calibration('Y')
    tempo_z = time_calibration('Z')

    # Use os valores de tempo_x, tempo_y e tempo_z para a calibração dos movimentos em cada eixo

    # Exemplo de uso dos tempos calibrados
    print(f"Tempo calibrado em X: {tempo_x} segundos")
    print(f"Tempo calibrado em Y: {tempo_y} segundos")
    print(f"Tempo calibrado em Z: {tempo_z} segundos")

if __name__ == "__main__":
    main()
