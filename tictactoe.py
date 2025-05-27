class TicTacToe:
    """
    A class to represent a Tic-Tac-Toe game.
    This class manages the state of a Tic-Tac-Toe board, handles player moves, checks for game termination, 
    determines the winner, and provides utility methods for displaying the board and querying available moves.
    Attributes:
        __tab (list[list[int]]): Internal 3x3 board representation. Each cell contains -1 (empty), 0 (player X), or 1 (player O).
        __turn (int): Indicates the current player's turn. 0 for player X, 1 for player O.
        __winner (int): Stores the winner of the game. -1 if no winner yet, 0 for player X, 1 for player O.
    Methods:
        __init__():
            Initializes a new game with an empty board, sets the starting player, and resets the winner.
        display():
            Prints the current state of the board in a formatted grid, showing 'X', 'O', or blank for each cell.
        play(x: int, y: int):
            Executes a move for the current player at the specified (x, y) coordinates.
            Raises an AssertionError if the move is invalid (out of bounds or cell occupied).
        isEnded() -> bool:
            Checks if the game has ended due to a win (three in a row, column, or diagonal).
            Updates the winner if the game has ended.
            Returns True if the game is over, False otherwise.
        getWinner() -> int:
            Raises an Exception if the game is not finished.
        getFreeCells() -> list[tuple[int, int]]:
            Returns a list of (x, y) tuples representing all empty cells on the board.
    """



    def __init__(self,tab=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],turn = 0, winner = -1):
        self.__tab = tab
        self.__turn = turn
        self.__winner = winner

    def copy(self):
        return TicTacToe([[i for i in line] for line in self.__tab],self.__turn,self.__winner)


    def display(self):
        """
        Displays the current state of the Tic-Tac-Toe board in a formatted grid.
        The board is printed with horizontal and vertical separators. Each cell displays
        'X', 'O', or a blank space depending on its value in the internal board representation.
        """
        print("-"*13)
        for line in self.__tab:
            for cel in line:
                print("| "+["X","O"," "][cel]+" ",end="")
            print("|")
            print("-"*13)
    
    def play(self,x: int,y: int):
        """
        Executes a move in the Tic-Tac-Toe game at the specified (x, y) coordinates.
        Args:
            x (int): The x-coordinate (column) of the cell to play (must be between 0 and 2).
            y (int): The y-coordinate (row) of the cell to play (must be between 0 and 2).
        Raises:
            AssertionError: If x or y are out of bounds (not between 0 and 2).
            AssertionError: If the cell at (x, y) is already occupied.
        Side Effects:
            Updates the game board at position (x, y) with the current player's mark.
            Switches the turn to the next player.
        """
        if x<0 or x>2:
            assert(f"x coordinate must be between 0 and 2. [Given value : x=(${x})]")
        if y<0 or y>2:
            assert(f"y coordinate must be between 0 and 2. [Given value : y=(${y})]")
        if self.__tab[y][x]!=-1:
            assert(f"Cell at position ({x}, {y}) is already occupied.")
        self.__tab[y][x]=self.__turn
        self.__turn= (self.__turn+1)%2
    
    def isEnded(self)  -> bool:
        """
        Checks if the Tic-Tac-Toe game has ended.
        The game is considered ended if any row, column, or diagonal contains the same value 
        (indicating a win for one of the players).
        Returns:
            bool: True if the game has ended (a player has won), False otherwise.
        """

        for line in self.__tab:
            if line[0]==line[1] and line[1]==line[2] and line[0]!=-1:
                self.__winner = line[0]
                return True
        for i in range(3):
            if self.__tab[0][i]==self.__tab[1][i] and self.__tab[1][i]==self.__tab[2][i] and self.__tab[2][i]!=-1:
                self.__winner = self.__tab[0][i]
                return True
        if self.__tab[0][0]==self.__tab[1][1] and self.__tab[1][1]==self.__tab[2][2] and self.__tab[1][1]!=-1:
            self.__winner = self.__tab[1][1]
            return True
        if self.__tab[0][2]==self.__tab[1][1] and self.__tab[1][1]==self.__tab[2][0] and self.__tab[1][1]!=-1:
            self.__winner = self.__tab[1][1]
            return True
        if len(self.getFreeCells())==0:
            self.__winner = -1
            return True
        return False

    def getWinner(self) -> int:
        """
        Returns the winner of the game.
        Returns:
            int: The winner of the game. Typically, this could be 1 for player 1, -1 for player 2, or 0 for a draw.
        Raises:
            Exception: If the game has not ended yet.
        """

        if not self.isEnded():
            raise Exception("The game is not finished yet.")
        return self.__winner

    def getFreeCells(self) -> list[tuple[int,int]]:
        """
        Returns a list of coordinates for all free (empty) cells on the Tic-Tac-Toe board.
        Each free cell is represented as a tuple (x, y), where x is the column index and y is the row index.
        A cell is considered free if its value in the internal board representation (self.__tab) is -1.
        Returns:
            list[tuple[int, int]]: A list of (x, y) tuples indicating the positions of all free cells.
        """
        return [(x,y) for x in range(3) for y in range(3) if self.__tab[y][x]==-1]
