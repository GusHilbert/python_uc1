# 🔢 Imprimir uma tabela de multiplicação (aninhando loops)
# 🔖 Elabore um código para imprimir a tabela de multiplicação dos números de 1 até 10


for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
