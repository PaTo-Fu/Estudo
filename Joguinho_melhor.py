import os
import random
from unidecode import unidecode
escape = True
while escape:
    numero_aleatorio = random.randint(0,180)
    nome_arquivo = "C:/Users/andre/Desktop/Python/aulas/Forca/palavras.txt"
    lista_palavras = []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                palavra = linha.strip()
                lista_palavras.append(palavra)
    except FileNotFoundError:
        print('O arquivo {nome_arquivo} não foi encontrado')

    def remover_acentos(palavra):
        return unidecode(palavra)
    
    lista_sem_acentos = list(map(remover_acentos, lista_palavras))


    palavra_secreta = lista_sem_acentos[numero_aleatorio]
    
    rgt_lttrs = ''
    segredo = '_ ' * len(palavra_secreta)
    print(segredo)
    tentativas = 0
    acertos = 0
    erros = 0
    restart = True

    while restart:
        letra = input('Digite uma letra para tentar adivinhar a palavra: ')
        if len(letra) > 1:
            print('Por favor, digite apenas uma letra por vez')
            continue

        if letra in palavra_secreta:
            acertos += 1
            tentativas += 1
            rgt_lttrs += letra
        else:
            tentativas += 1
            erros += 1
        palavra_formada = ''

        for letra_secreta in palavra_secreta:
            if letra_secreta in rgt_lttrs:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '_ ' 
        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            palavra_formada = palavra_formada.upper()
            os.system('cls')
            print('Parabens! você acertou!')
            print(f'A palavra é : {palavra_formada}')
            print(f'Voce teve um total de {tentativas} tentativas')
            print(f'Totalizando {erros} erros')
            print(f'Com {acertos} acertos no total')
            sair = input('Digite [S]air para sair ou [R]einiciar para reiniciar: ')
            sair = sair.upper().startswith('S')

            if sair == True:
                escape = False
                os.system('cls')
                break
            else:
                os.system('cls')
                restart = None
                continue