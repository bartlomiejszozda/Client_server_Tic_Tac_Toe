from draw_board import draw_board

board = draw_board()
class game_state:
    def if_game_over(self):
        return self.any_of_three_elements_in_win_position(board.list_of_cross_points) or self.any_of_three_elements_in_win_position(board.list_of_circle_points)


    def if_arg1_in_hood_with_arg2(self,point1,point2):
        if (abs(point1[0]-point2[0])<=1 and abs(point1[1]-point2[1])<=1):
            return 1
        else:
            return 0

    def if_three_points_in_win_position(self,point1,point2,point3):
        if(self.if_arg1_in_hood_with_arg2(point1, point2) and self.if_arg1_in_hood_with_arg2(point1, point3)):
            return point1[0]-point2[0]==point3[0]-point1[0] and point1[1]-point2[1]==point3[1]-point1[1]

        if(self.if_arg1_in_hood_with_arg2(point1, point2) and self.if_arg1_in_hood_with_arg2(point2, point3)):
            return point1[0]-point2[0]==point2[0]-point3[0] and point1[1]-point2[1]==point2[1]-point3[1]

        if(self.if_arg1_in_hood_with_arg2(point2, point3) and self.if_arg1_in_hood_with_arg2(point1, point3)):
            return point3[0]-point2[0]==point1[0]-point3[0] and point3[1]-point2[1]==point1[1]-point3[1]

    def any_of_three_elements_in_win_position(self,list_of):
        for i in range(len(list_of)):
            for j in range (len(list_of)):
                for k in range(len(list_of)):
                    if(not (i==j and j==k) ):
                        if (self.if_three_points_in_win_position(list_of[i],list_of[j],list_of[k])):
                            return 1
        return 0
