nota1 = 1
nota2 = 2
nota3 = 3
nota4 = 4

provaFinal = 10

notas = [nota1,nota2,nota3,nota4]


def calculoMaluco(lista, prova):
    media = 0
    for num in lista:
        media += num
    media = media/4
    if (media >= 7):
        print ("Aprovado")
    else:
        media = 0
        for num in lista:
            media += num
        media += prova
        print(media)
        media = media/5
        if(media >= 5):
            print("Aprovado")
        else:
            print("Reprovado")

calculoMaluco(notas, provaFinal)