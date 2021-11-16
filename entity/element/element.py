class Element:
    def __init__(self, data):
        self.__data = data
        self.__prev = None


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, elem):
        self.__prev = elem