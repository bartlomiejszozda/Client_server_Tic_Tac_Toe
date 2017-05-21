
class draw_board:
    list_of_circle_points=[]
    list_of_cross_points=[]

    def __init__(self):
        self.board_string=""
    def draw_board(self,N):
        self.board_string=""
        for i in range (N):
            self.board_string+="("
            for j in range(N):
                self.board_string +="|"
                if((i,j) in self.list_of_circle_points):
                    self.board_string +="O"
                elif ((i,j) in self.list_of_cross_points):
                    self.board_string +="X"
                else:
                    self.board_string +=" "
                    #self.board_string +="|"
            self.board_string +=")"
            self.board_string+="\n"
        return self.board_string
