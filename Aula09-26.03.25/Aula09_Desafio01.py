
def soma_elementos():
# 1️⃣ Soma de Elementos
# 📚 Crie um programa que recebe 5 números inteiros do usuário e os armazena em uma lista. Depois, calcule e exiba a soma de todos os elementos.
     i=0
     lista = []
     while i<=4:
        pergunta = int(input("Fale um número: "))
        lista.append(pergunta)
        i+=1
     print(f"O total dos números é {sum(lista)}")
     print(lista)

def impares():
# 2️⃣ Números Ímpares de um Intervalo
# 📚 Utilizando a função range(), crie uma tupla contendo todos os números ímpares de 1 a 50 e exiba essa tupla.

    listaPar=[]
    listaImpar=[]

    for i in range(1,51):
         if i%2==0:
            listaPar.append(i)
         else:
            listaImpar.append(i)

    print(f"Os números pares são: {listaPar}\n Os números ímpares são: {listaImpar}")

def ordem():
# 3️⃣ Inserção Ordenada
# 📚 Crie um programa que permita ao usuário inserir 5 números inteiros em uma lista, garantindo que a inserção ocorra de forma ordenada sem utilizar sort().
     i=0
     lista = []
     while i<=4:
        pergunta = int(input("Fale um número: "))
        lista.append(pergunta)
        i+=1

def ocorrencia():
# 4️⃣ Contagem de Ocorrências
# 📚 Crie um programa que armazena uma tupla com 10 números aleatórios entre 1 e 5. 
# Depois, peça ao usuário para digitar um número e informe quantas vezes ele aparece na tupla.
    import random 
    i = 0
    lista=[]
    while i <= 9:
        aleatorio = random.randrange(1, 5, 1)
        lista.append(aleatorio)
        print(aleatorio)
        i+=1
    pergunta = int(input("Fale um número de 1 à 5: "))
    cont = lista.count(pergunta)
    print(f"Seu número {pergunta} aparece {cont} vezes.")

def duplicada():
# 5️⃣ Remoção de Duplicatas
# 📚 Crie um programa que recebe 10 números inteiros e os armazena em uma lista. Depois, remova os elementos duplicados, mantendo apenas um de cada.

    i=0
    lista=[]
    while i<=9:
        pergunta = int(input("Digite um número: "))
        lista.append(pergunta)
        i+=1
    lista=list(dict.fromkeys(lista))

    print(lista)

def estatistica():
# 6️⃣ Estatísticas de uma Lista
# 📚 Solicite ao usuário 10 números inteiros e armazene-os em uma lista. Depois, exiba o maior, o menor, a média e a mediana dos valores.
    
    lista = []
    for i in range (1,10):
        pergunta = int(input(f"Fale um número"))
        lista.append(pergunta)
    print(f"O maior número é o {max(lista)} \nO me")


if __name__ == "__main__":
    # soma_elementos()
    # impares()
    # ordem() <falta
    # ocorrencia()
    # duplicada()
    estatistica() # <falta terminar