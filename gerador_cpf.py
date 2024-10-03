import os
programa = True

while programa:
    cpf = input('Por favor, digite aqui o seu cpf sem pontos nem traços: ')
    nove_digitos = cpf[:9]
    dez_digitos = cpf[:10]
    primeiro_verificador = cpf[-2]
    resultado = 0
    resultado2 = 0
    contador_regressivo = 10
    segundo_contador = 11
    if cpf.isdigit() != True:
        print('por favor, Digite apenas numeros')
        continue
    primeiro_verificador = int(primeiro_verificador)
    for numero in nove_digitos:
        resultado += int(numero) * contador_regressivo
        contador_regressivo -= 1
    if resultado%11<2:
        primeiro_digito = 0
        contador_regressivo = 10
    else:
        primeiro_digito = 11-(resultado%11)
        contador_regressivo = 10



    for segundo in dez_digitos:
        resultado2 += int(segundo) * segundo_contador
        segundo_contador -= 1
    if resultado2%11<2:
        segundo_digito = 0
        segundo_contador = 11
    else:
        segundo_digito = 11 - (resultado2%11)

    print('Seu cpf é: ', nove_digitos, primeiro_digito, segundo_digito )


