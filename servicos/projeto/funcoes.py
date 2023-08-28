def somar(x,y):
    return x + y

def mult():
    print('essa funçao vai multiplicar os valores: ')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor ==  item:
            return i
    return -1