import os

palavra_secreta = 'paralelepipedo'
letras_acertadas = ''
tentativas = 0
acertos = 0



















while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_digitada) > 1:
        print('digite apenas uma letra.')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        acertos += 1


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
             palavra_formada += letra_secreta
        else:
                palavra_formada += '*'
                
    print('Palavra formada: ', palavra_formada)
    

    if palavra_formada == palavra_secreta:
         os.system('cls')
         print('Parabens, Você ganhou')
         print('total de tentativas: ', tentativas)
         print('A palavra era: ', palavra_secreta)
         palavra_secreta = 'paralelepipedo'
         letras_acertadas = ''
         tentativas = 0
         acertos = 0
