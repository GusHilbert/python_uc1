# 2️⃣ Contador de Palavras
# 🐍 Desenvolva um programa que receba um texto como argumento da linha de comando e use uma função 
# para contar quantas palavras existem no texto. A função main() deve chamar essa função e exibir o resultado.

# import sys


# def contagem ():


# if __name__ == "__main__":
#     argumentos = sys.argv[1:]
#     print ()


import sys

def contar_palavras(texto):
    """Conta quantas palavras existem no texto fornecido."""
    palavras = texto.split()
    return len(palavras)

def main():
    # Verifica se o texto foi passado como argumento da linha de comando
    if len(sys.argv) < 2:
        print("Por favor, forneça o texto como argumento da linha de comando.")
        return

    # Junta todos os argumentos em uma única string (caso haja múltiplas palavras)
    texto = " ".join(sys.argv[1:])
    
    # Chama a função contar_palavras e exibe o resultado
    total_palavras = contar_palavras(texto)
    print(f"O texto contém {total_palavras} palavras.")

if __name__ == "__main__":
    main()