from itertools import zip_longest

lia = [1,2,3,4,5,6,7]
lib = [1,2,3,4]
def soma(lista1, lista2):
    max_interval = min(len(lista1), len(lista2))
    return [
        lista1[i] + lista2[i] for i in range(max_interval)
    ]

print(soma(lia, lib))
lista_soma = [x + y for x, y in zip(lia,lib)]

biggest_list = [x + y for x,y in zip_longest(lia,lib, fillvalue=0)]

print(biggest_list)



# for i in range(len(lib)):
#     lista_soma.append(lia[i] + lib[i])
print(lista_soma)