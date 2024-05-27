import os

escolha = 1
opcao = 0

nomes_lista = []

while escolha > 0:
    print ("\nLista de Opções: \n")
    print('1 - Inserir pessoa na Lista')
    print('2 - Listar pessoas cadastradas')
    print('3 - Pesquisar pelo nome de uma pessoa')
    print('4 - Ordenar a lista por ordem alfabética')
    print('5 - Atualizar nome')
    print('6 - Deletar nome da lista')
    print('7 - Sair do programa')

    opcao1 = int(input('\nEscolha a opção desejada (1 a 7):\n'))
    
    match opcao1:
        case 1:
            while True:
                novo_nome = input('Informe o novo nome a ser inserido na lista: ')
                if novo_nome !='':
                    nomes_lista.append(novo_nome)
                    print(f'{novo_nome} inserido com sucesso.')
                    continue
                else: 
                    os.system('cls')
                    for nome in nomes_lista:
                        print(nome)                
                    break
        case 2:
            for nome in nomes_lista:
                print(nome)
        case 3:
            nome = input('Informe o nome que deseja encontrar: ').capitalize()
            # busca o nome desejado
            try:
                indice = nomes_lista.index(nome)
                quantidade = nomes_lista.count(nome)
                print(f'Nome encontrado: {nome} {quantidade} vez(es) no índice {indice}')
            except:
                print(f'{nome} não encontrado na lista.')
        case 4:
            nomes_lista.sort()        
            # lista ordenada...
            print ('Lista ordenada:')
            for nome in nomes_lista:
                print(nome)
        case 5:
            indice2 = int(input('Informe o índice que deseja alterar: '))
            indice2 -= 1
            nomes_lista[indice2] = input('Informe o novo nome: ')
            for nome in nomes_lista:
                print(nome)        
        case 6:
            nome_a_excluir = input('Informe o nome que deseja retirar da lista: ')
            try:
                nomes_lista.remove(nome_a_excluir)
            except:
                print('Nome não pode ser excluído.')

            for nome in nomes_lista:
                print(nome)        
        case 7:
            escolha = 0
            break
        case _:
            print('Opção inváida! Digite uma opção de 1 a 7')
            continue      