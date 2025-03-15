# 8️⃣ Pode Dirigir? 🚗
# Crie um programa que pergunte a idade e se a pessoa possui carteira de motorista (s/n).
# ✅ Se tiver 18 anos ou mais e tiver carteira, pode dirigir.
# ✅ Caso contrário, não pode.


idade=int(input("Coloque a sua idade: "))
tem_carteira=input("Tem carteira (s/n): ")
tem_carteira=tem_carteira.lower()

if(idade>=18) and (tem_carteira == "s"):
    print("Você pode dirigir!")
elif idade<18:
    print("Você não tem idade para dirigir")
else:
    print("Você não tem carteira")