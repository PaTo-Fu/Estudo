#funções decoradoras e decoradores
#decorar = adicionar / remover / restringir / alterar
#é uma forma de alterar uma função sem mexer na função?
#funções decoradoras são funções que decoram outras funções
#Decoradores são usados para fazer o Python
#usar as funções decoradoras em outras funções
def create_function(func):
    def intern(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            is_string(arg)        
        result = func(*args, **kwargs)

        print(f'ok, você foi decorado, seu resultado é {result}')
        return result
    return intern


@create_function #usa criar função automaticamente nesta func
def invert_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param must be a string")
    

invertida = invert_string('123456')
print(invertida)