class Deque: 
    def __init__(self): 
        self.items = [] 
 
    def estaVazio(self): 
        return self.items == [] 
 
    def adicionaFrente(self, item): 
        self.items.append(item) 
 
    def adicionaAtras(self, item): 
        self.items.insert(0,item) 
 
    def removeFrente(self): 
        return self.items.pop() 
 
    def removeAtras(self): 
        return self.items.pop(0) 
 
    def size(self): 
        return len(self.items) 
         
# Função que checa se é palíndrome  
def ePalindrome(aString): 
    chardeque = Deque() 

    for ch in aString: # adiciona caracter por caracter 
        chardeque.adicionaAtras(ch) 

    stillEqual = True # inicializa stillEqual object como True 

    while chardeque.size() > 1 and stillEqual:  
    # enquanto o tamanho for >1 e stillEqual for True 
        first = chardeque.removeFrente() # remove da parte da frente 
        last = chardeque.removeAtras() # remove da parte de trás 
        if first != last: # se o caracter da frente não form igual ao de trás 
            stillEqual = False # não é Palindrome 

    return stillEqual 
 
print(ePalindrome("mirim")) 
print(ePalindrome("asdfgh")) 
print(ePalindrome("radar")) 
print(ePalindrome("123321"))