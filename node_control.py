import socketio
from control_class import control


# Crie uma instância do Socket.IO client
sio = socketio.Client()

# Variáveis para armazenar os valores
procedimento = None
compartimento = None

control = control()

@sio.event
def connect():
    print('Conectado ao servidor')

@sio.event
def mensagem(data):
    global procedimento, compartimento
    print('Mensagem recebida:', data)

    # Atribua os valores aos procedimento e compartimento
    procedimento = data['procedimento']
    compartimento = data['compartimento']

    # Realize o processamento necessário com os dados recebidos
    print('Procedimento:', procedimento)
    print('Compartimento:', compartimento)

    # Executar procedimento
    if (procedimento=='armazenar'):
        control.armazenar(compartimento)
    elif (procedimento=='retirar'):
        control.retirar(compartimento)
    else:
        print("Procedimento recebido é inválido: ", procedimento)


@sio.event
def disconnect():
    print('Desconectado do servidor')

# Conecte-se ao servidor Socket.IO
sio.connect('http://localhost:3000')

# Mantenha o cliente em execução
sio.wait()
