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

while True:
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    escolha = input("Digite o número da operação: ")

    if escolha == "0":
        print("Saindo do programa.")
        break

    if escolha not in ["1", "2", "3", "4"]:
        print("Operação inválida! Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite números.")
        continue

    if escolha == "1":
        resultado = adicao(num1, num2)
    elif escolha == "2":
        resultado = subtracao(num1, num2)
    elif escolha == "3":
        resultado = multiplicacao(num1, num2)
    elif escolha == "4":
        resultado = divisao(num1, num2)

    print(f"Resultado: {resultado}\n")
