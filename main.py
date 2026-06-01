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

def menu_cadastro():
    
    print("""Opções de cadastro: 
               
   1 - Cadastrar Ativo
   2 - Cadastrar Vulnerabilidade             
     """)
    
    escolha = int(input('Escolha uma opção para continuar: '))

    match escolha:

        case 1: 
            cadastrar_ativo()

        case 2:
            cadastrar_vuln()


def cadastrar_ativo():

    global id_ativo
    
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
    "nome_hostname" : nome_host,
    "responsavel" : responsavel,
    "setor" : setor,
    "tipo" : tipo_ativo.name,
    "vulnerabilidades" : []

        }

    ativos.append(ativo)
    print('Ativo cadastrado com sucesso!!')
    id_ativo += 1 
        
    sleep(3)
    return


def cadastrar_vuln():
        
        ativo = conferir_ativo()

        if ativo:
            
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

            ativo["vulnerabilidades"].append(vulnerabilidades)


def buscar_ativo(ativo_buscado):

    if ativo_buscado.isdigit():
        ativo_buscado = int(ativo_buscado)

    for ativo in ativos:
        if ativo_buscado == ativo["ID"] or ativo_buscado == ativo["nome_hostname"]:

            return ativo
        
    return None


def conferir_ativo():

    if len(ativos) == 0 :
        print('Não existem Ativos cadastrados!!')
        return None
    
    elif len(ativos) > 0:
        
        ativo_buscado = input('Digite o nome/hostname ou ID do ativo buscado: ')
        ativo = buscar_ativo(ativo_buscado)

        if ativo:
            return ativo

    return None
                    

def listar_ativo(ativo):

    print(f""" 
-------------------------
          
ID: {ativo["ID"]}
Nome/Hostname: {ativo["nome_hostname"]}
Responsável: {ativo["responsavel"]}
Setor: {ativo["setor"]}
Tipo: {ativo["tipo"]}     

---- Vulnerabilidades --- """)
    
    if len(ativo["vulnerabilidades"]) == 0:

        print('\nNão existem Vulnerabilidades cadastradas!!')

    elif len(ativo["vulnerabilidades"]) > 0:

        for vuln in ativo["vulnerabilidades"]:
            
            print(f"""                             
Descrição: {vuln["descricao"]}
Tipo: {vuln["tipo"]}
Severidade: {vuln["severidade"]}
Status: {vuln["status"]}   """)


# def atualizar_ativo():

# def excluir_ativo():


while True:

    print("""
---- Bem Vindo ao Sistema de Cadastro ----
   
   1 - Cadastrar Ativo/Vulnerabilidade
   2 - Buscar
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

            menu_cadastro()

        case 2:

           certo = conferir_ativo()

           if certo :
               
               listar_ativo(certo)
               