# 🔢 Números pares
# 🔖 Use um for para imprimir todos os números pares de 1 a 20.

for i in range(1,21):
    if i%2 == 0:
        print(i)
        i+=1
    else:
        continue