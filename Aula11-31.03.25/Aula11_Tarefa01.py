
d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4}
dici = d1.update(d2)
dici2 = {**d1,**d2}

print("Dicionário 1", dici)
print("Dicionário 2",dici2)