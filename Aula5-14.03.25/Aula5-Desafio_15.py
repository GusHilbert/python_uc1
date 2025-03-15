# 🔢 Qual Tipo de Triângulo? 🔺
# Peça três lados de um triângulo e informe:

# Equilátero (todos iguais)
# Isósceles (dois iguais)
# Escaleno (todos diferentes)

lado1 = float(input("Me fala o primeiro lado do triângulo? "))
lado2 = float(input("Me fala o segundo lado do triângulo? "))
lado3 = float(input("Me fala o terceiro lado do triângulo? "))

if lado1 == lado2 == lado3:
    print("Esse triângulo é equilatero!")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Esse triângulo é isosceles!")
else:
    print("Esse triângulo é escaleno")