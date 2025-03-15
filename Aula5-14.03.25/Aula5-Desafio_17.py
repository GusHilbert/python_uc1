# ✅ Pergunte a temperatura
# ✅ Se a temperatura for acima de 30°C, diga que está quente.
# ✅ Se for abaixo de 10°C, diga que está frio.
# ✅ Se estiver entre 10°C e 30°C, diga que está agradável.

temp = float(input("Qual é a temperatura? "))

if temp >= 30:
    print("Está quente")
elif temp <= 10:
    print ("Está frio")
else: print("Está agradável")