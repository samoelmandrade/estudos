import pandas as pd

baseVenda_DF = pd.read_excel("D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Ordenação.xlsx")

print("\n Imprimindo dados \n")
print(baseVenda_DF)
print("\n")

#sort_values = ele ordena a coluna
ordenarVendedor = baseVenda_DF.sort_values(by="Vendedor")

print("\n Ordenando pela coluna de vendedor \n")
print(ordenarVendedor)
print("\n")

#------------------------------------------------

ordenarProduto = baseVenda_DF.sort_values(by="Produto")

print("\n Ordenando pela coluna de Produto \n")
print(ordenarProduto)
print("\n")

#------------------------------------------------

ordenarDataVenda = baseVenda_DF.sort_values(by="Data Venda")

print("\n Ordenando pela coluna da Data da Venda \n")
print(ordenarDataVenda)
print("\n")

#------------------------------------------------

ordenarTotalVendas = baseVenda_DF.sort_values(by="Total Vendas")

print("\n Ordenando pela coluna de Total Vendas \n")
print(ordenarTotalVendas)
print("\n")

#------------------------------------------------

ordenarDuasColunas = baseVenda_DF.sort_values(by=["Vendedor", "Produto"])

print("\n Ordenando pelas colunas de Vendedor e Produtos \n")
print(ordenarDuasColunas)
print("\n")

#------------------------------------------------

#ascending = Ordena do maior para o menor
#False = Z a A
#True = A a Z
ordenarZaA = baseVenda_DF.sort_values(by="Vendedor", ascending=False)

print("\n Ordenando Vendedor de Z a A \n")
print(ordenarZaA)
print("\n")

#-----------------------------------------------

ordenarTotalVendasZaA = baseVenda_DF.sort_values(by="Total Vendas", ascending=False)

print("\n Ordenando Total Vendas de Z a A \n")
print(ordenarTotalVendasZaA)
print("\n")