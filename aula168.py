# def zipper(lista1, lista2):
#     max_interval = min(len(lista1),len(lista2))
    
#     return [
#         (lista1[i],lista2[i]) for i in range(max_interval)
#     ]
from itertools import zip_longest
cidades = ['salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(cidades,estados))
print(list(zip(cidades,estados)))
print(list(zip_longest(cidades,estados, fillvalue='SEM CIDADE')))
