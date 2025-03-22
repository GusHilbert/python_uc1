# 🔢 Soma de números:
# 🔖 Use um while para somar números até que o usuário digite 0.

numero = int(input("Digite um número: "))
listNum = []

while numero != 0:
    listNum.append(numero)
    numero = int(input("Digite um número: "))
print(f"A somatória de todos os números que vc digitou foi de {sum(listNum)}")