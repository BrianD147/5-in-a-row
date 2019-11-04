# 5-in-a-row

### Running the game

* Open a command prompt and run the server - **python server.py**
* Open a seperate command prompt and connect a client - **python client.py**
* Enter the clients name into the console
* Open a 3rd command prompt and connect the 2nd client - **python client.py**
* Enter the 2nd clients name into the console

### Game flow

Each player takes turns to make a move, by entering which column they want to drop their piece down. First person to make a line of 5 pieces in a row wins (Horizonal, Vertical, or Diagonal)

### Server
The server handles the connecting of the players, and sends and recieves all the information that each client needs. After initially connecting both players, the server routinely sends each client the updated board, and then either requests the players move input, or informs the player it is their opponents turn. Each turn the server also calls on the logic.py to determine if there has been a winner.

### Logic
The logic constructs the board, places pieces into the board, and then routinely checks after each move whether a winning state has been reached.

### Client
The client simply recieves messages from the server. When the next move is needed, the client prompts input and sends it back to the server.

### Overview
I wanted to keep the client as dumb as possible, however opted to do a simple check of the servers message in order to determine if input is needed. 

The logic is pretty tidy when checking for a game win, initally was going to use numpy to manage the board matrix, but ended up moving over to a basic array instead. There isn't much complexity to the program, so the time using numpy would have saved is minute.

The server uses sockets to connect to the clients, working over localhost for now. I opted to extract the game logic to a seperate class, as it simply made more sense to me, having the server manage mainly just messaging back and forth to clients.

Currently there is no error checking for clients input, the program expects the players to only enter 1-9 when prompted, also their is no check for whether a piece can be placed into a column, so the program expects the players not to try and put a piece into an already full column. Also there isn't a DRAW state, meaning the program expects one of the two players to reach a winning state.
