A = float(input("Coloque o valor inicial: "))
B = float(input("Coloque a taxa de juros (em %): "))
C = float(input("Coloque o tempo em meses: "))

calculo = A * ((1+(B/100))**C)

print(f"A montante final é: {calculo:.2f}")