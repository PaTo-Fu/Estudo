# Exercício - sistema de perguntas e respostas

a = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
pergunta1 = perguntas[0]
pergunta2 = perguntas[1]
pergunta3 = perguntas[2]
r1 = input(pergunta1['Pergunta'])
if r1 == pergunta1['Resposta']:
    print('Parabens, resposta correta')
    a += 1
else:
    print('não foi dessa vez, você errou')
    
r2 = input(pergunta2['Pergunta'])
if r2 == pergunta2['Resposta']:
    print('Parabens, resposta correta')
    a += 1
else:
    print('não foi dessa vez, você errou')

r3 = input(pergunta3['Pergunta'])
if r3 == pergunta3['Resposta']:
    print('parabens, resposta correta')
    a += 1
else:
    print('não foi dessa vez, você errou')

print(f'Você acertou {a} perguntas')