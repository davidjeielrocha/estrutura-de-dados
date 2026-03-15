class Fila:
    def __init__(self):
        self._data = []
    
    def enfileirar(self, item):
        self._data.append(item)
    
    def desenfileirar(self):
        if self.is_empty():
            raise IndexError("Desenfileirar não se aplica, a fila está vazia")
        return self._data.pop(0)
    
    def espiar(self):
        if self.is_empty():
            raise IndexError("Espiar não se aplica, a fila está vazia")
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def size(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)