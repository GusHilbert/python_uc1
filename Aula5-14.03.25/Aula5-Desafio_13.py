# 🔢 Autorização de Entrada em um Evento 🎟️
# Para entrar em um evento, a pessoa precisa:
# ✅ Ter 18 anos ou mais OU
# ✅ Ter entre 16 e 17 anos e estar acompanhada

idade = int(input("Qual é a sua idade? "))
acompanhada = input("Está acompanhado(a)  (s/n)").lower()

if idade >= 18:
    print("Pode entrar no evento")
elif idade >= 16 and acompanhada == "s":
    print("Pode entrar no evento")
else:
    print("Não pode entrar no evento")