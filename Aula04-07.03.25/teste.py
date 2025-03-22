# Função para calcular a raiz quadrada sem usar math
def raiz_quadrada(n):
    if n < 0:
        return None  # Retorna None se tentar tirar a raiz de um número negativo
    epsilon = 0.000001  # Precisão da raiz quadrada
    guess = n / 2.0  # Chute inicial
    while abs(guess * guess - n) > epsilon:
        guess = (guess + n / guess) / 2.0
    return guess

# Função para calcular as raízes usando a fórmula de Bhaskara
def bhaskara(a, b, c):
    # Calculando o discriminante (Δ)
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Não existem raízes reais."
    elif delta == 0:
        x = -b / (2 * a)
        return f"A equação tem uma raiz real: x = {x:.2f}"
    else:
        # Calculando as duas raízes reais
        raiz_delta = raiz_quadrada(delta)
        if raiz_delta is None:
            return "Não existem raízes reais."
        
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        return f"As raízes reais são: x1 = {x1:.2f} e x2 = {x2:.2f}"

# Solicitar os coeficientes ao usuário
print("Resolução de equação do segundo grau (ax² + bx + c = 0)")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verificar se o valor de 'a' é zero (não é uma equação do segundo grau)
if a == 0:
    print("O valor de 'a' não pode ser zero em uma equação do segundo grau.")
else:
    # Chamar a função para calcular as raízes
    resultado = bhaskara(a, b, c)
    print(resultado)
