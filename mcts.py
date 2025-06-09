# packages
import math
import random

# tree node class
class Treenode():
    # constructor
    def __init__(self, board, parent):
        # init associated board state
        self.board = board

        # init is node terminal flag
        if self.board.is_win() or self.board.is_draw():
            self.is_terminal = True

        # otherwise
        else:
            self.is_terminal = False

        # init is fully expanded flag
        self.is_fully_expanded = self.is_terminal

        # init parent node if available
        self.parent = parent

        # init number of visits
        self.visits = 0

        # init the total score of the node
        self.score = 0

        # init current node's children
        self.children = {}

# MCTS class definition
class MCTS():
    # search for the best movfe in the current position
    def search(self, initial_state):
        # create a root node
        self.root = Treenode(initial_state, None)

        # walk through iterations
        for iteration in range(10000):
            # select a node (selection phase)
            node = self.select(self.root)

            # score current node (simulation phase)
            score = self.rollout(node.board)

            # backpropagate the number of visits and score up to the root node
            self.backpropagate(node, score)

        # pick up the best move in the current position
        try:
            return self.get_best_move(self.root, 0)

        except:
            pass

    # select most promising node
    def select(self, node):
        # make sure that we're dealing with non-terminal nodes
        while not node.is_terminal:
            # case where node is fully expanded
            if node.is_fully_expanded:
                node = self.get_best_move(node, 2)

            # case where node is not fully expanded
            else :
                return self.expand(node)
            
        return node
    
    # expand node
    def expand(self, node):
        # generate legal states
        states = node.board.generate_states()

        # loop over states
        for state in states:
            # make sure the current node is not present in the child nodes
            if str(state.position) not in node.children:
                # create a new node
                new_node = Treenode(state, node)

                # add child node to parent's node to children list (dict)
                node.children[str(state.position)] = new_node

                # case when node is fully expanded
                if len(states) == len(node.children):
                    node.is_fully_expanded = True

                return new_node 

    # simulate the game by making random moves untill reach end of the game
    def rollout(self, board):
        # make random moves for both sides until terminal state of the game is reached
        while not board.is_win():
            # try to make a move
            try:
                board = random.choice(board.generate_states())

            # no moves available
            except:
                return 0

        # return score from player "x" prespective
        if board.player_2 == 'x' : return 1
        elif board.player_2 == 'o' : return -1

    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, score):        
        # update nodes's up to the root
        while node is not None:
            # update node's visits
            node.visits += 1

            # update node's score
            node.score += score

            # set node to parent
            node = node.parent

    # select the best node basing on UCB1 formula
    def get_best_move(self, node, exploration_constant):
        # define best score and best move
        best_score = float('-inf')
        best_moves = []

        # loop over children nodes
        for child_node in node.children.values():
            # skip unvisited nodes
            if child_node.visits == 0:
                continue

            # define current player
            if child_node.board.player_2 == 'x' : current_player = 1
            elif child_node.board.player_2 == 'o' : current_player = -1

            # get move score using UCT formula
            move_score = current_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(math.log(node.visits) / child_node.visits)

            # better move has been or as good as best_score found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            elif move_score == best_score:
                best_moves.append(child_node)

        # if no moves have been visited, pick a random child
        if not best_moves:
            return random.choice(list(node.children.values()))

        # return one of the best moves
        return random.choice(best_moves)   