import pandas as pd

baseVendas_DF = pd.read_excel(
    "D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Base_Vendas.xlsx")
print('\n')
print('IMPRIMINDO OS DADOS')
print(baseVendas_DF)
print('\n')

#nunique - resumo dos itens
resumovaloresUnicos = baseVendas_DF.nunique()
print('IMPRIMINDO OS DADOSa resumo')
print(resumovaloresUnicos)

print('\n')
#first,False, last
print('IMPRIMINDO OS DADOSa veiricar duplicidade')
confereDuplicidades = baseVendas_DF.duplicated(subset='Vendedor', keep='first')
print(confereDuplicidades)
print('\n')


print('IMPRIMINDO OS DADOSa veiricar duplicidade com nova coluna')
print('\n')
baseVendas_DF['Confere Duplicidade'] = baseVendas_DF.duplicated(subset="Vendedor", keep='first')
print(baseVendas_DF)
print('\n')
removerDuplicidade = baseVendas_DF.drop_duplicates(subset="Vendedor",keep='first')
print(removerDuplicidade)
print('\n')