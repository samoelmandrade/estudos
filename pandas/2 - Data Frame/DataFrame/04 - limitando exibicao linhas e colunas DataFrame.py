import pandas as opcoesPandas
import math

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

print("INDEX exibe apenas as informaçoes as ultimas 3 linhas do DATAFRAME ")
print(vendas_DF["Vendedor"])
print("\n")


print("Exibe TOTAL : ")
total_vendas =math.fsum(vendas_DF["Total Vendas"])
print(str(total_vendas))
print("\n")