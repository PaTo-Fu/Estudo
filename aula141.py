import pprint

produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório',

}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'

}

lista = [
('a', 'valor a'),
('b', 'valor b'),
('c', 'valor c'),

]
dc = {
    chave: valor 
    for chave, valor in lista

}
print(dc)
lista = [n for n in range(10)]

generator = (n for n in range(10)) # () para criar um generator, uma funcão que dá varios numeros, mas que pauza, sem guardar os numeros na memoria