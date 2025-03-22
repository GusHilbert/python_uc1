# 🔢 Criar um programa que peça ao usuário para digitar uma sequência de números até que ele digite um número maior que 100.
# 🔖 O programa deve contar quantos números foram digitados antes do número maior que 100 ser inserido.

numero = int(input("Digite um número: "))
listnumero = []

while numero < 100:
    listnumero.append(numero)
    numero = int(input("Digite um número: "))
listnumero.append(numero)
tamanho = len(listnumero)
print(f"Seu número {numero} é maior do que 100, vc digitou o total de {tamanho} números ")