from enum import IntEnum
from time import sleep
import os

class TipoAtivo(IntEnum): 

    NOTEBOOK = 1
    SERVIDOR = 2
    BANCO_DE_DADOS = 3
    SOFTWARE_LICENCIADO = 4 
    IMPRESSORA_DE_REDE = 5

class SeveridadeTipo(IntEnum):

    BAIXA = 1
    MEDIA = 2
    ALTA  = 3
    CRITICA = 4 

class TratamentoStatus(IntEnum):

    AGUARDANDO = 1
    EM_PROCESSO = 2
    CORRIGIDA = 3
    RISCO_ACEITO = 4

ativos = []
id_ativo = 1

def cadastrar_ativo():

    global id_ativo
    
    print("""Opções de cadastro: 
               
   1 - Cadastrar Ativo
   2 - Cadastrar Vulnerabilidade
               
     """)
    
    escolha = int(input('Escolha uma opção para continuar: '))

    match escolha:

        case 1:
 
            print('Escreva as informações do ativo a ser cadastrado\n')
            nome_host = input('Nome ou hostname: ')
            responsavel = input('Responsavel: ')
            setor = input('Setor/localização: ')


            print('\n---- Tipos de Ativos ----\n')

            for tipo in TipoAtivo:
                print(f'   {tipo.value} - {tipo.name}')

            tipo_ativo = TipoAtivo(int(input('Tipo: ')))

            ativo = {

    "ID" : id_ativo,
    "nome/hostname" : nome_host,
    "responsavel" : responsavel,
    "setor" : setor,
    "tipo" : tipo_ativo.name,
    "vulnerabilidade" : []

        }

            ativos.append(ativo)
            print('Ativo cadastrado com sucesso!!')
            id_ativo += 1 
        
            sleep(3)
            return
        
        case 2: 
            cadastrar_vuln()

def cadastrar_vuln():

    global ativos

    print("""Buscar ativo por:
          
   1 - ID
   2 - Nome/Hostname  

          """)
    
    opcao = int(input('Escolha uma opção para continuar: '))

    match opcao:

        case 1:

            id_procurado = int(input('Digite o ID do ativo desejado: '))

            for ativo in ativos:

                if id_procurado == ativo["ID"]:
                
                    descricao = input('Descrição: ')
                    tipo = input('Tipo: ')

                    print('\n---- Severidade ----\n')

                    for sev in SeveridadeTipo:
                        print(f'   {sev.value} - {sev.name}')
    
                    sev_tipo = SeveridadeTipo(int(input('Severidade: ')))

                    print('\n---- Status de Tratamento ----\n')

                    for status in TratamentoStatus:
                        print(f'   {status.value} - {status.name}')
    
                    status_tipo = TratamentoStatus(int(input('Status de Tratamento: ')))


                    vulnerabilidades = {

        "descricao" : descricao,
        "tipo" : tipo,
        "severidade" : sev_tipo.name,
        "status" : status_tipo.name

        }

                    ativo["vulnerabilidade"].append(vulnerabilidades)
        
    
    # elif opcao == 2:

    #      procurado = int('Digite o Nome ou Hostname do ativo desejado: ')

    #      if procurado == ativo["Nome/Hostname"]:
        

# def buscar_lis_ativo():


# def atualizar_ativo():


# def excluir_ativo():


while True:

    print("""

---- Bem Vindo ao Sistema de Cadastro ----
   
   1 - Cadastrar Ativo/Vulnerabilidade
   2 - Buscar/Listar
   3 - Atualizar
   4 - Remover
   0 - Sair 

""")
    escolha = int(input('Escolha uma opção para continuar: '))

    match escolha:

        case 0:

            print('Encerrando sistema...')
            sleep(3)
            break
        
        case 1:
            cadastrar_ativo()