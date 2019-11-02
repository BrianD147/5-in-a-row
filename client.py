import socket

SERVER_IP = '127.0.0.1' # Localhost IP
SERVER_PORT = 3000  # Localhost port
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialise a socket instance (AF_INET -> ipv4 , SOCK_STEAM -> TCP) 

class GameClient():
    def start(self):
        CLIENT.connect_ex((SERVER_IP, SERVER_PORT)) # Bind localhost to the socket

        gameRunning = True
        
        while gameRunning:
            serverMessage = CLIENT.recv(1024).decode() # Receive message
            print(serverMessage)

            if serverMessage == "Enter a column (1-9): ":
                clientResponse = input()   # Read the input
                CLIENT.send(clientResponse.encode())    # And send it

        CLIENT.close()

GameClient().start()    # Startup