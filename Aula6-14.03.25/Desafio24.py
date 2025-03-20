# 🔢 Fatorial:
# 🔖 Calcule o fatorial de um número usando um for.


numero = int(input("Digite o seu número aqui: "))
fatorial = 1
contador = numero
lista =[]

for i in range (1,numero+1):
    fatorial=contador
    contador -=1
print(f"O fatorial de {numero:.2f} é {sum(lista):.2f}")