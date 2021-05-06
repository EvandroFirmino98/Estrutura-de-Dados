from biblioteca.interface import *
from time import sleep

cabecalho('ESTACIONAMENTO UNIESP ')

#funcao para logar no sistemas
def dados():
    while True:
        try:
            log = (str(input('\033[32mLogin: \033[m')))
            senha = (int(input("\033[32mSenha: \033[m")))

            if log == str("jonas") or log == str("evandro"):
                if senha == int(123):
                    print("PESQUISANDO.....")
                    sleep(2)
                    print("SEJA BEM VINDO!!!")
                    break
        except:
            print('\033[31mERRO! Esperando Uma Senha Numerica:\033[m')

            # if senha != 123:
            # print("\033[31mSenha Invalida \033[m")
            # se deixar essa linha vai da erro quando colocar um numero no login e uma string na senha
            # sem essa linha funciona corretamente
        else:
            print('\033[31m[ERRO] Dados Inválidos!\033[m')
dados()
while True:
    resposta = menu(['Funcionário Do Estacionamento','Funcionário Do RH','Gestor Do Estacionamento','Sair Do Sistema'])
                        #menus de escolha paraas atividades
    #Estacionamento
    if resposta == 1:
        cabecalho('Funcionário Do Estacionamento')
        while True:
            menu_esta = menu(['Cadastrar novo veiculo',
                              'Remover veiculo',
                              'Monitora o estacionamento',
                              'Cadastrar ocorrência no estacionamento',
                              'Cadastrar novo evento no esacionamento',
                              'Sair do Sistema'])

            if menu_esta == 1:
                #cadastrar veiculo
                cadastrar = {
                    'veiculo1': {
                        'Proprietario': str(input("Proprietario: ")),
                        'Matricula': int(input("Matricula: ")),
                        'Modelo do Carro': str(input("Modelo do veiculo: ")),
                        'Ano do veiculo': int(input("Ano do veiculo: ")),
                        'Cor do veiculo': str(input("Cor do veiculo: ")),
                        'Placa': str(input("Placa do veiculo: "))},

                    }
                for veiculo_k, veiculo_v in cadastrar.items():
                    print(f'{veiculo_k}')
                    for dados_k, dados_v in veiculo_v.items():
                        print(f'\t{dados_k} = {dados_v}')

            elif menu_esta == 2:
                # Remover veiculo cadastrado
                menu_opcao = menu(['Remover',
                                    'Sair'])
                if menu_opcao == 1:
                    for veiculo_k, veiculo_v in cadastrar.items():
                        print(f' {veiculo_k}')
                        for dados_k, dados_v in veiculo_v.items():
                            print(f'\t{dados_k} = {dados_v}')
                    del cadastrar[input('Remover: ')]
                elif menu_opcao == 2:
                    cabecalho('Saindo')
                    break
                else:
                    print('\033[31m[ERRO] Opção inválida!\033[m')
                    continue

            elif menu_esta == 3:
                #monitorar o estacionamento
                try:
                    for veiculo_k, veiculo_v in cadastrar.items():
                        print(f' {veiculo_k}')
                        for dados_k, dados_v in veiculo_v.items():
                            print(f'\t{dados_k} = {dados_v}')
                except:
                    print("Nenhum veículo cadastrado!")
            elif menu_esta == 4:
                #cadastrar uma ocorrencia
                ocorrencia = {
                    'ocorrencia': {
                        'Enxiste': input("Enxiste alguma ocorrência: "),
                        'Proprietario': input("Proprietario: "),
                        'Local': input("Lcal da ocorrência: "),
                        'Placa': input("Placa do veiculo: ")}
                    }
                for ocorrencia_k, ocorrencia_v in ocorrencia.items():
                    print(f' {ocorrencia_k}')
                    for dados_k, dados_v in ocorrencia_v.items():
                        print(f'\t{dados_k} = {dados_v}')
            elif menu_esta == 5:
                #cadastrar eventos
                eventoGestor = {
                    'Evenstos': {
                    'Existe': input("Existe algum evento: "),
                    'Local': input("Local da evento: ")
                    }
                }
                for evento_k, evento_v in eventoGestor.items():
                    print(f' {evento_k}')
                    for dados_k, dados_v in evento_v.items():
                        print(f'\t{dados_k} = {dados_v}')
            elif menu_esta == 6:
                #sair do Funcionario do Estacionamento
                cabecalho('Saindo do sistema... Até logo!')
                break
            else:
                print('\033[31m[ERRO] Opção inválida!\033[m')
                continue
    #RH
    elif resposta == 2:
        cabecalho('Funcionário do RH')
        while True:
            menu_rh = menu(['Cadastrar novo Funcionario',
                            'Permissão de Acesso',
                            'Sair do Sistema'])

            if menu_rh == 1:
                #cadastrar Funcionario
                Funcionario = {
                    'Funcionario': {
                        'Nome': input("Digite Seu Nome: "),
                        'Sobrenome': input("Digite Seu Sobrenome: ") ,
                        'CPF': input("Digite Seu CPF: "),
                        'Data': input('Digite Sua Data De Anivesário: '),
                        'Endereço': input('Digite Seu Endereço: ')
                    }
                }
                for Funcionario_k, Funcionario_v in Funcionario.items():
                    print(f' {Funcionario_k}')
                    for dados_k, dados_v in Funcionario_v.items():
                        print(f'\t{dados_k} = {dados_v}')
            elif menu_rh == 2:
                #cadastrar permisão
                Permissao = {
                    'Permisão': {
                        'Existe': input("Existe Alguma Permissão: "),
                        'Nome': input("Digite Seu Nome: "),
                        'Funcionario': input("Digite o Funcionario: "),
                    }
                }
                for Permissao_k, Permissao_v in Permissao.items():
                    print(f' {Permissao_k}')
                    for dados_k, dados_v in Permissao_v.items():
                        print(f'\t{dados_k} = {dados_v}')
            elif menu_rh == 3:
                #sair do RH
                cabecalho('Saindo Do sistema... Até Logo!')
                break
            else:
                print('\033[31m[ERRO] Opção inválida!\033[m')
                continue
    #Gestor
    elif resposta == 3:
        cabecalho('Gestor Do Estacionamento')
        while True:
            menu_gesto = menu(['Monitorar o Estacionamento',
                               'Visualizar Relatórios',
                               'Criar área Especiais',
                               'Cadastrar Eventos No Estacionamento',
                               'Sair Do Sistema'])

            if menu_gesto == 1:
                #monitora o estacionamento
                try:
                    for veiculo_k, veiculo_v in cadastrar.items():
                        print(f' {veiculo_k}')
                        for dados_k, dados_v in veiculo_v.items():
                            print(f'\t{dados_k} = {dados_v}')
                except:
                    print("Nenhum veículo cadastrado!")
            elif menu_gesto == 2:
                #Relatorios
                menu_relatorio = menu([
                    'Relatórios de veiculos',
                    'Relatórios de Ocorrência',
                    'Relatórios de Eventos',
                    'Relatórios de Funcionario',
                    'Relatórios de Permisão',
                    'Relatórios da Área Especiais',
                    'Sair do Sistema'])

                if menu_relatorio == 1:
                    try:
                        for veiculo_k, veiculo_v in cadastrar.items():
                            print(f' {veiculo_k}')
                            for dados_k, dados_v in veiculo_v.items():
                                print(f'\t{dados_k} = {dados_v}')
                    except:
                        print("Nenhum veículo cadastrado!")
                elif menu_relatorio == 2:
                    try:
                        for ocorrencia_k, ocorrencia_v in ocorrencia.items():
                            print(f' {ocorrencia_k}')
                            for dados_k, dados_v in ocorrencia_v.items():
                                print(f'\t{dados_k} = {dados_v}')
                    except:
                        print("Nenhum Ocorrência cadastrado!")
                elif menu_relatorio == 3:
                    try:
                        for evento_k, evento_v in eventoGestor.items():
                            print(f' {evento_k}')
                            for dados_k, dados_v in evento_v.items():
                                print(f'\t{dados_k} = {dados_v}')
                    except:
                        print("Nenhum Evento cadastrado!")
                elif menu_relatorio == 4:
                    try:
                        for Funcionario_k, Funcionario_v in Funcionario.items():
                            print(f' {Funcionario_k}')
                            for dados_k, dados_v in Funcionario_v.items():
                                print(f'\t{dados_k} = {dados_v}')
                    except:
                        print("Nenhum Funcionario cadastrado!")

                elif menu_relatorio == 5:
                    try:
                        for Permissao_k, Permissao_v in Permissao.items():
                            print(f' {Permissao_k}')
                            for dados_k, dados_v in Permissao_v.items():
                                print(f'\t{dados_k} = {dados_v}')
                    except:
                        print("Nenhuma Permisão cadastrada!")
                elif menu_relatorio == 6:
                    try:
                        for area_k, area_v in areas.items():
                            print(f' {area_k}')
                            for dados_k, dados_v in area_v.items():
                                print(f'\t{dados_k} = {dados_v}')
                    except:
                        print("Nenhuma Área Especial cadastrada!")
                elif menu_relatorio == 7:
                    print("Saindo..")
                    sleep(1)
                    continue
                else:
                    print('\033[31m[ERRO] Opção inválida!\033[m')

            elif menu_gesto == 3:
                #cadastrar permisão
                areas = {
                    'Permissao': {
                        'Existe': input("Existe Alguma Permissão: "),
                        'Nome': input("Digite Seu Nome: "),
                        'Funcionario': input("Digite o Funcionario: "),
                    }
                }
                for area_k, area_v in areas.items():
                    print(f' {area_k}')
                    for dados_k, dados_v in area_v.items():
                        print(f'\t{dados_k} = {dados_v}')
            elif menu_gesto == 4:
                #cadastrar Eventos
                eventoGestor = {
                    'Eventos': {
                        'Existe': input("Existe Algum Evento: "),
                        'Local': input("Local Do Evento: ")
                    }
                }
                for eventoGestor_k, eventoGestor_v in eventoGestor.items():
                    print(f' {eventoGestor_k}')
                    for dados_k, dados_v in eventoGestor_v.items():
                        print(f'\t{dados_k} = {dados_v}')
            elif menu_gesto == 5:
                #sair do Gestor
                cabecalho('Saindo Do Sistema... Até Logo!')
                break
            else:
                print('\033[31m[ERRO] Opção inválida!\033[m')
                continue

    #sair do programa
    elif resposta == 4:
        cabecalho('Saindo Do Sistema... Até Logo!')
        break
    else:
        print('\033[31m[ERRO] Opção inválida!\033[m')
    sleep(1)