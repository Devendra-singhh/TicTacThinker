
# packages
from copy import deepcopy
from mcts import *

# tic tac toe Board class
class Board():
    #Constructor
    def __init__(self, board=None):
        #define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '.'

        #define board position
        self.position = {}

        #init reset board
        self.init_board()

        #create a copy of previous board state if there is any available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)
    
    #init (reset) board
    def init_board(self):
        #loop board over rows
        for row in range(3):
            #loop board over columns
            for col in range(3):
                self.position[row, col] = self.empty_square

    #make move
    def make_move(self, row, col):
        # create new board instances which inherits from current board state
        board = Board(self)

        #make move
        board.position[row, col] = self.player_1

        #swap players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)

        #return new board state
        return board
    
    # get whether the game is drawn
    def is_draw(self):
        # loop over board squares
        for row, col in self.position:
            # empty square is available
            if self.position[row, col] == self.empty_square:
                # this is not a draw
                return False

        # by default we return a draw
        return True

    # get whether the game is won
    def is_win(self):
        # vertical sequence detection
        # loop board over columns
        for col in range(3):
            # define count of winning sequence
            count = 0

            # loop board over row
            for row in range(3):
                if self.position[row, col] == self.player_2:
                    # update count
                    count += 1

                if count == 3:
                    return True
                   
        # horizontal sequence detection
        # loop board over columns
        for row in range(3):
            # define count of winning sequence
            count = 0

            # loop board over row
            for col in range(3):
                if self.position[row, col] == self.player_2:
                    # update count
                    count += 1

                if count == 3:
                    return True

        # 1st diagonal sequence detection
        # define count of winning sequence
        count = 0
        # loop board over columns
        for row in range(3):
            col = row
            # check for the diagonal elements
            if self.position[row, col] == self.player_2:
                # update count
                count += 1

        if count == 3:
            return True
        
        # 2nd diagonal sequence detection  
        # define count of winning sequence
        count = 0
        # loop board over columns
        for row in range(3):
            col = 3 - row - 1
            # check for the diagonal elements
            if self.position[row, col] == self.player_2:
                # update count
                count += 1

        if count == 3:
            return True

        # by default
        return False
    
    def generate_states(self):
        # define states list (move list - list of available actions to consider)
        actions = []

        # loop board over rows
        for row in range(3):
            # loop board over columns
            for col in range(3):
                # make sure that current square is empty
                if self.position[row, col] == self.empty_square:
                    actions.append(self.make_move(row, col))

        return actions

    # main game loop
    def game_loop(self):
        print('\n  Tic Tac Toe game\n')
        print(' Type "exit to quit the game')
        print(' Move format [x, y]: 1,2 where 1 is the column and 2 is the row')

        # print board
        print(self)

        # create a MCTS instance
        mcts = MCTS()

        # game loop
        while True:
            # get user input
            user_input = input('> ')

            # escape condition
            if user_input == 'exit' : break

            # skip empty input
            if user_input == '' : continue

            try:
                # parse user input
                row = int(user_input.split(',')[1]) - 1
                col = int(user_input.split(',')[0]) - 1

                # check the legality of the move
                if self.position[row, col] !=  self.empty_square:
                    print(' Illegal move!')
                    continue

                # make move on board
                self = self.make_move(row, col)

                # search for the best move
                best_move = mcts.search(self)

                try:
                    # make AI move here
                    self = best_move.board
                except:
                    pass

                # print board
                print(self)

                # check if the game is won
                if self.is_win():
                    print('player "%s" has won the game!\n' % self.player_2)
                    break

                # check if the game is drawn
                if self.is_draw():
                    print('Game is drawn!\n')
                    break

            except Exception as e:
                print(' Error: ', e)
                print(' Illegal command!')
                print(' Move format [x, y]: 1,2 where 1 is the column and 2 is the row')

    #print board state
    def __str__(self):
        #define board string representation
        board_string = ''

        #loop board over rows
        for row in range(3):
            #loop board over columns
            for col in range(3):
                board_string += ' %s' % self.position[row, col]

            #print new line every row
            board_string += '\n'

        #prepend side to move
        if self.player_1 == 'x':
            board_string = '\n-------------------\n "x" to move: \n-------------------\n' + board_string

        elif self.player_1 == 'o':
            board_string = '\n-------------------\n "o" to move: \n-------------------\n' + board_string

        #return board string
        return board_string        


# main driver
if __name__ == '__main__':
    # create board instance
    board = Board()

    # start game loop
    board.game_loop()