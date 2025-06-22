# Versão 2

# Objetivo Geral
# - Separar as funções existentes de saque, depósito e extrato em funções.
# - Criar duas novas funções:
#     - Cadastrar usuário (cliente)
#     - Cadastrar conta bancária (vincular com usuário)

# Separação em funções

# Função Saque
#     - Deve receber os argumentos apenas por nome (keyword only)
#     - Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
#     - Sugestão de retorno: saldo e extrato

# Depósito
#     - Deve receber os argumentos apenas por posição (positional only)
#     - Sugestão de argumentos: saldo, valor, extrato
#     - Sugestão de retorno: saldo e extrato

# Extrato
#     - Deve receber os argumentos por posição e nome (positional only e keyword only)
#     - Argumentos posicionais: saldo
#     - Argumentos nomeados: extrato

# Criar usuário (cliente)
#     - Deve armazenar os usuários em uma lista
#     - Um usuário é composto de:
#         - nome
#         - data de nascimento
#         - cpf: 
#             - deve ser cadastrado apenas numeros do cpf
#             - Não podemos cadastrar dois usuários com o mesmo cpf
#         - endereço: é uma string com formato logradouro, nro - bairro - cidade/estado

# Criar conta corrente
#     - Deve armazenar contas em uma lista
#     - Uma conta é composto de:
#         - agência
#             - É um número fixo "0001"
#         - número da conta
#             - Deve ser sequencial, iniciando em 1
#         - usuário
#             - Um usuário pode ter mais de uma conta, mas uma conta não pode ter mais do que um usuário

# Dica
#     Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
###########################################################################################################################################

def depositar(saldo, valor_deposito, extrato, /):
    saldo += valor_deposito
    extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Histórico de Movimentações")
    print(extrato)
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def sacar(*, saldo, valor_sacado, extrato, numero_saques):
    saldo -= valor_sacado
    extrato += f"Saque de R$ {valor_sacado:.2f}\n"
    numero_saques += 1
    return saldo, valor_sacado, extrato, numero_saques

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    # Verifica se o usuário já foi cadastrado.
    if cpf_existe(usuarios, cpf):
        print("Já existe um usuário cadastrado com esse CPF!\n\nTente novamente!")
        return
    # O sistema só avança se for um novo usuário.
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento no formato dd/mm/aaaa: ")
    endereco = input("Digite o endereço no formato logradouro, nro - bairro - cidade/estado: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário cadastrado com sucesso!\n\n")

# Função que verifica se o CPF digitado já foi cadastrado
def cpf_existe(usuarios, cpf):
    return any(usuario["cpf"] == cpf for usuario in usuarios)

# Função pra listar os dados dos usuários cadastrados
def lista_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario["nome"]}")
        print(f"Data de Nascimento: {usuario["data_nascimento"]}")
        print(f"CPF: {usuario["cpf"]}")
        print(f"Endereço: {usuario["endereco"]}\n")

def criar_conta(usuarios, agencia, contas, numero_conta):
    cpf = input("Digite o CPF do usuário que deseja abrir uma conta: ")
    # Verifica se o usuário já foi cadastrado.
    if cpf_existe(usuarios, cpf):
        usuario_localizado = localizar_usuario(usuarios, cpf)
        print("\nUsuário localizado com sucesso!")
        print (f"Nome: {usuario_localizado["nome"]}\n\n")
        nome_usuario = usuario_localizado["nome"]
        opcao = input("Deseja prosseguir com a abertura de conta? [y/n]: ")
        if opcao == "n": 
            return
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "nome_usuario": nome_usuario})
        print("\nConta criada com sucesso!\n\n")
        print(f"Usuário: {nome_usuario}")
        print(f"Agência: {agencia}")
        print(f"Número da Conta: {numero_conta}\n\n")

    else:
        print("Não existe usuário cadastrado com o número de CPF informado.\nRelize primeiramente o cadastro do usuário.\n\n")

# Retorna o usuário com base no CPF
def localizar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario 

# Função para listar as contas existentes
def lista_contas(contas):
    for conta in contas:
        print(f"\nTitular: {conta["nome_usuario"]}")
        print(f"Agência: {conta["agencia"]}")
        print(f"Número da Conta: {conta["numero_conta"]}\n\n")

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Novo Usuário
[5] Listar Usuários Cadastrados
[6] Criar Conta Corrente
[7] Listar Contas

[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
AGENCIA = "0001"
contas = []
numero_conta = 1

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito <= 0:
            print("\nValor inválido!\nDigite um valor maior que 0 (zero)\nTente novamente.")

        else:
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
            print(f"\nValor depositado com sucesso!\nSaldo atual: R$ {saldo:.2f}\nO que deseja fazer a seguir?")
    
    elif opcao == "2":
        if numero_saques < 3:
            print(f"Limite diário permitido pela política do banco: {LIMITE_SAQUES} saques de R$ {limite:.2f} cada")
            print(f"Quantidade de saques restantes permitidos no dia: {LIMITE_SAQUES - numero_saques}\n")
            valor_sacado = float(input("Digite o valor que deseja sacar: "))

            if saldo < valor_sacado:
                print ("\nVocê não possui saldo suficiente!\nConsulte seu extrato para maiores informações.\nTente novamente.")
            
            elif valor_sacado > 500:
                print(f"\nO valor solicitado ultrapassa o limite diário permitido de R$ {limite:.2f}\nTente novamente.")

            elif valor_sacado > 0 and valor_sacado <= 500:
                saldo, valor_sacado, extrato, numero_saques = sacar(saldo=saldo, valor_sacado=valor_sacado, extrato=extrato, numero_saques=numero_saques)
                print(f"\nValor sacado com sucesso!\nSaldo atual: R$ {saldo:.2f}")

            else:
                print("\nValor inválido!\nTente novamente.")

            print("\nO que deseja fazer a seguir?")
        else:
            print(f"\nLIMITE DIÁRIO DE SAQUE ATINGIDO!\nREALIZE ESTA OPERAÇÃO NOVAMENTE AMANHÃ!\n\nO que deseja fazer a seguir?")
    
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)
    
    elif opcao == "4":
        criar_usuario(usuarios)
    
    elif opcao == "5":
        lista_usuarios(usuarios)

    elif opcao == "6":
        criar_conta(usuarios, AGENCIA, contas, numero_conta)
        numero_conta += 1
    
    elif opcao == "7":
        lista_contas(contas)

    elif opcao == "0":
        break
    
    else:
        print("Opção inválida!")