def validar_e_sacar(valor, saldo, limite, numero_saques, extrato):
    if valor < 0:
        print("Valor inválido. Tente novamente ou digite 0 para sair para o menu")
    elif valor > 0:
        if valor > saldo:
            print(f'Não foi possível realizar a operação por saldo insuficiente em conta. \n Seu saldo atual é R${saldo:.2f}')
            print('Tente novamente ou digite 0 para retornar ao menu.')
        elif valor <= limite and valor <= saldo:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com Sucesso! \n Novo saldo: R${saldo:.2f}")
            extrato = f"Saque: \n   R${valor:.2f} \n {extrato}"
            numero_saques += 1
            return True, saldo, extrato, numero_saques
        else:
            print(f'Não é possível sacar o valor informado pois ele está acima do limite de R${limite:.2f} por transação.')
            print('Por favor, tente novamente ou digite 0 para retornar ao menu.')
    return False, saldo, extrato, numero_saques

def saque(*,saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
        while True:
            valor = float(input("Digite um valor a ser sacado: "))
            if valor == 0:
                break;
            sucesso, saldo, extrato, numero_saques = validar_e_sacar(valor, saldo, limite, numero_saques, extrato)
            if(sucesso):
                break         
    else:
        print(f'Você já realizou {numero_saques} de {LIMITE_SAQUES} hoje. \n Volte novamente amanhã.')
    return saldo, extrato, numero_saques

def coleta_endereco():
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Sigla Estado: ")
    endereco = f"{logradouro}, {numero}-{bairro}-{cidade}/{estado}"
    return endereco

def valida_cpf_existente(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False    

def coleta_informacoes_usuario(usuarios):
    cpf = input("CPF (Apenas números): ")
    if valida_cpf_existente(cpf, usuarios):
        print(f"CPF já utilizado.")
        return False, False
    else:    
        nome = input("Digite seu nome: ")
        endereco = coleta_endereco()
        nascimento = input("Digite sua data de nascimento: ")
        usuario = {"nome":nome, "endereco":endereco, "cpf":cpf, "nascimento":nascimento}
        return True, usuario

def adicionar_usuario(usuarios):
    adicionar, usuario = coleta_informacoes_usuario(usuarios)
    if adicionar:
        usuarios.append(usuario)
 
def deposito(saldo, extrato,/):
    ## Depositar os valores positivos
    while True:
        valor = float(input("Digite um valor a ser depositado: "))
        if valor < 0:
            print("Valor inválido. Tente novamente ou digite 0 para sair para o menu")
        elif valor > 0:
            saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com Sucesso! \n Novo saldo: R${saldo:.2f}")
            extrato = f"Depósito: \n   R${valor:.2f} \n {extrato}"
            break
        else:
            break
    return saldo, extrato

def extrato_conta(saldo,/,*,extrato):
    print(f"""
EXTRATO BANCÁRIO
------------------
              
{extrato}
------------------
Saldo atual: R${saldo:.2f}
              """)
 
def coleta_informacoes_conta(contas, usuarios):
    agencia = "0001"
    cpf = input("Digite seu CPF (Apenas números): ")
    if valida_cpf_existente(cpf,usuarios):
        ## criar conta
        conta_corrente = len(contas) + 1
        dados_conta = {"agencia":agencia, "conta":conta_corrente, "usuario":cpf}
        print(f"Conta {conta_corrente} criada com sucesso!")
        return True, dados_conta
    else:
        print(f"CPF {cpf} não existente na base de usuários.")
        return False, False

def adicionar_conta(contas, usuarios):
    adicionar, conta = coleta_informacoes_conta(contas, usuarios)
    if adicionar:
        contas.append(conta)

def menu_inicio():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [a] Adicionar Usuário
    [c] Adicionar conta
    [q] Sair

    """
    while True:
        opcao = input(menu)
        if opcao == 'd':
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == 's':
            saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == 'e':
            extrato_conta(saldo, extrato=extrato)
        elif opcao == 'a':
            adicionar_usuario(usuarios)
        elif opcao == 'c':
            adicionar_conta(contas, usuarios)
        elif opcao == 'q':
            print(contas)
            print(usuarios)
            break
        else:
            print("Opção inválida. Por favor, selecione novamente")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

menu_inicio()