
vetor = [1,2,3,4,5,6,7,8,9,10]

def calcularSomaDosVetores(lista):
    aux = 0;
    for num in lista:
        aux = aux + num*num
    print(aux)
        
        
calcularSomaDosVetores(vetor)