# 🔢 Pode Fazer Empréstimo? 💰
# A pessoa só pode pegar um empréstimo se:

# Tem mais de 21 anos
# Tem renda maior que R$2000
# Não tem nome sujo

idade = int(input("Qual é a sua idade? "))
renda = float(input("Qual é a sua renda?"))
sujo = input("Você tem o nome sujo? (s/n)").lower()

if idade >=18 and renda >= 2000 and sujo == "n":
    print("Pode fazer empréstimo!")
else:
    print("Não pode fazer o empréstimo ")