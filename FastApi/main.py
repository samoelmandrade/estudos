import sqlite3



con = sqlite3.connect("D:\\curso\\sqlite3\\db\\Chinook")
cur = con.cursor()

def INSERT_TABLE(titulo,ano,score):
    data = [
    (titulo, ano, score)
]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit() 
    return True

'''titulo = (input("DIGITE O TITULO: "))
ano = int(input("qual O ANO: "))
score = int(input("SCORE: "))

retorno = INSERT_TABLE(titulo=titulo,ano=ano,score=score)
print(retorno)
'''
print('--------------------------')
nome = 'NERCI'

res = con.execute("SELECT title, year, score FROM movie mo where mo.title like name = '(nome)'" )



title, year , score = res.fetchone()
print ('RETORNO DA TABELA')
print(f'TITULO:  {title!r}, ANO:  {year} E PONTUAÇAO:  {score}')