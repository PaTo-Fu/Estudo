from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'joana', 'nota': 'D'},
    {'nome': 'joao', 'nota': 'B'},
    {'nome': 'eduardo', 'nota': 'A'},
    {'nome': 'andre', 'nota': 'C'},
    {'nome': 'anderson', 'nota': 'A'},
    
]
def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)


# print(grupos)


# alunos = ['a','a','a','a', 'b', 'c','a',]

# grupos = groupby(alunos)

# for chave, grupo in grupos:
#     print(list(grupo))