class Deque:
    def __init__(self):
        self.items = []

    def adicionaFrente(self, item):
        self.items.append(item)

    def adicionaAtras(self, item):
        self.items.insert(0, item)

    def removeFrente(self):
        return self.items.pop()
    
    def removeAtras(self):
        return self.items.pop(0)
    
    def estaVazio(self):
        return self.items == []
    
    def tamanho(self):
        return len(self.items)