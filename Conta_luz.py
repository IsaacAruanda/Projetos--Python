def calcular_variacao_percentual(valor_antigo, valor_novo):
    try:
        variacao = valor_novo - valor_antigo
        percentual = (variacao / valor_antigo) * 100

        if percentual > 0:
            return f"\nHouve um aumento de {percentual:.2f}% na conta de luz."
        elif percentual < 0:
            return f"\nHouve uma redução de {abs(percentual):.2f}% na conta de luz."
        else:
            return "\nNão houve alteração no valor da conta de luz."
    except ZeroDivisionError:
        return "\nErro: o valor antigo não pode ser zero."

# Função que converte vírgula para ponto e trata saída
def entrada_float(msg):
    while True:
        entrada = input(msg).strip().lower()
        if entrada in ["sair", "q"]:
            return "sair"
        try:
            valor = float(entrada.replace(',', '.'))
            return valor
        except ValueError:
            print("Valor inválido. Use números (ex: 123.45 ou 123,45) ou 'sair' para encerrar.")

# Loop principal
while True:
    print("\n=== CALCULADORA DE VARIAÇÃO DA CONTA DE LUZ ===")
    
    valor_antigo = entrada_float("Informe o valor antigo da conta de luz (ou 'sair' para encerrar): ")
    if valor_antigo == "sair":
        break

    valor_novo = entrada_float("Informe o valor novo da conta de luz (ou 'sair' para encerrar): ")
    if valor_novo == "sair":
        break

    mensagem = calcular_variacao_percentual(valor_antigo, valor_novo)
    print(mensagem)

    input("\nPressione Enter para continuar...")
