A = float(input(""" Na equação de segundo grau (ax² + bx + c = 0).
                Coloque o valor de A: """))
B = float(input("Coloque o valor de B: "))
C = float(input("Coloque o valor de C: "))

calculoPos = (-B + (B**2)- ((4*A*C)**0.5))/(2*A)
calculoNeg = (-B - (B**2)- ((4*A*C)**0.5))/(2*A)

print(f"""O resultado positivo é: {calculoPos:.2f}
O resultado negativo é: {calculoNeg:.2f}  """)
