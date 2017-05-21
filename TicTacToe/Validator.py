#from Exceptions import Not_A_Possible_Input_Or_Not_In_Array_Size, Not_An_Integer , Place_Is_Cover

class Validator():
    #def __init__(self, size):
     #   self.__size=size

    def a_possibe_input_or_in_array_size(self , value, N):
        if (0 <= value and value < N):
            return True
        else:
            return False

    def an_integer(self , value):
        if isinstance(value, int):
            return True
        else:
            return False

    def place_is_free(self , value_x, value_y, list_of_circles,list_of_crosses):
        if ((value_x,value_y) in list_of_circles or (value_x,value_y) in list_of_crosses):
            return False
        else:
            return True