menu = """

[1] Depositar
[2] Sacar
[3] Extrato

[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo += valor_deposito
        extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
        print("Valor depositado com sucesso!\n\nO que deseja fazer a seguir?")
    
    elif opcao == "2":
        if numero_saques < 3:
            print(f"Limite diário permitido pela política do banco: {LIMITE_SAQUES} saques de R$ {limite:.2f} cada")
            print(f"Quantidade de saques restantes permitidos no dia: {LIMITE_SAQUES - numero_saques}\n")
            valor_sacado = float(input("Digite o valor que deseja sacar: "))

            if valor_sacado > 500:
                print(f"O valor solicitado ultrapassa o limite diário permitido de R$ {limite:.2f}\nTente novamente.")

            elif valor_sacado > 0 and valor_sacado <= 500:
                saldo -= valor_sacado
                extrato += f"Saque de R$ {valor_sacado:.2f}\n"
                numero_saques += 1
                print("Valor sacado com sucesso!\n")

            else:
                print("Valor inválido!\nTente novamente.")

            print("\nO que deseja fazer a seguir?")
        else:
            print(f"LIMITE DIÁRIO DE SAQUE ATINGIDO!\nREALIZE ESTA OPERAÇÃO NOVAMENTE AMANHÃ!\n\nO que deseja fazer a seguir?")
    
    elif opcao == "3":
        print("Histórico de Movimentações")
        print(extrato)
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
    
    