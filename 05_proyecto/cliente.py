# Cliente

import socket
import threading

def recibir_mensajes(sock):
    while True:
        try:
            mensaje = sock.recv(1024).decode('utf-8')
            print(f"\n{mensaje}")
        except:
            print("[!] La conexion ya esta cerrada.")
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('127.0.0.1', 5000))

    nombre = input("Ingresa tu nombre por favor: ")


    hilo_recibo = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_recibo.daemon = True
    hilo_recibo.start()

    while True:
        msg = input("> ")
        if msg.lower() == 'salir': break
        cliente.send(f"{nombre}: {msg}".encode('utf-8'))

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()