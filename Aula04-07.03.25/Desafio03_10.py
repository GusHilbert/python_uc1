# Crie um programa que converta um valor em reais para dólares. Peça ao usuário a cotação do dólar e o valor em reais.
A = float(input("Coloque a cotação do Dolar: "))
B = float(input("Coloque o valor em reais: "))

calculo = B / A 

print(f"O valor convertido em Dólares é: {calculo:.2f}")