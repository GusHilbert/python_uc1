idade = int(input("Qual é a sua idade? "))
senha = input("Qual é a sua senha? ")

if (idade >= 18) and (senha == "123456Ab!"):
    print("Acesso aprovado")
else:
    print("Acesso negado")