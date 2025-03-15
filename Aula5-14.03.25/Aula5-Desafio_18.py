# 🔢 Maior de Três Números 🔢
# Peça três números e exiba o maior deles.

listnum =[]
num = int(input("Me fale um número "))
listnum.append(num)
num = int(input("Me fale um número "))
listnum.append(num)
num = int(input("Me fale um número "))
listnum.append(num)

print(max(listnum))