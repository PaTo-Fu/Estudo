import copy


pessoa = {
    'nome': 'André',
    'sobrenome': 'Manzano',
    'idade': 25,
    'altura': '1,75',
    'peso': '95kg',


}
print(pessoa['nome'])
#as chaves criam um dicionário, uma lista a qual eu posso dar nomes aos indices, fica mais facil de encontrar algo dentro dela

pessoa_2 = {}

pessoa_2['nome'] = 'André' #cria nova chave

chave = 'nome' #chave dinamica cria chaves e pesquisa também
print(pessoa_2[chave])
pessoa_2[chave] = 'marcos'
print(pessoa_2[chave])
if pessoa_2.get('sobrenome') is None:
    print('Não existe')


d1 = {
    'c1': 1,
    'c2': 2,
    }
d2 = d1 # o = está dizendo que d2 aponta à mesma unidade de memoria que d1

d2['c1'] = 10 # ao tentar editar a d2 acabamos modificando diretamente a d1

print(d1)

    # Dicionários são mutaveis, o sinal '=' aponta para a maesma unidade da memoria, cuidado para não mutar uma lista ao invez de copiar
d2 = d1.copy() #d2 fará uma cópia rasa de d1, se tiver algo mutável dentro de d1, ele não será copiado, mas sim apontados, cuidado para não modificar sem querer

d2 = copy.deepcopy(d1) #faz uma cópia 'profunda' de d1, copiando inclusive valores mutáveis, podendo ser editado preservando d1
ultima_chave = d2.popitem() #faz a ultima_chave pegar o valor da ultima chave de d2, e apaga a chave de d2
d2.update({
    'nome': 'pato',
    'c2': 'não'

})
print(d2)