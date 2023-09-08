import pandas as pd
import numpy as np
import plotly.express as px

temp = pd.read_excel("D:\\curso\\Livro1.xlsx",engine = "openpyxl")
#print(temp)

entrada= np.nansum(temp["maio"]) 
print("%.2f" % round(12954- entrada))
#print (entrada)

dados_x=temp["maio"]
dados_y=temp["junho"]

fig=px.line(x=dados_x, y=dados_y, title="Vendas x Ano", height=400, width=1000)
fig.update_yaxes(title='Vendas', title_font_color='red', ticks='outside', tickfont_color='yellow')
fig.show()
