# 🔢 Números primos
# 🔖 Verifique se um número é primo usando um for e break.

numero = int(input("Digite o seu número aqui: "))
lista = []
for i in range (1,numero+1):
    if numero%(i+1) == 0:
        lista.append(i+1)
if len(lista) >= 2:
    print(f"O {numero} não é primo, ele é divisivel pelos números: ",lista)
else:
    print(f"O número {numero} é primo")

