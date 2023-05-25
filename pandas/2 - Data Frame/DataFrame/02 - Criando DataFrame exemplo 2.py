import pandas as opcoesPandas
import numpy as opcoesNumpy
import json as json

print('\n----------------------numeros aleatorios 15 linhas e 10 colunas ALTERANDO O NOME DA COLUNA ')
numeros_aleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(
    15, 10)*100, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print(numeros_aleatorios)
print('\n')

print(numeros_aleatorios.columns)


notaAlunos_DataFrame = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao","Samoel"],
    "Media": [9, 7, 10,0]
})


print("\n----dataFrame dicionario notas alunos\n")
print(notaAlunos_DataFrame)



notaAlunos_DataFrame.to_json(path_or_buf="D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\arq2.json", orient=None, date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False, compression='infer', index=True, indent=None, storage_options=None, mode='w', )


caminho = "D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\arq2.json"
with open(caminho, encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
print(dados) 

