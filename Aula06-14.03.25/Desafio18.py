# 🔢 Imprimir o somatório de todos os números pares de 1 a 100.
# 🔖 Crie um programa que calcule a soma dos números pares entre 1 e 100.

lisnumero = []
i = 1

while i <= 100:
    if i%2 == 0:
        lisnumero.append(i)
        i+=1
    else:
        i+=1
print(sum(lisnumero))