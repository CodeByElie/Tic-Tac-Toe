class TicTacToe:
    def __init__(self):
        self.__tab = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.__turn = 0

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
