# 🔢 Menu interativo
# 🔖 Crie um menu que repete até o usuário escolher "sair" (use while).

exercicio = []
duvida = []
erro = []

print("""Oque vc deseja fazer:
      1 - Enviar um exercício
      2 - Enviar uma dúvida
      3 - Enviar um erro
      4 - Saír
      """)
resposta = input("Digite o número relativo a sua solicitação: ")

while resposta != "4":
    if resposta == "1":
        print("Seu exercício foi enviado")
        print("""
        Oque vc deseja fazer agora:
        1 - Enviar um exercício
        2 - Enviar uma dúvida
        3 - Enviar um erro
        4 - Saír
        """)
        resposta = input("Digite o número relativo a sua solicitação: ")
        exercicio.append(resposta)
    elif resposta =="2":
        print("Sua dúvida foi enviada")
        print("""
        Oque vc deseja fazer agora:
        1 - Enviar um exercício
        2 - Enviar uma dúvida
        3 - Enviar um erro
        4 - Saír
        """)
        resposta = input("Digite o número relativo a sua solicitação: ")
        duvida.append(resposta)
    elif resposta == "3":
        print("Seu erro foi enviado")
        print("""
        Oque vc deseja fazer agora:
        1 - Enviar um exercício
        2 - Enviar uma dúvida
        3 - Enviar um erro
        4 - Saír
        """)
        resposta = input("Digite o número relativo a sua solicitação: ")
        erro.append(resposta)

if len(exercicio) ==0 and len(duvida) == 0 and len(erro) == 0: 
    print("""
Desculpa não poder ter te ajudado =/
Até a próxima""")
elif len(exercicio) !=0 and len(duvida) != 0 and len(erro) != 0: 
    print("""
Todas as suas solicitações foram enviadas!!!
Até a próxima""")    
elif len(exercicio) !=0 and len(duvida) != 0 and len(erro) == 0: 
    print("""
Seu exercício e dúvida foram enviados com sucesso =)
Até a próxima""")
elif len (exercicio) ==0 and len (duvida) != 0 and len(erro) != 0: 
    print("""
Sua dúvida e erro foram enviados com sucesso =)
Até a próxima""")
elif len (exercicio) !=0 and len (duvida) == 0 and len(erro) != 0: 
    print("""
Seu exercício e erro foram enviados com sucesso =)
Até a próxima""")
elif len (exercicio) !=0 and len (duvida) == 0 and len(erro) == 0: 
    print("""
Seu exercício foi enviado com sucesso =)
Até a próxima""")
elif len (exercicio) ==0 and len (duvida) != 0 and len(erro) == 0: 
    print("""
Sua dúvida foi enviada com sucesso =)
Até a próxima""")
elif len (exercicio) ==0 and len (duvida) == 0 and len(erro) != 0: 
    print("""
Seu erro foi enviado com sucesso =)
Até a próxima""")