# 🔢 Ano Bissexto? 📅
# Peça um ano e diga se ele é bissexto.
# ✅ Um ano é bissexto se for divisível por 4 e não for divisível por 100, a menos que também seja divisível por 400.

ano = int(input("Digite um ano: "))

if (ano%4 == 0 and ano%100 !=0) or ano%400 == 0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")
