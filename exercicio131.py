lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def duplicados(a):
    l1 = []
    d2 = []
    for i in a:        
        d1 = []
        d = -1      
        s3 = set()
        l1 = i
        for j in l1:
            if j in s3:
                if d == -1:
                    d1.append(j)
                    d = 1
            s3.add(j)
        if len(d1) < 1:
            d2.append(-1)
        else:
            d2.append(d1)

    return d2

        
    
result = duplicados(lista_de_listas_de_inteiros)
for i in result:

    print(i)
