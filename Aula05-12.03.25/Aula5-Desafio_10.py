# 🔟 Par ou Ímpar e Positivo ou Negativo? 🔢
# Crie um programa que peça um número e informe:
# ✅ Se ele é par ou ímpar e
# ✅ Se é positivo ou negativo.

n1 = int(input("Diga um número: "))
if (n1 > 0) and (n1%2>0):
    print("O número é positivo e ímpar")
elif (n1> 0):
    print("O número é positivo e par")
elif n1 <0 and (n1%2>0):
    print("O número é negativo e ímpar")
elif n1 <0 :
    print("O número é negativo e par")
else:
    print("O número é zero")