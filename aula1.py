nome = "Andre Ricardo"
n = 0
nome_alterado = ''
while n < len(nome):
    letra = nome[n]
    nome_alterado += letra + '-'
    n += 1
print (nome_alterado)