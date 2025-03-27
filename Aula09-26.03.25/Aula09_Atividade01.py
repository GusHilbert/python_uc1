vetor = [10, 20, 30, 40, 50]


def imprimir_vetor (vet):
    print("Vetor:", vet)


def imprimir_elemento(vet):
    for elemento in vet:
        print("Elemento", elemento)

def somar_elementos(vet):
    soma=sum(vet)
    print("Soma dos elementos: ",soma)

vetor1 = [3, 7, 2, 9, 4]

def maior_menor(vet):
    maior = max(vet)
    menor = min(vet)
    print("O maior valor é:",maior)
    print("O menor valor é:",menor)

vetor2 = [1, 2, 3, 4, 5]

def vetor_invertido(vet):
    vetorInvert= vet[::-1]
    print("O vetor invertido é:",vetorInvert)

def multiplicador(vet):
    multi = 2
    for element in vet:
        vetorMult = element *  multi
        print("Vetor multiplicado:", vetorMult)

vetor3 = [1, 3, 3, 4, 3, 5]

def ocorrencias(vet):
    ocorre = vet.count(3)
    print ("O valor 3 aparece",ocorre,"vezes")
    
vetor4 = [5, 2, 9, 1, 5, 6]

def ordem(vet):
    vetorOrdenado = sorted(vet)
    print("O vetor ordenado é:",vetorOrdenado)

vetor5 = [1, 2, 2, 3, 4, 4, 5]

def duplicadas(vet):
    vetorSem = list(dict.fromkeys(vet))
    print("Vetor sem duplicadas:",vetorSem)

vetor6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def par_impar(vet):
     x = [i for i in range(10) if i%2 == 1]
     print(x)


    #   for num in vet:
    #     if num%2 == 1:
    #         print("O número", num,"é par")
    #     else:
    #         print("O número", num,"é ímpar")

def media(vet):
    med=sum(vet)/len(vet)
    for i in vet:
        if i > med:
            print("O número",i,"é maior do que a média",med)
        else:
            print("O número",i,"é menor do que a média",med)



if __name__ == "__main__":
    # imprimir_vetor(vetor)
    # imprimir_elemento(vetor)
    # somar_elementos(vetor)
    # maior_menor(vetor1)
    # vetor_invertido(vetor2)
    # multiplicador(vetor2)
    # ocorrencias(vetor3)
    # ordem(vetor4)
    # duplicadas(vetor5)
    # par_impar(vetor6)
    media(vetor6)