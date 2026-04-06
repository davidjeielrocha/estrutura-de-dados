class Ordena:
    @staticmethod
    def bolha(lista):
        n = len(lista)    
        for i in range(n):
            # Flag para otimização (se não houver troca, já está ordenado)
            trocou = False
            print("Execução: ", i + 1)
            
            for j in range(0, n - i - 1):
                print("Compara: ", lista[j], " com ", lista[j + 1])
                if lista[j] > lista[j + 1]:
                    # Troca os elementos
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            
            # Se não houve troca, a lista já está ordenada
            if not trocou:
                break
        
        return lista
    
    @staticmethod
    def selecao(lista):
        n = len(lista)
        
        for i in range(n):
            # Assume que o menor elemento está na posição atual
            menor_indice = i
            print("Execução: ", i + 1)
            # Procura o menor elemento no restante da lista
            for j in range(i + 1, n):
                print("Compara se ", lista[j], " > ", lista[menor_indice])
                if lista[j] < lista[menor_indice]:
                    menor_indice = j
            
            # Troca o menor elemento encontrado com o elemento atual
            print("Substitui o índice ", i, " pelo ", menor_indice)
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
        
        return lista

    @staticmethod
    def insercao(lista):
        # Começa do segundo elemento (índice 1)
        for i in range(1, len(lista)):
            print("Execução: ", i + 1)
            chave = lista[i]  # valor atual a ser inserido
            j = i - 1

            # Move os elementos maiores para frente
            while j >= 0 and lista[j] > chave:
                print("Caso ", j, " >= 0 ", "e ", lista[j], " > ", chave)
                print( lista[j + 1], " = ", lista[j])
                lista[j + 1] = lista[j]
                j -= 1

            # Insere o valor na posição correta
            lista[j + 1] = chave

        return lista
    
    @staticmethod
    def seleciona_mistura(lista):
        # Caso base (lista com 1 elemento já está ordenada)
        if len(lista) <= 1:
            return lista

        # Divide a lista no meio
        meio = len(lista) // 2
        esquerda = Ordena.seleciona_mistura(lista[:meio])
        direita  = Ordena.seleciona_mistura(lista[meio:])

        # Junta (mistura) as duas partes ordenadas
        return Ordena.mistura(esquerda, direita)

    @staticmethod
    def mistura(esquerda, direita):
        resultado = []
        i = j = 0

        # Compara os elementos das duas listas
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

        # Adiciona o que sobrou (se sobrar)
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])

        return resultado

    @staticmethod
    def rapido(lista):
        # Caso base
        if len(lista) <= 1:
            return lista

        # Escolhe o pivô (aqui usamos o elemento do meio)
        indice_pivo = len(lista) // 2
        pivo = lista[indice_pivo]
        print("Pivô escolhido: ", pivo, " no índice: ", indice_pivo)

        # Divide a lista em três partes considerando índices
        menores = [lista[i] for i in range(indice_pivo) if lista[i] < pivo]
        iguais = [x for x in lista if x == pivo]
        maiores = [lista[i] for i in range(indice_pivo + 1, len(lista)) if lista[i] > pivo]
        
        # Elementos à esquerda que são >= pivô (devem ir para direita)
        esquerda_maior = [lista[i] for i in range(indice_pivo) if lista[i] > pivo]
        # Elementos à direita que são < pivô (devem ir para esquerda)
        direita_menor = [lista[i] for i in range(indice_pivo + 1, len(lista)) if lista[i] < pivo]
        
        print("Menores que o pivô: ", menores)
        print("Iguais ao pivô: ", iguais)
        print("Maiores que o pivô: ", maiores)

        # Aplica recursão
        return Ordena.rapido(menores + direita_menor) + iguais + Ordena.rapido(esquerda_maior + maiores)


lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original: ", lista)
# print("Lista ordenada (Bolha): ", Ordena.bolha(lista.copy()))
# print("Lista ordenada (Seleção): ", Ordena.selecao(lista.copy()))
# print("Lista ordenada (Inserção): ", Ordena.insercao(lista.copy()))
# print("Lista ordenada (Mistura): ", Ordena.seleciona_mistura(lista.copy()))
print("Lista ordenada (Rápida): ", Ordena.rapido(lista.copy()))