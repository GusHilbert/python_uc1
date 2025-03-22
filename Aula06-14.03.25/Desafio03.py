# 3️⃣ Imprimir Números pares e impares
# 🔖 Elabore um código para imprimir todos os números pares e ímpares de 1 a 20 usando for

for item in range(20):
    if (item+1)%2 ==1:
        print(item+1, "- este número é ímpar")
    else:
        print(item+1, " - Este número é par")