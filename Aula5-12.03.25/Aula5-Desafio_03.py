idade=int(input("Coloque a sua idade: "))
acompanhado=input("Está acompanhado (s/n): ")
acompanhado=acompanhado.lower()

if(idade>=18) or (acompanhado == "s"):
    print("Você pode entrar!")
else:
    print("Você não tem idade e nem está acompanhado")