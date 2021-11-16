from entity.element.element import Element

class Stack:
    def __init__(self):
        self.__size = 0
        self.__top = None
        
    #Adiciona elemento na pilha
    def push(self, elem):
        #Adiciona elemento à pilha
        element = Element(elem)
        element.prev(self.__top)
        self.__top = element
        self.__size =+ 1

    
    #Remove elemento da pilha
    def pop(self):
        if self.__size > 0:
            element = self.__top
            self.__top = self.__top.prev
            self.__size -= 1
            return element

        raise IndexError("A pilha está vazia")

    #Informa o topo
    def peek(self):
        if self.__size > 0:            
            return self.__top.data

        raise IndexError("A pilha está vazia")
        

    #Informa tamanho da pilha
    def __len__(self):
        return self.__size

    #Representação da pilha
    def __repr__(self):
        repr = ""
        pointer = self.__top
        while(pointer):
            repr = repr + str(pointer.data) + "\n"
            pointer = pointer.prev
        
        return pointer

    def __str__(self):
        return self.__repr__()

    