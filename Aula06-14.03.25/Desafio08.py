# 8️⃣ Soma de números positivos
# 🔖 Elabora um código para imprimir a soma de números positivos até um número negativo ser digitado


numero = int(input("Escreva um número: "))
adicao = 0


while numero >= 0:
    adicao += numero
    numero = int(input("Escreva um número: "))
print (adicao)
