import pandas as pd

dadosDAtaFrame = pd.read_excel("D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Tratamento_Dados.xlsx"
                               )
print(dadosDAtaFrame)

'''dadosDAtaFrame = dadosDAtaFrame.dropna()
'''

print('\n')
print(dadosDAtaFrame)
print('\n')


# print('MEDIA COLOCAR EM LUGAR DE BRANCO NAN')
# dadosDAtaFrame['Total Vendas'] = dadosDAtaFrame['Total Vendas'].fillna(dadosDAtaFrame['Total Vendas'].mean())
'''print('FIXAR VALOR COLOCAR EM LUGAR DE BRANCO NAN')
print('\n')
dadosDAtaFrame['Total Vendas'] = dadosDAtaFrame['Total Vendas'].fillna(5)
print(dadosDAtaFrame)
print('\n')'''

print('PEGAR ULTIMO VALOR VALIDO VALOR COLOCAR EM LUGAR DE BRANCO NAN')
print('\n')
dadosDAtaFrame['Total Vendas'] = dadosDAtaFrame['Total Vendas'].ffill()
print(dadosDAtaFrame)
print('\n')

#valeu counts - conta qualntas linhas/ vendas foram feitas
print('vendas foram feitas : ')
print('\n')
qtdVendas = dadosDAtaFrame["Vendedor"].value_counts()
print(qtdVendas)
print('\n')
      
print('Soma tudo dos vendedores:')
excluirLinha3 = dadosDAtaFrame.drop('Data Venda',axis=1)
VendaVendedor = excluirLinha3.groupby("Vendedor").sum()
print(VendaVendedor)
print('\n')
