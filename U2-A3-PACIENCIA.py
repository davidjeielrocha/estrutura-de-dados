# Naipes
Baralho = []
Espadas = []
Copas = []
Ouros = []
Paus = []

# Adicionando os números de 1 a 13 para cada naipe
for i in range(1, 14):
    if(i == 1):
        i = "A"
    elif(i == 11):  
        i = "J"
    elif(i == 12):
        i = "Q"
    elif(i == 13):
        i = "K"

    Espadas.append(i)
    Copas.append(i)
    Ouros.append(i)
    Paus.append(i)

Baralho.append({"Espadas": Espadas})
Baralho.append({"Copas": Copas})  
Baralho.append({"Ouros": Ouros})
Baralho.append({"Paus": Paus})

print("Baralho Completo:", Baralho)