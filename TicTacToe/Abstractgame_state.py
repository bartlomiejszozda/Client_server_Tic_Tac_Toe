import abc
from abc import ABC

class Abstractgame_state(ABC):
    """klasa abstrakcyjna sprawdzajaca czy gra powinna byc kontynuowana ( czy nikt nie zwyciezyl stawiajac 3 znaki w linii)"""
    @abc.abstractmethod
    def if_game_over(self):
        pass
        """zwraca 1, gdy ktos zwyciezyl, 0 gdy gra powinna byc kontunowana"""

    @abc.abstractmethod
    def if_arg1_in_hood_with_arg2(self,point1,point2):
        pass
        """sprawdza, czy point 1 jest w sasedztwie point 2"""

    @abc.abstractmethod
    def if_three_points_in_win_position(self,point1,point2,point3):
        pass
        """sprawdza, czy podane w parametrach trzy punkty sa na wygranej pozycji ( 3 w jednej linii)"""

    @abc.abstractmethod
    def any_of_three_elements_in_win_position(self,list_of):
        pass
        """sprawdza, czy jakiekolwiek 3 elementy na planszy sa punktami na wygranej pozycji"""