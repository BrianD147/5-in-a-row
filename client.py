import socket

SERVER_IP = '127.0.0.1' # Localhost IP
SERVER_PORT = 3000  # Localhost port
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialise a socket instance (AF_INET -> ipv4 , SOCK_STEAM -> TCP) 

class GameClient():
    def start(self):
        CLIENT.connect_ex((SERVER_IP, SERVER_PORT)) # Bind localhost to the socket

        gameRunning = True
        # serverResponse = CLIENT.recv(1024).decode()  # Player number message
        # print(serverResponse)

        # serverResponse = CLIENT.recv(1024).decode()  # Lets Play! message
        # print(serverResponse)

        while gameRunning:
            serverMessage = CLIENT.recv(1024).decode() # Receive message
            print(serverMessage)

            if serverMessage == "Enter a column (1-9): ":
                clientResponse = input()   # Read the input
                CLIENT.send(clientResponse.encode())    # And send it back

            # serverResponse = CLIENT.recv(1024).decode() # Input message
            # clientResponse = input(serverResponse)  # Read input
            # CLIENT.send(clientResponse.encode())    # Send input

            # serverResponse = CLIENT.recv(1024).decode() # Opponents turn message
            # print(serverResponse)   # Print message

        CLIENT.close()

GameClient().start()    # Startup