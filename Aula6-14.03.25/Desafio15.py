# 🔢 Imprimir os números de 1 a 20 e verificar se são múltiplos de 3 ou 5.
# 🔖 Para cada número de 1 a 20, imprima se o número é múltiplo de 3, de 5 ou de ambos.

i=1

while i <= 20:
    if i%3 ==0:
        print(f"{i} é múltiplo de 3")
    elif i%5 == 0:
        print(f"{i} é múltiplo de 5")
    i+=1