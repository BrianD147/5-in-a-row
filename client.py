import socket

SERVER_IP = '127.0.0.1' # Localhost IP
SERVER_PORT = 3000  # Localhost port
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialise a socket instance (AF_INET -> ipv4 , SOCK_STEAM -> TCP) 

class GameClient():
    def start(self):
        CLIENT.connect_ex((SERVER_IP, SERVER_PORT)) # Bind localhost to the socket

        gameRunning = True

        serverMessage = CLIENT.recv(1024).decode()  # Receive name message
        print(serverMessage)    # print
        clientResponse = input()    # Read the name
        CLIENT.send(clientResponse.encode())    # And send it

        while gameRunning:
            try:
                serverMessage = CLIENT.recv(1024).decode() # Receive message
                print(serverMessage)

                if "Enter a column (1-9): " in serverMessage:
                    clientResponse = input()   # Read the input
                    CLIENT.send(clientResponse.encode())    # And send it
                elif "GAME OVER" in serverMessage:
                    gameRunning = False
            except ConnectionResetError:
                gameRunning = False
        CLIENT.close()

GameClient().start()    # Startup