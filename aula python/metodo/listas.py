'''
numeros = [2,3,4,5]

final = numeros *4

print(final)
'''
'''
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

final = numeros + letras
print(final)

numeros.extend(letras)
print(numeros)

'''
'''
itens = [['item1', 'item2'], ['item3', 'item4']]

print(itens[1][1])
'''
produtos = [
    'arroz',
    'feijao',
    'laranja',
    'banana',
    'maça'
]

item1, item2, item3, *outros = produtos

print(produtos[2])

print('--------------------')

print(item1)

print('--------------------')

print(outros)
