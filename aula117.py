def multiplica(a):
    def multiplicando(b):
        return a * b
    return multiplicando   

primeiro = input('Digite um numero: ')
segundo = input('Quer multiplicar por quanto? ')
primeiro = int(primeiro)
segundo = int(segundo)
multiplicador = multiplica(primeiro)
multiplicado = multiplicador(segundo)

print(f'O resultado de {primeiro} multiplicado {segundo} vezes é {multiplicado}')
#isso se chama closure, funções que retornam funções