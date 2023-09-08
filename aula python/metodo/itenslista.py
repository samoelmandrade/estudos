

cores = ['amarelo', 'azul', 'verde', 'branco']

cor_cliente = input('digite a cor desejada: ')
if cor_cliente.lower() in cores:
    print('temos em estoque')
else:
    print("nao temos a cor desejada")


