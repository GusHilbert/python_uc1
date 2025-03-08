B = float(input("Coloque valor total da sua compra: "))
desc = B * 0.9
A = B - desc
print(f"""O seu valor à pagar é: {desc:.2f}
O valor do desconto é: {A:.2f}""")