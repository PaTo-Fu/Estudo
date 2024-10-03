# #funções geradoras, funções que pausam

# def generator(n=0):
#     yield 1 #pausa a função
#     print('continuando')
#     yield 2
#     yield 'testando'
#     return 'acabou' #esse não retorna

# gen = generator(n=0)
# print(gen)
# print(next(gen)) #next passa pra próxima linha da função
# print(next(gen))
# print(next(gen))
# print(next(gen))
def generator(n=0, maximum=10):
    while True:
        yield n
        n +=1
        if n > maximum:
            return n




gen = generator()
for n in gen:
    print(n)