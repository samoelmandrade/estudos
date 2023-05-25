import pandas as opcoesPandas




vendas_DF = opcoesPandas.read_excel(
    "D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Vendas_Jan.xlsx")

print(vendas_DF)
print("\n")

print("INDEX exibe apenas as informaçoes as linhas do DATAFRAME ")
print(vendas_DF.index)
print("\n")
print("INDEX exibe apenas as informaçoes as colunas do DATAFRAME ")
print(vendas_DF.columns)
print("\n")

print("INDEX exibe apenas as informaçoes as 5 primeiras linhas do DATAFRAME ")
print(vendas_DF.head())
print("\n")

print("INDEX exibe apenas as informaçoes as 10 primeiras linhas do DATAFRAME ")
print(vendas_DF.head(10))
print("\n")


print("INDEX exibe apenas as informaçoes as ultimas 3 linhas do DATAFRAME ")
print(vendas_DF.tail(3))
print("\n")

print("IMPRIMINDO UMA COLUNA DATAFRAME ")
print(vendas_DF["Vendedor"])
print("\n")

print("IMPRIMINDO MAIS DE UMA COLUNA DATAFRAME ")
print(vendas_DF[["Vendedor","Total Vendas"]])
print("\n")


print("IMPRIMINDO 2 linhas do DATAFRAME ")
print(vendas_DF.loc[0:2])
print("\n")

#loc = localizar
vendas_Leonardo_Almeida_DF = vendas_DF.loc[vendas_DF["Vendedor"]=='Leonardo Almeida']
print("IMPRIMINDO linhas do Leonardo Almeida DATAFRAME ")
print(vendas_Leonardo_Almeida_DF)
print("\n")
'''
vendas_Leonardo_Almeida_DF = vendas_DF.loc[vendas_DF["Vendedor"]=='Leonardo Almeida']
print("IMPRIMINDO linhas do Leonardo Almeida nome e total de vendas DATAFRAME ")
print(vendas_Leonardo_Almeida_DF[["Vendedor","Total Vendas"]])
print("\n")'''



vendas_Leonardo_Almeida_DF = vendas_DF.loc[vendas_DF["Vendedor"]=='Leonardo Almeida',["Vendedor","Total Vendas"]]
print("IMPRIMINDO linhas do Leonardo Almeida nome e total de vendas DATAFRAME ")
print(vendas_Leonardo_Almeida_DF)
print("\n")

#loc = localizar
print("IMPRIMINDO total linhas em colunas DATAFRAME ")
print(vendas_DF.shape)
print("\n")


print("IMPRIMINDO invertendo  linhas em colunas DATAFRAME ")
transformarLinhasEmColunas = vendas_DF.T
print(transformarLinhasEmColunas)