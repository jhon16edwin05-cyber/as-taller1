# Servidor

import socket
import threading


HOST = '127.0.0.1'  
PORT = 5000        
clientes = []

def broadcast(mensaje, _cliente_actual):
    """Envía el mensaje a todos los clientes excepto al que lo envió."""
    for cliente in clientes:
        if cliente != _cliente_actual:
            try:
                cliente.send(mensaje)
            except:
                cliente.close()
                clientes.remove(cliente)

def manejar_cliente(cliente):
    """Gestiona la conexión individual de cada cliente."""
    while True:
        try:
            mensaje = cliente.recv(1024)
            if not mensaje: break
            broadcast(mensaje, cliente)
        except:
            clientes.remove(cliente)
            cliente.close()
            break

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] Servidor escuchando {HOST}:{PORT}")

    while True:
        cliente_socket, direccion = server.accept()
        print(f"[*] Nueva conexión iniciada desde {direccion}")
        clientes.append(cliente_socket)
        
       
        hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()