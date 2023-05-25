import pandas as pd

dataFrameDados = pd.read_excel(
    "D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Deletar_Linhas_Colunas.xlsx")

print(dataFrameDados)
print('\n')
print(type(dataFrameDados))
print('\n')


print('Somente linhas com dados')
deletandoLinhasEmBranco = dataFrameDados.dropna()
print(deletandoLinhasEmBranco)
print('\n')

'''print('deletando coluna produto')
del deletandoLinhasEmBranco["Produto"]
print(deletandoLinhasEmBranco)
print('\n')'''

print('deletando linhas produto e data venda')
deletandoDuasColunas = deletandoLinhasEmBranco.drop(columns=["Produto" , "Data Venda"])
print(deletandoDuasColunas)
print('\n')
print('deletando linha 2')
#axis = eixo(1 - coluna , 0 - linha)
excluirLinha3 = deletandoDuasColunas.drop(2,axis=0)
print(excluirLinha3)
print('\n')
print('deletando linha 1 ')
#axis = eixo(1 - coluna , 0 - linha)
excluirLinha2 = deletandoDuasColunas.drop(1,axis=0)
print(excluirLinha2)
print('\n')