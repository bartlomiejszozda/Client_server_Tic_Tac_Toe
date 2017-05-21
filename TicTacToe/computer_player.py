from draw_board import draw_board
board=draw_board()
from Validator import Validator
from random import randint

class computer_player:
    def do_turn(self,N):
        while(True):
            x=randint(0,N-1)
            y=randint(0,N-1)
            if (Validator.place_is_free(self , x, y, board.list_of_circle_points, board.list_of_cross_points) and  Validator.a_possibe_input_or_in_array_size(self,x,N) and Validator.a_possibe_input_or_in_array_size(self, y,N) ):
                board.list_of_circle_points.append((x, y))
                break

