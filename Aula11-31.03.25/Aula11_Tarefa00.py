pessoas = {"nome":"Papagaio","idade":49,"cidade":"Petropolis"}
dados_atualizados = pessoas
dados_atualizados["idade"] = 59
dados_atualizados["email"] = "papagaio@gmail.com"
dados_atualizados["sexo"] = "m"
del dados_atualizados["nome"]
del dados_atualizados["email"]


for i in dados_atualizados:
    print(f"Dados da pessoa: {i} - {dados_atualizados[i]}")