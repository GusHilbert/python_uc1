# 7️⃣ Calcular o fatorial de um número usando while
# 🔖 O programa deve obter um número e em seguida imprimir o valor do fatorial

numero = float(input("Digite o seu número aqui: "))

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1
print(f"O fatorial de {numero:.2f} é {fatorial:.2f}")