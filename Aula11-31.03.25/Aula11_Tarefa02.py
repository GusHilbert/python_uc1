
d3 = d1 = {"a":1,"b":2} # o D3 se atualiza automáticamente quando altera o d1
d2 = {"c":3,"d":4}
d4={"a":100,"b":9,"e":8888}

dici2 = {**d1,**d2}


print("Dicionários Originais")
print("Dicionário 1", d1)
print("Dicionário 2",d2)

d1.update(d2)
d2.update(d3)
def teste():
    d1.update(d4)
    print("Última etapa: ",d1)


print("Dicionários Atualizado")
print("Dicionário 1", d1)
print("Dicionário 2",dici2)
print("Dicionário 3",d2)

if len(d1)>=1:
    teste()

if d1 == d3:
    print("d3 e d1 são iguais")
    print("D3: ", d3)
    print("D1: ", d1)