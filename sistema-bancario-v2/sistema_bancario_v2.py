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

        if valor_deposito <= 0:
            print("\nValor inválido!\nDigite um valor maior que 0 (zero)\nTente novamente.")

        else:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
            print(f"\nValor depositado com sucesso!\nSaldo atual: R$ {saldo:.2f}\nO que deseja fazer a seguir?")
    
    elif opcao == "2":
        if numero_saques < 3:
            print(f"Limite diário permitido pela política do banco: {LIMITE_SAQUES} saques de R$ {limite:.2f} cada")
            print(f"Quantidade de saques restantes permitidos no dia: {LIMITE_SAQUES - numero_saques}\n")
            valor_sacado = float(input("Digite o valor que deseja sacar: "))

            if saldo < valor_sacado:
                print ("\nVocê não possui saldo suficiente!\nConsulte seu extrato para maiores informações.\nTente novamente.")
            
            else:
                if valor_sacado > 500:
                    print(f"\nO valor solicitado ultrapassa o limite diário permitido de R$ {limite:.2f}\nTente novamente.")

                elif valor_sacado > 0 and valor_sacado <= 500:
                    saldo -= valor_sacado
                    extrato += f"Saque de R$ {valor_sacado:.2f}\n"
                    numero_saques += 1
                    print(f"\nValor sacado com sucesso!\nSaldo atual: R$ {saldo:.2f}")

                else:
                    print("\nValor inválido!\nTente novamente.")

                print("\nO que deseja fazer a seguir?")
        else:
            print(f"\nLIMITE DIÁRIO DE SAQUE ATINGIDO!\nREALIZE ESTA OPERAÇÃO NOVAMENTE AMANHÃ!\n\nO que deseja fazer a seguir?")
    
    elif opcao == "3":
        print("Histórico de Movimentações")
        print(extrato)
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
    
    