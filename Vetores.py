numeros = list(range(10))

for n in range(len(numeros)):
    numeros[n]= int(input("Digite um número: "))

for n in range(0, 10):
    if n % 2 != 0:
        print(numeros[n])