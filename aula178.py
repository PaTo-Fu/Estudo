from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 105},
    {'nome': 'Produto 4', 'preco': 69},

]

def funcao_do_reduce(prev, produto): # pode ser trocado por:
    print('Acumulador: ', prev)      #lambda ac, p: ac +p['preco]
    print('Produto: ', produto)
    print()
    return prev + produto['preco']


total2 = reduce(
    funcao_do_reduce,       #função do reduce
    produtos,               #item à ser reduzido
    0                       #valor padrão para evidar bugs
)

total = 0
for p in produtos:
    total += p['preco']

print(total)
print(total2)
