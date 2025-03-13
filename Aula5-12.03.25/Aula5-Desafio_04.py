import random

print("""Jogo de Adivinhação
      Pense em um número entre 0 e 10""")
#i = 6
i = float(random.random()*10)
i = int(i)
print(i)

t1=int(input("Qual é o seu primeiro número: "))
if t1 == i:
    print("Parabéns, vc acertou!!!!")
else:
    t2=int(input("Qual é o seu segundo número: "))
    if t2 == i:
        print("Parabéns, vc acertou na segunda tentativa!!!!")
    else:
        t3=int(input("Qual é o seu terceiro número: "))
        if t3 == i:
         print("Parabéns, vc acertou na terceira tentativa!!!!")
        else:
         print(f"Você não acertou, o número era {i}")
