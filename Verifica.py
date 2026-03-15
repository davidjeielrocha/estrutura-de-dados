# Com algum erro que ainda não consegui identificar, o código abaixo não funciona.

class Nodo:
    def __init__(self, codigo = 0, proximo_nodo = None):
        self.codigo = codigo
        self.proximo_nodo = proximo_nodo

    def __repr__(self):
        return f"Nodo(codigo={self.codigo}, proximo_nodo={self.proximo_nodo})"
    
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"ListaEncadeada(head={self.head})"
    
    def verifica_vazia(ListaEncadeada):
        if ListaEncadeada.head == None:
            print("A lista está vazia.")
            return True
        else:
            print("A lista não está vazia.")
            return False