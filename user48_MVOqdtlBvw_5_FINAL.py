"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(900)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
#    print 'called'
    if board.check_win() != None:
        return 0, (-1,-1)
    else:
        if player == provided.PLAYERX:
            best_score, best_move = -1, (-1,-1)
        elif player == provided.PLAYERO:
            best_score, best_move = 1, (-1,-1)

        empty_squares_list = board.get_empty_squares()
        for trial_square in empty_squares_list:
            clone_board = board.clone()
            
            clone_board.move(trial_square[0], trial_square[1], player)
#            print clone_board
#            print trial_square, player
            result = clone_board.check_win()
            
            if result == None:
                myscore = mm_move(clone_board, provided.switch_player(player))[0]
#                print 'debug', myscore, mymove
            elif SCORES[result] == 1 and player == provided.PLAYERX:
                return SCORES[result], trial_square
            elif SCORES[result] == -1 and player == provided.PLAYERO:
                return SCORES[result], trial_square
            else:
                myscore = SCORES[result]

            if player == provided.PLAYERX and myscore >= best_score:
                best_score, best_move = myscore, trial_square
            elif player == provided.PLAYERO and myscore <= best_score:
                best_score, best_move = myscore, trial_square

        return best_score, best_move
        
        
        
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
## poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
#test_board1 = provided.TTTBoard(3)
#test_board1.move(0,2,provided.PLAYERX)
#test_board1.move(1,1,provided.PLAYERO)
#test_board1.move(0,0,provided.PLAYERX)
#test_board1.move(0,1,provided.PLAYERO)
#test_board1.move(2,1,provided.PLAYERX)
#test_board1.move(1,2,provided.PLAYERO)
#test_board1.move(1,0,provided.PLAYERX)
#
#print test_board1
#print('lets go')
#print('==========================================================================================')
#print mm_move(test_board1,provided.PLAYERO)
#
###################################################3
##test_board1 = provided.TTTBoard(3)
##test_board1.move(0,2,provided.PLAYERO)
##test_board1.move(1,1,provided.PLAYERX)
##test_board1.move(0,0,provided.PLAYERO)
##test_board1.move(0,1,provided.PLAYERX)
##test_board1.move(2,1,provided.PLAYERO)
##test_board1.move(1,2,provided.PLAYERX)
##test_board1.move(1,0,provided.PLAYERO)
##
##print test_board1
##print('lets go')
##print('==========================================================================================')
##print mm_move(test_board1,provided.PLAYERX)
#
#
#
