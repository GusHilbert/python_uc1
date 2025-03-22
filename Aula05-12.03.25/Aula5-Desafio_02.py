nota = int(input("Qual é a sua nota? "))
nota2 = int(input("Qual é a sua outra nota? "))
media = (nota+nota2)/2
trabalho = input("Houve um trabalho extra? (s/n) ")
trabalho=trabalho.lower()
if (media >= 7) or (trabalho == "s"):
    print("Aprovado")
else:
    print("Reprovado")