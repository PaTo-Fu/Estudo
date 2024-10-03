import os

s1 = set('luiz') 
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setvazio = set()
print(s1)
print(type(s2))

#set() é perfeito para remover iteraveis duplicados

l1 = [1,2,3,4,5,6,6,5,2,4,89,6,2,4]
s3 = set(l1)
l2 = list(s3)
print(l2)

for i in s1:
    print(i)

input('apagar')
os.system('cls')

s3.add('andre')
print(s3)
s3.add(1)
print(s3)
s3.update('ola, mundo')#will iterate the item, it means that will send item by item, without an order
print(type(s3))
print(s3)
s3.discard(' ')
print(s3)
input('apagar')
os.system('cls')

#operadores do set
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #pipe is union between s1 and s2
print(s3)
s3 = s1 & s2 #ampersand is the intersection between s1 and s2, it will result in the itens that repeat in both sets
print(s3)
s3 = s1 - s2 #will show itens that are in the s1 but not in s2 (aways show the iten on left)
print(s3)
s3 = s2 ^ s1 #will show the simetric diference between s1 and s2
print(s3)