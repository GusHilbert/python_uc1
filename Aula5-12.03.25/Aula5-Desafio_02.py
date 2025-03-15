nota = int(input("Qual é a sua nota? "))
trabalho = input("Houve um trabalho extra? (s/n) ")
trabalho=trabalho.lower()
if (nota >= 7) or (trabalho == "s"):
    print("Aprovado")
else:
    print("Reprovado")