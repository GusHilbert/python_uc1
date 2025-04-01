frase = "o rato roeu a roupa do rei de roma roma roma a"
palavras = frase.split()
palavras_2 = ["não","existe","nenhum","alimento","azul","existe"]
contagem = {}


for palavra in palavras:
    contagem[palavra] = contagem.get(palavra,0)+1

print(contagem)


contagem = {}
for palavra in palavras_2:
    contagem[palavra] = contagem.get(palavra,0)+1

print(contagem)