
produtos_list = [
    'arroz',
    'feijao',
    'laranja',
    'banana',
    'maça'
]
produtos_tuple = (
    'arroz',
    'feijao',
    'laranja',
    'banana',
    'maça'
)

print('--------------------')
print(type(produtos_tuple))
print('--------------------')
print(type(produtos_list))
print(produtos_list)
print('--------------------')
print(produtos_tuple)
print('--------------------')
produtos_list.append('bergamota')
print(produtos_list)
print('--------------------')
#nao pode fazer
'''
produtos_tuple.append('bergamota')
print(produtos_tuple)
'''
