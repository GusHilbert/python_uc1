# 🔢 Tabuada
# 🔖 Peça um número ao usuário e mostre a tabuada de 1 a 10 usando um for.

numero = int(input("Insira um número: "))


for i in range(10):
    print(f"{i+1} x {numero} = {(i+1) * numero}")