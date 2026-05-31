from enum import IntEnum
from time import sleep
import os

class tipoAtivo(IntEnum): 

    NOTEBOOK = 1
    SERVIDOR = 2
    BANCO_DE_DADOS = 3
    SOFTWARE_lICENCIADO = 4 
    IMPRESSORA_DE_REDE = 5

class severidadeTipo(IntEnum):

    BAIXA = 1
    MÉDIA = 2
    ALTA  = 3
    CRITICA = 4 

class tratamentoStatus(IntEnum):

    AGUARDANDO = 1
    EM_PROCESSO = 2
    CORRIGIDA = 3
    RISCO_ACEITO = 4

ativos = []
id_ativo = 1

def cadastrar_ativo():

    global id_ativo

    print('Digite as Informações do ativo a ser cadastrado\n')
    nome_host = input('Nome ou hostname: ')
    responsavel = input('Responsavel: ')
    setor = input('Setor/localização: ')


    print('\n---- Tipos de Ativos ----')

    for tipo in tipoAtivo:
        print(f'{tipo.value} - {tipo.name}')

    tipo_ativo = tipoAtivo(int(input('Tipo: ')))

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

def cadastrar_vulne():

    global ativo

    print("""Buscar ativo por:
          
        1 - ID
        2 - Nome/Hostname  

          """)
    
    opcao = int(input())

    if opcao == 1:

        procurado = int('Digite o ID do ativo desejado: ')

        if procurado == ativo["ID"]:
            
            descricao = input('Dscrição: ')
            tipo = input('Tipo: ')

            print('---- Severidade ----')

            for sev in severidadeTipo:
                print(f'{sev.value} - {sev.name}')
    
            sev_tipo = severidadeTipo(int(input('Severidade: ')))

            print('---- Status de Tratamento ----')

            for status in tratamentoStatus:
                print(f'{status.value} - {status.name}')
    
            status_tipo = tratamentoStatus(int(input('Status de Tratamento: ')))


        vulnerabilidades = {

        "descricao" : descricao,
        "tipo" : tipo,
        "severidade" : sev_tipo.name,
        "status" : status_tipo.name

        }

        ativos["vulnerabildades"].append(vulnerabilidades)

    
    elif opcao == 2:

         procurado = int('Digite o Nome ou Hostname do ativo desejado: ')

         if procurado == ativo["Nome/Hostname"]:
        

# def buscar_lis_ativo():


# def atualizar_ativo():

# def excluir ativo():


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

    if escolha == 0:

        print('Encerrando sistema...')
        sleep(3)
        break

    elif escolha == 1:

        cadastrar_ativo()

    
    