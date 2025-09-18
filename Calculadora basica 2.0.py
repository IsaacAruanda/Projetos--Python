import math

# Funções para operações
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y

def potenciacao(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Erro: número negativo não tem raiz quadrada real!"
    return math.sqrt(x)

def modulo(x):
    return abs(x)

def exponencial(x):
    return math.exp(x)

def logaritmo(x):
    if x <= 0:
        return "Erro: logaritmo só é definido para números positivos!"
    return math.log10(x)

def fatorial(x):
    if not x.is_integer() or x < 0:
        return "Erro: fatorial só é definido para inteiros não negativos!"
    return math.factorial(int(x))

# Dicionário para mapear operações
# Para funções com 2 números, a chave aponta pra função normal
# Para funções com 1 número, criaremos uma tupla (função, tipo = '1num')
operacoes = {
    "1": (adicao, '2num'),
    "2": (subtracao, '2num'),
    "3": (multiplicacao, '2num'),
    "4": (divisao, '2num'),
    "5": (potenciacao, '2num'),
    "6": (raiz_quadrada, '1num'),
    "7": (modulo, '1num'),
    "8": (exponencial, '1num'),
    "9": (logaritmo, '1num'),
    "10": (fatorial, '1num')
}

# Loop principal da calculadora
while True:
    print("\nEscolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação (x^y)")
    print("6 - Raiz Quadrada")
    print("7 - Módulo (valor absoluto)")
    print("8 - Exponencial (e^x)")
    print("9 - Logaritmo base 10")
    print("10 - Fatorial")
    print("0 - Sair")

    escolha = input("Digite o número da operação: ")

    if escolha == "0":
        print("Encerrando a calculadora. Até mais!")
        break

    if escolha not in operacoes:
        print("Operação inválida! Por favor, escolha uma opção válida.")
        continue

    funcao, tipo = operacoes[escolha]

    try:
        if tipo == '2num':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = funcao(num1, num2)
        else:  # tipo == '1num'
            num = float(input("Digite o número: "))
            resultado = funcao(num)

        print("Resultado:", resultado)

    except ValueError:
        print("Erro: entrada inválida. Digite apenas números.")

    input("Pressione ENTER para continuar...")
