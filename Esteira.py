class Produto:
    def __init__(self, codigo = 0, proximo_nodo = None):
        self.codigo = codigo
        self.proximo_nodo = proximo_nodo

    def __repr__(self):
        return f"Produto(codigo={self.codigo}, proximo_nodo={self.proximo_nodo})"
    

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"ListaEncadeada(head={self.head})"
    
    def inserir_produto(self, codigo):
        novo_produto = Produto(codigo)
        if self.head is None:
            self.head = novo_produto
        else:
            ultimo_produto = self.head
            while ultimo_produto.proximo_nodo is not None:
                ultimo_produto = ultimo_produto.proximo_nodo
            ultimo_produto.proximo_nodo = novo_produto