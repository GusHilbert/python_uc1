# 🔢 Verificador de Votação 🗳️
# Peça a idade e verifique se o usuário pode votar:

# Obrigatório (18 a 69 anos)
# Opcional (16, 17 ou 70+)
# Proibido (menor de 16)

idade = int(input("Qual é a sua idade? "))

if idade >= 18 and idade <= 69:
    print("Você pode votar")
elif idade >= 16 or idade >= 70:
    print("Você pode votar ou não")
else:
    print("Você não pode votar")
