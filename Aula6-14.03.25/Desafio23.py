# 🔢 Adivinhe o número
# 🔖 Crie um jogo onde o usuário tenta adivinhar um número secreto (use while e break).

import random

i = float(random.random()*10)
i = int(i)

numero = int(input("Adivinhe o número: "))
while numero != i:
    numero = int(input("Adivinhe o número: "))
print("Parabéns, vc acertou o número!")