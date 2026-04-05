class Busca:
    @staticmethod
    def sequencial(lista, alvo):
        for i in range(len(lista)):
            if lista[i] == alvo:
                return i
        return -1
    
    @staticmethod
    def binaria(lista, alvo):
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if lista[meio] == alvo:
                return meio
            elif lista[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1

        return -1

    @staticmethod
    def hash(dicionario, chave):
        return dicionario.get(chave, "Não encontrado")
    
# Exemplos de uso
# lista = [1, 3, 5, 7, 9, 11, 13]
# tabela = {v: i for i, v in enumerate(lista)}
# Busca.sequencial(lista, 3)
# Busca.binaria(lista, 3)
# Busca.hash(tabela, 3)
