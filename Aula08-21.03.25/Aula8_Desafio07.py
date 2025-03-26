import sys

# def calculadora(a,b,c):
#     calculo = "a c b"
    

# def testeCalculadora():
#     n1 = int(input("N1: "))
#     n2 = int(input("N2: "))
#     operacao = (input("Qual é a operação: (+,-,*,/)"))


def calculadora (n1,op,n2):
    if op == "-":
        calculo = n1 - n2
        return calculo
    elif op == "+":
        calculo = n1 + n2
        return calculo
    elif op == "*":
        calculo = n1 * n2
        return calculo
    elif op == "/":
        calculo = n1 / n2
        return calculo
    else:
        return print("Essa operação não existe")


if __name__ == "__main__":
    argumentos = sys.argv[1:]
    num1 = float(argumentos[0])
    num2 = float(argumentos[2])
    operacao = argumentos [1]
    print (calculadora(num1,operacao,num2))