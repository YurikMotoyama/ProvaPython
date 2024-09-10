
biblioteca = []
biblioteca.append({"teste", "testeAutor"})

def addBook(biblioteca,nome,autor):
    biblioteca.append({nome, autor})

def listBook(biblioteca):
    
    for livro in biblioteca:
        print(livro)

def findBook(biblioteca, nome):
    aux = 0
    for livro in biblioteca:
        if(nome in biblioteca[aux]):
            print("Livro/Autor: ", biblioteca[aux])
        else:
            print("Livro não encontrado")
       
print("=========================================================================")       
print("Bem vindo a biblioteca blablabla selecione o pipipi do popopo:")
print("1: Adicionar livro")
print("2: Listar livros")
print("3: Buscar livro por titulo")
print("4: Sair")
print("=========================================================================") 



dentro = input()
if(dentro == 1):
    print("Qual o nome do livro?")
    nomeDoLivro = input()
    print("Qual o autor do livro?")
    autorDoLivro = input()
    addBook(biblioteca,nomeDoLivro,autorDoLivro)
elif(dentro == 2):
    listBook(biblioteca)
elif(dentro == 3):
    print("Qual o nome do livro que deseja buscar?")
    nomeDoLivro = input()
    findBook(biblioteca, nomeDoLivro)


