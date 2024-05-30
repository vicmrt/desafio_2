menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
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

    elif opcao == 's':
        if numero_saques < 3:
            while True:
                valor = float(input("Digite um valor a ser sacado: "))
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
                        break
                    else:
                        print(f'Não é possível sacar o valor informado pois ele está acima do limite de R${limite:.2f} por transação.')
                        print('Por favor, tente novamente ou digite 0 para retornar ao menu.')
                else:
                    break    
        else:
            print(f'Você já realizou {numero_saques} de {LIMITE_SAQUES} hoje. \n Volte novamente amanhã.')        
    elif opcao == 'e':
        print(f"""
EXTRATO BANCÁRIO
------------------
              
{extrato}
------------------
Saldo atual: R${saldo:.2f}
              """)
    elif opcao == 'q':
        break
    
    else:
        print("Opção inválida. Por favor, selecione novamente")
