n1=input("Qual é o seu nome? ")
if len(n1) >=3:
    senha=input("Qual é a sua senha? ")
    if len(senha) >=6:
        if (senha == "123456") or (senha ==  "senha1"):
            print("Senha fraca")
        else:
            print("Parabéns, você está conectado")
    else:
        print("Sua senha tem menos de 6 caracteres")
else:
    print("Seu nome tem menos de 3 carácteres")





