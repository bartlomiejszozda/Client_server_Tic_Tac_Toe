import socket
import sys

from Validator import Validator
from Exceptions import Not_A_Possible_Input_Or_Not_In_Array_Size, Not_An_Integer , Place_Is_Cover
Validator = Validator()

from draw_board import draw_board
board=draw_board()

from game_state import game_state
state=game_state()

from computer_player import computer_player
computer = computer_player()

import random



sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',10000)
sys.stderr.write( 'starting up on %s port %s'% server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    sys.stderr.write(' \nwaiting for a connection')
    connection, client_address=sock.accept()
    if connection or client_address:
        break


def value_in_size(x, y, N):
    if not Validator.a_possibe_input_or_in_array_size(x, N):
        connection.send(str.encode("wybrales zbyt duze liczby(x,y musza byc mniejsze od rozmiaru)"))
        # raise Not_A_Possible_Input_Or_Not_In_Array_Size(x)
        return False
    if not Validator.a_possibe_input_or_in_array_size(y, N):
        connection.send(str.encode("wybrales zbyt duze liczby(x,y musza byc mniejsze od rozmiaru)"))
        # raise Not_A_Possible_Input_Or_Not_In_Array_Size(y)
        return False
    elif (not Validator.place_is_free(x, y, board.list_of_circle_points, board.list_of_cross_points)):
        # raise Place_Is_Cover((x, y))
        connection.send(str.encode("pole zajete"))
        return False
    return True

try:
    sys.stderr.write('\nconnection from {}'.format(client_address))

    while True:
        connection.send(str.encode("\nchcesz zagrac w kolko i krzyzyk? (wpisz 1)\n chcesz zagrac w zgadnij liczbe, wpisz 2"))

        #################################### sprawdzanie poprawnosci input()
        while True:
            data = connection.recv(16)
            if (data.decode()=="1" or data.decode()=="2"):
                break
            connection.send(str.encode("Podano zly input. Jesli chcesz zagrac w kolko i krzyzyk podaj 1, jesli chcesz grac w zgadnij liczbe, podaj 2"))
        #################################
        if data:
            if "1" == data.decode():
                connection.send(str.encode("Witamy w grze kolko i krzyzyk. Rozmiar planszy n x n, wybierz n:"))
                #odbieramy informacje na temat rozmiaru planszy
                while True:
                    data = connection.recv(16)
                    board_size = int(data.decode())
                    if(True):
                        break
                    connection.send(str.encode("Zly input(). Podaj rozmiar planszy jako jedna liczbe typu int"))

                connection.send(str.encode(board.draw_board(board_size) + "Aby wybrac miejsce postawienia znaku, wpisz (x y) bez nawiasow\n, gdzie x-numer wiersza, y-numer kolumny numerowane od 0."))

                while(True):
                    while (True):
                        data = connection.recv(16)
                        place = data.decode()
                        #################### obsluga zbyt krotkiego input()
                        while (len(place)<2):
                            connection.send(str.encode("Zly input.Podaj (x y), bez nawiasow, gdzie x-numer wiersza, y-numer kolumny numerowane od 0."))
                            data = connection.recv(16)
                            place = data.decode()
                        ######################
                        x=int(place[0])
                        y=int(place[2])
                        ############################## obsluga zlego input() za pomoca value_in_size
                        if (value_in_size(x, y, board_size)):
                            board.list_of_cross_points.append((x, y))
                            break
                        ##############################
                    if (state.if_game_over()):
                        connection.send(str.encode(board.draw_board(board_size)+"zwyciezyles, dzieki za gre"))
                        break
                    computer.do_turn(board_size)
                    if (state.if_game_over()):
                        connection.send(str.encode("zwyciezyl komputer, dzieki za gre"))
                        break
                    connection.sendall(str.encode(board.draw_board(board_size) + "Aby wybrac miejsce postawienia znaku, wpisz (x y) bez nawiasow\n, gdzie x-numer wiersza, y-numer kolumny numerowane od 0."))
            elif "2"== data.decode():
                to_guess = random.randint(0, 100)
                attempts = 0
                connection.sendall(str.encode("Zgadnij liczbe!"))
                while True:
                    data = connection.recv(16)
                    guess = int(data.decode())
                    if (guess == to_guess):
                        connection.sendall(str.encode("Zgadles w {} probach".format(attempts)))
                        break
                    if (guess < to_guess):
                        connection.sendall(str.encode("liczba jest wieksza, sprobuj ponownie"))
                        attempts += 1
                    if (guess > to_guess):
                        connection.sendall(str.encode("liczba jest mniejsza, sprobuj ponownie"))
                        attempts += 1
            break


                        #connection.sendall(str.encode("dzieki za gre"))
        else:
            sys.stderr.write('\nno more data from {}' .format(client_address))
            break
finally:
    connection.close()

