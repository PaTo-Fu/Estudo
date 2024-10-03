# RECURSIVAS:                                                  #
# funções que podem se chamar de volta                         #
# uteis p/ dividir problemas em partes menores                 #
# toda função recursiva deve ter:                              #
# - um problema que possa ser dividido em partes menores       #
# - um caso recursivo que resolve esse pequeno problema        #
# - um caso base que pare a recursão                           #
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1                     #
################################################################
# def recursiva(inicio=0, fim=10):
#     #caso recursivo
#     #contar até o final
#     inicio += 1
#     if inicio >= fim:
#         return print(f'{inicio}/{fim} cheguei ao final')
#     print(f'{inicio}/{fim}')
#     return recursiva(inicio, fim)

# recursiva()

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(8))
print(factorial(9))
