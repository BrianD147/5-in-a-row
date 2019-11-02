import socket   # https://docs.python.org/3/library/socket.html

from logic import Logic

SERVER_IP = '127.0.0.1' # Localhost IP
SERVER_PORT = 3000  # Localhost port
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialise a socket instance (AF_INET -> ipv4 , SOCK_STEAM -> TCP) 
SERVER.bind((SERVER_IP, SERVER_PORT))   # Bind localhost to the socket
SERVER.listen(2)   # Allow 2 connections to the server

PLAYER_OBJECTS = {}

class GameServer():
    def start(self):
        gameRunning = True

        print("Awaiting Players...")
        self.connectPlayers()   # Connect 2 players

        print("Players connected.. starting game")
        counter = 1

        while gameRunning:
            try:     
                self.updateClients(Logic().displayBoard())  # Display the game board
                PLAYER_OBJECTS[counter]['playerObject'].send("Opponents turn...".encode())   # Opponents turn message

                counter = 1 - counter

                clientInput = self.getInput(PLAYER_OBJECTS[counter]['playerObject'])    # Input request
                Logic().placePiece(counter, int(clientInput))
            except ConnectionResetError:
                gameRunning = False
        SERVER.close()

    def connectPlayers(self):
        for i in range(2):
            playerObject, playerAddress = SERVER.accept() # Accept connection to the server (returns [Object, Address])
            print("Client connected: ", playerAddress)
            playerName = self.getName(playerObject)
            PLAYER_OBJECTS[i] = {'playerObject': playerObject, 'playerAddress': playerAddress, 'playerName': playerName}  # populate PLAYER_OBJECTS with the clients object address, and name
            playerObject.send("Welcome {}".format(playerName).encode())

        self.updateClients("Both Players connected.. Lets Play!")

    def getName(self, playerObject):
        playerObject.send("Enter your name: ".encode())
        return playerObject.recv(1024).decode()

    def getInput(self, playerObject):
        playerObject.send("Enter a column (1-9): ".encode()) # Send input request
        return playerObject.recv(1024).decode()  # Return response (bufsize should be small power of 2)

    def updateClients(self, update):
        for count in PLAYER_OBJECTS:
            PLAYER_OBJECTS[count]['playerObject'].send(update.encode())


GameServer().start() # Startup