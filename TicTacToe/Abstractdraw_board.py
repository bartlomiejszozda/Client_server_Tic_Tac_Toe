import abc
from abc import ABC

class Abstractdraw_board:
    """rysuje tablice do gry wraz z juz wstawionymi znakami"""

    @abc.abstractmethod
    def draw_board(self,N):
        pass
        """rysuje tablice do gry wraz z juz wstawionymi znakami"""