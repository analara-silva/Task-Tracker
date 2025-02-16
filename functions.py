import json
import os

def Arquivo_json():
    if not os.path.isfile('arquivo.json'):
        arquivo = open('arquivo.json', 'w+', encoding='utf-8')
        arquivo.close()
        tarefa = list()
        
    else:
        with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
            try:
                tarefa = json.load(arquivo)
            
            except:
                tarefa = list()
            
    return tarefa
        
def Option(lista):
    while True:
        try:
            option = int(input('Sua opção: '))
            
        except:
            print('Opção Invalida!')
            
        else:
            if option in lista:
                return option
            else:
                print('Digite uma opção valida!')

def Verificar_Lista(lista):
    if len(lista) == 0:
        return False       
    else:
        return True
        
def Adicionar(lista):
    from datetime import datetime
    afazeres = dict()
    
    print()
    afazeres['id'] = len(lista) + 1
    afazeres['titulo'] = str(input('Título: ')).strip().upper()
    afazeres['descricao'] = str(input('Descrição: ')).strip()
    afazeres['status'] = 'Afazer'
    afazeres['criacao'] = (datetime.now().strftime("%d/%m/%Y - %H:%M"))
    afazeres['atualizacao'] = (datetime.now().strftime("%d/%m/%Y - %H:%M"))
    print()
    
    lista.append(afazeres.copy())

def Listagem(lista):
        print(f'{"ID":^5}| {"TITULO":^20}| {"STATUS":^13}|')
        print('-' * 43)
            
        for item in lista:
            print(f'{item["id"]:^5}| {item["titulo"]:^20}| {item["status"]:^13}|')
            print('-' * 43)

def Lista_para_json(lista):
    with open('arquivo.json', 'w+', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo)

def atualizacao(lista, option):
    from datetime import datetime
    
    Listagem(lista)
    tarefa = Option(list(range(1, len(lista) + 1)))
    
    
    if option == 3:
        print('[1] AFAZER')
        print('[2] EM ANDAMENTO')
        print('[3] CONCLUIDO')
        
        status = Option([1, 2, 3])
        
        if status == 1:
            item_lista = 'Afazer'
        elif status == 2:
            item_lista = 'Em Andamento'
        elif status == 3:
            item_lista = 'Concluido'
        
        for item in lista:
            if item['id'] == tarefa:
                item['status'] = item_lista    
                item['atualizacao'] = datetime.now().strftime("%d/%m/%Y - %H:%M")            

    else:
        if option == 1:
            for item in lista:
                if item['id'] == tarefa:
                    item['titulo'] = str(input('Atualize seu titulo: ')).strip().upper()
                    item['atualizacao'] = datetime.now().strftime("%d/%m/%Y - %H:%M")
        else:
            for item in lista:
                if item['id'] == tarefa:
                    item['descricao'] = str(input('Atualize sua descrição: '))
                    item['atualizacao'] = datetime.now().strftime("%d/%m/%Y - %H:%M")

def Listar_id(lista): 
    id = 0
    
    for item in lista:
        for x in range(1):
            id += 1
        if item['id'] != id:
            item['id'] = id
                        
def Excluir(lista, id):
    del lista[id - 1]
    
    Listar_id(lista)

def verificar_status(lista, status):
    
    verificação = 0
    
    for item in lista:
        if status in item.values():
            verificação += 1
            
    if verificação > 0:
        return True
    
    else:
        return False
            
def listagem(lista, option ='Todos'):
    print(f'{"ID":^5}| {"TITULO":^20}| {"STATUS":^13}|')
    print('-' * 43)
    for item in lista:
        if 'Todos' in option:
            print(f'{item["id"]:^5}| {item["titulo"]:^20}| {item["status"]:^13}|')
            print('-' * 43)
            
        else:
            aprovação = verificar_status(lista, option)
            
            if aprovação:
                if item['status'] == option:
                    print(f'{item["id"]:^5}| {item["titulo"]:^20}| {item["status"]:^13}|')
                    print('-' * 43)
            else:
                print('\n\033[1;31mNão há itens na sua lista\033[m\n')
                          