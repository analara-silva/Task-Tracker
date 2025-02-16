from functions import *
from time import sleep
tarefa = Arquivo_json()

while True:
    
    aprovação = False

    print('[1] Adicionar')
    print('[2] Atualizar')
    print('[3] Excluir')
    print('[4] Listar')
    print('[5] Sair do programa')

    option = Option([1, 2, 3, 4, 5])
     # Adicionar
    if option == 1:
        Adicionar(tarefa)

    # Atualizar    
    elif option == 2:
        aprovação = Verificar_Lista(tarefa)
        if aprovação:
            print('[1] Titulo')
            print('[2] Descrição')
            print('[3] Status')
            
            option = Option([1, 2, 3])
            atualizacao(tarefa, option)
        
        else:
            print('\n\033[1;31mNão há itens na lista.\033[m\n')
           
    # Excluir
    elif option == 3:
        aprovação = Verificar_Lista(tarefa)
        
        if aprovação:
            Listagem(tarefa)
            
            id = Option(list(range(1, len(tarefa) + 1)))
            
            Excluir(tarefa, id)
        
        else:
            print('\n\033[1;31mNão há itens para excluir.\033[m\n')
        
    
    # Listar
    if option == 4:
        
        aprovação = Verificar_Lista(tarefa)
        
        if aprovação:
            print('[1] Todos')
            print('[2] Afazer')
            print('[3] Em Andamento')
            print('[4] Concluido')
            print('[5] Voltar')
            
            option = Option([1, 2, 3, 4, 5])
            
            if option == 1:
                listagem(tarefa)  
            elif option == 2:
                listagem(tarefa, 'Afazer')
            elif option == 3:
                listagem(tarefa, 'Em Andamento')
            elif option == 4:
                listagem(tarefa, 'Concluido')
            elif option == 5:
                continue
        
        else:
            print('Não há itens na lista.')
            print('Adicione uma tarefa para poder listar.')
    
    if option == 5:
        Listar_id(tarefa)
        Lista_para_json(tarefa)
        print('\nSaindo...')
        break