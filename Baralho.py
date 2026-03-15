class Baralho:
    NAIPES = ["Espadas", "Copas", "Ouros", "Paus"]
    VALORES = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

    def __init__(self):
        self.cartas_por_naipe = {naipe: [] for naipe in self.NAIPES}
        self.baralho_completo = []
        for naipe in self.NAIPES:
            for valor in self.VALORES:
                carta = {"naipe": naipe, "valor": valor}
                self.cartas_por_naipe[naipe].append(carta)
                self.baralho_completo.append(carta)
                
    def selecionar_por_naipe_e_valor(self, naipe, valor):
        # Seleciona cartas de um naipe e valor específico
        return [carta for carta in self.cartas_por_naipe.get(naipe, []) if carta["valor"] == str(valor)]
    
    def selecionar_por_numero(self, numero):
        # Seleciona todas as cartas de um número específico (ex: todas as cartas 10 de todos os naipes)
        valor = str(numero)
        return [carta for carta in self.baralho_completo if carta["valor"] == valor]

    def selecionar_por_naipe(self, naipe):
        return self.cartas_por_naipe.get(naipe, [])

    def selecionar_por_valor(self, valor):
        return [carta for carta in self.baralho_completo if carta["valor"] == valor]

    def selecionar(self, filtro):
        # filtro deve ser uma função que recebe uma carta e retorna True/False
        return [carta for carta in self.baralho_completo if filtro(carta)]

    def __str__(self):
        return str(self.baralho_completo)

# # Exemplo de uso:
# baralho = Baralho()
# print("Baralho Completo:", baralho.baralho_completo)
# print("Cartas de Copas:", baralho.selecionar_por_naipe("Copas"))
# print("Cartas de valor K:", baralho.selecionar_por_valor("K"))
# print("Carta número 10:", baralho.selecionar_por_numero(9))