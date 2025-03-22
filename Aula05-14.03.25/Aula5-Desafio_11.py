# 🔢 Promoção de Compras 🛍️
# Dê desconto se:
# ✅ O cliente gastou mais de R$100 ou
# ✅ Comprou mais de 5 produtos.

listaProd = []
valorProd = []

prod = input("Qual foi o produto? ")
valor = float(input("Qual foi o valor do produto? "))

listaProd.append(prod)
valorProd.append(valor)
fim = "n"
fim = input("Foram todos os produtos? (s/n) ").lower()

while fim == "n":
    prod = input("Qual foi o produto? ")
    valor = float(input("Qual foi o valor do produto? "))
    
    listaProd.append(prod)
    valorProd.append(valor)

    valorTotal = sum(valorProd)
    fim = input("Foram todos os produtos? (s/n) ").lower()

    if fim == "s":
        cupom = input("Você usou cupom na última compra? (s/n)").lower()
        if len(listaProd)>= 5 or valorTotal >=100 or cupom == "n":
            print(f"""
                  Parábéns!!!!!
                  Você ganhou desconto de 10%!!!
                  Os seus produtos: {listaProd}, no valor total de: R${valorTotal:.2f} 
                  Você pagará apenas R${valorTotal*0.9:.2f}""")
        else:
            print("\n")
            for item in range (len(listaProd)):
                print (f" {item+1} - {listaProd[item]} no valor de: R$ {valorProd[item]}")
            print(f"\nTotalizando {len(listaProd)} produto(s) com valor total de R$ {valorTotal:.2f}\n")   


