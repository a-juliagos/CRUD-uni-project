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

def limpar_tela():

    os.system('cls')

def pausar():
    input("\nPressione ENTER para continuar...")


def cadastrar_ativo():

    global id_ativo
    
    print('Escreva as informações do ativo a ser cadastrado\n')

    while True:

        nome_host = input('Nome ou hostname: ').strip()

        if any(nome_host.lower() == ativo["nome_hostname"].lower() for ativo in ativos):
            print('Este nome já está em uso!\n')
        
        else:
            break

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
        
    pausar()


def cadastrar_vuln():
        
    ativo = buscar_ativo()

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

        print("Vulnerabilidade cadastrada com sucesso!")

    pausar()
    

def buscar_ativo():

    if not ativos:
        print('Não existem Ativos cadastrados!!')
        pausar()
        return None

    ativo_buscado = input(
        'Digite o nome/hostname ou ID do ativo buscado: '
    )

    if ativo_buscado.isdigit():
        ativo_buscado = int(ativo_buscado)

    for ativo in ativos:
        
        if (
        isinstance(ativo_buscado, str)
        and ativo_buscado.lower() == ativo["nome_hostname"].lower() ): 
            return ativo

        if ativo_buscado == ativo["ID"]:
            return ativo
    
    print('O ativo não existe ou foi excluído.')
    pausar()
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
    
    if not ativo["vulnerabilidades"]:

        print('\nNão existem Vulnerabilidades cadastradas!!')

    else:

        for i, vuln in enumerate(ativo["vulnerabilidades"], start=1):
            
            print(f"""   
Vulnerabilidade {i}

Descrição: {vuln["descricao"]}
Tipo: {vuln["tipo"]}
Severidade: {vuln["severidade"]}
Status: {vuln["status"]} """)
            

def listar_all_ativos():

    if not ativos:
        print("Não existem ativos cadastrados.")
        pausar()
        return

    for ativo in ativos:
        listar_ativo(ativo)

    pausar()


def atualizar_ativo():

    ativo = buscar_ativo()

    if not ativo:
        
        print('O ativo não existe ou foi excluído.')
        pausar()
        return
    
    while True:
            
        novo_nome_host = input('Digite o novo nome: ')
            
        if any( novo_nome_host == a["nome_hostname"] for a in ativos if a["ID"] != ativo["ID"] ):
            print('Este nome já está em uso!')

        else:
            break

    novo_responsavel = input('Digite o novo responsável: ')
    novo_setor = input('Digite o novo setor: ')

    ativo["nome_hostname"] = novo_nome_host
    ativo["responsavel"] = novo_responsavel
    ativo["setor"] = novo_setor

    print('Ativo atualizado com sucesso!!')

    pausar()
   

def excluir_ativo():

    ativo = buscar_ativo()
    
    if ativo:

        nome = ativo["nome_hostname"]

        ativos.remove(ativo)
        print(f'O ativo {nome} foi excluído com sucesso!!')

    else:
        print('O ativo não existe ou foi excluído.')

    pausar()
   

while True:

    limpar_tela()

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
            sleep(2)
            break
        
        case 1:

            limpar_tela()
            
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
                
                case _:
                    print("Escolha um valor válido.")

        case 2:

            limpar_tela()
            
            print("""Opções de busca: 
               
   1 - Buscar 
   2 - Listar todos            
     """)
    
            escolha = int(input('Escolha uma opção para continuar: '))

            match escolha:
                
                case 1: 
                    ativo_certo = buscar_ativo()
                    
                    if ativo_certo :
                        limpar_tela()
                        listar_ativo(ativo_certo)
                        pausar()
                                     
                case 2:
                    limpar_tela()
                    listar_all_ativos()

                case _:
                    print("Escolha um valor válido.")
     
        case 3:

            atualizar_ativo()

        case 4:

            excluir_ativo()
        
        case _:
            print("Escolha um valor válido.")
            pausar()
