from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()



pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia'
]
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculina', 'Feminina', 'Unisex'],
    ['Algodão', 'Poliester']
]


print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
