# 🔢 Imprimir uma sequência de números e seus cubos
# 🔖 Elabore um programa que leia um número, em seguida deve-se imprimir os cubos de 1 até o numero lido


numero = int(input("Coloque um número: "))
dife = numero
i = 1

while i in range(numero+1):
    print(f"O número é {i} e seu cubo é {i**2}")
    i+=1