from limit.screen import Screen
from entity.stack import Stack

class Control():

    def __init__(self):
        self.__screen = Screen()

    def start(self):        
        size = self.__screen.options()

        Stack(size)