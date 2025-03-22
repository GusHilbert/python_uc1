# 9️⃣ Login no Sistema 🔐
# Peça um usuário e uma senha. O login só será aceito se:
# ✅ O usuário for "admin" e a senha for "1234"

login = input("Coloque seu login: ")
senha = input("Coloque sua senha: ")
if (senha == "1234") and (login == "admin") :
    print("Acesso permitido")
else:
    print("Acesso negado")