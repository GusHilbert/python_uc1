# 7 Crie um programa que:
# ✅ Peça a idade do usuário.
# ✅ Se tiver 18 anos ou mais, pode viajar sozinho.
# ✅ Se tiver 16 ou 17, pode viajar com autorização dos pais.
# ✅ Se tiver menos de 16, não pode viajar sozinho.
# 💡 Extra: Use input() para perguntar se os pais autorizaram (s/n).

idade = int(input("Qual é a sua idade? "))


if idade >= 18:
    print("Você pode viajar!")
elif idade >= 16:
    autorizacao = input ("Você tem autorização dos seus pais? (s/n)")
    if autorizacao == "s":
        print("Você pode viajar!")
    else:
        print("Você não pode viajar ;/")
else:
    print("Você não pode viajar ;/")