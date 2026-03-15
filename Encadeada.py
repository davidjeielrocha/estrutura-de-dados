
from Registro import Registro

sequencial = []

class Encadeada:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        if self.head:
            # Inserção quando a lista já tem elementos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Registro(value)
        else:
            self.head = Registro(value) 
        self._size += 1

    def __len__(self):
        return self._size
    
    
    def get(self, index):
        pass

    def set(self, index, value):
        pass

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer is None:
                raise IndexError("Esse índice não foi encontrado")
            else:
                pointer = pointer.next
        if pointer is None:
            raise IndexError("Esse índice não existe")
        return pointer.value
    
    def __setitem__(self, index, value):
        pointer = self.head
        for i in range(index):
            if pointer is None:
                raise IndexError("Esse índice não foi encontrado")
            else:
                pointer = pointer.next
        if pointer is None:
            raise IndexError("Esse índice não existe")
        else:   
            pointer.data = value

    def index(self, value):
        pointer = self.head
        for i in range(len(self)):
            if pointer.value == value:
                return i
            else:
                pointer = pointer.next
        raise ValueError(" O valor não foi encontrado entre os elementos existentes")


