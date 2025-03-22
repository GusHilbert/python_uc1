# 🔢 Criar um programa que imprima uma tabela de multiplicação de 1 a 5 (sem usar o range).
# 🔖 Imprima a tabuada do 1 até o 5, sem utilizar a função range().

i = 1

while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i * j:4}", end="")
        j+=1
    print()
    i+=1

    