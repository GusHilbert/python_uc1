def saudacao():
    
    return print("Olá, seja bem-vindo(a) ao curso de Python!")
    
def soma(a,b):
    return soma(5,7)

def fatorial (n):
    if n<0:
        return "Número inválido para fatorial"
    elif n==0:
        return 1
    else:
        resultado = 1
        for i in range (1,n+1):
            resultado *= i
        return resultado

def pergunta():
    numero = int(input("Coloque o seu número: "))

# _________________________________________________________________________________

# def testeSaudacao():
#     saudacao()

# def testeSoma ():
#     resultado = soma(5,7)
#     print("A soma é: ",resultado)

# def testePergunta():
#     pergunta()

def testeFatorial ():
    numero = int(input("Coloque o seu número: "))
    print (f"O fatorial de {numero} é {fatorial(numero)}")


if __name__ == "__main__":
    # testeSaudacao()
    # print (f"O somatório é {resultado}")
    # testeSoma()
    # testePergunta()
    testeFatorial()
