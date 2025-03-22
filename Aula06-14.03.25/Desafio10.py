# 🔟 Senha correta e repetição até acertar
# 🔖 Elabore um código que solicite a senha do usuário, deve-se solicitar a senha até que o valor
#    informando seja igual ao conteúdo da constante "SENHA"

senha = input("Escreva sua senha: ").upper() 

while senha != "SENHA":
    senha = input("Escreva sua senha: ").upper() 
print("Você está logado")