
class FilaPrioritariaBanco:
    PRIORIDADES = [
        "deficiencia",
        "lactante",
        "gestante",
        "crianca_de_colo",
        "obesidade",
        "normal"
    ]

    def __init__(self):
        self.filas = {prioridade: [] for prioridade in self.PRIORIDADES}
        self.senha_counter = 1
        self.atendendo = None

    def gerar_senha(self, nome, prioridade):
        prioridade = prioridade.lower()
        if prioridade not in self.PRIORIDADES:
            prioridade = "normal"
        senha = f"{prioridade[:3].upper()}-{self.senha_counter:04d}"
        self.filas[prioridade].append({"nome": nome, "senha": senha, "prioridade": prioridade})
        self.senha_counter += 1
        return senha

    def proximo_atendimento(self):
        for prioridade in self.PRIORIDADES[:-1]:  # Prioridades primeiro
            if self.filas[prioridade]:
                self.atendendo = self.filas[prioridade].pop(0)
                return self.atendendo
        # Se não houver prioritários, atende normal
        if self.filas["normal"]:
            self.atendendo = self.filas["normal"].pop(0)
            return self.atendendo
        self.atendendo = None
        return None

    def fila_atual(self):
        return {p: list(self.filas[p]) for p in self.PRIORIDADES}

    def __str__(self):
        return str(self.fila_atual())

# Exemplo de uso:
# fila = FilaPrioritariaBanco()
# senha1 = fila.gerar_senha("Maria", "gestante")
# senha2 = fila.gerar_senha("João", "normal")
# senha3 = fila.gerar_senha("Ana", "deficiencia")
# print(fila)
# print("Atendendo:", fila.proximo_atendimento())
# print("Atendendo:", fila.proximo_atendimento())
# print(fila)
