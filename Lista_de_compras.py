import os

lista = []
deletar = True
sair = True
while sair:
    def mostrar():
        os.system('cls')
        for i in range(len(lista)):
            print(i, lista[i])

    mostrar()
    print('selecione uma opção')
    opcao = input(' [I]nserir, [A]pagar ou [S]air: ')
    opcao = opcao[0].upper()
    if opcao == 'I':
        mostrar()
        adicao = input('Digite o nome do produto a ser comprado: ')
        lista.append(adicao)

    elif opcao == 'A':
        mostrar()
        if len(lista) < 1:
            print('Não há itens na lista para serem apagados')
        else:
            while deletar:
                delete = input('Digite o indice do produto a ser deletado: ') 
                try:
                    delete = eval(delete)
                    lista.pop(delete)
                    deletar = None
                except:
                    print('Por favor, digite um numero valido existente no indice')
            deletar = True
    
    elif opcao == 'S':
        sair = None
