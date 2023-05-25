import pandas as opcoesPandas

notasAlunos_DF = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao", "Samoel"],
    "Nota1": [9, 7, 10, 0],
    "Nota2": [6, 8, 2, 10],
    "Nota3": [8, 7, 10, 9],
    "Nota4": [9, 8, 8, 8]
})


print("\n---------DATA FRAME NOTAS ALUNOS---------")
print(notasAlunos_DF)
print("\n")
notasAlunos_DF["Média"]=(notasAlunos_DF["Nota1"]+ notasAlunos_DF["Nota2"]+notasAlunos_DF["Nota3"]+notasAlunos_DF["Nota4"]) / 4
print("\n---------DATA FRAME NOTAS ALUNOS MEDIA---------")
print(notasAlunos_DF)
print("\n")
print("\n---------DATA FRAME NOTAS ALUNOS FALTAS---------")
notasAlunos_DF["Faltas"]=5
print(notasAlunos_DF)

novasFaltas = [2,5,3,4]
print(novasFaltas)
notasAlunos_DF["Faltas"] = novasFaltas
print("\n---------DATA FRAME NOTAS ALUNOS NOVAS FALTAS---------")
print(notasAlunos_DF)

novasNotas = [2,5,3,4]
print(novasNotas)
notasAlunos_DF["Nota4"] = novasFaltas
notasAlunos_DF["Média"]=(notasAlunos_DF["Nota1"]+ notasAlunos_DF["Nota2"]+notasAlunos_DF["Nota3"]+notasAlunos_DF["Nota4"]) / 4
print("\n---------DATA FRAME NOTAS ALUNOS NOVAS NOTAS---------")
print(notasAlunos_DF)
print("\n---------DATA FRAME NOTAS ALUNOS NOVAS nota 2---------")
notasAlunos_DF.loc[1,"Nota2"] = 1

notasAlunos_DF["Média"]=(notasAlunos_DF["Nota1"]+ notasAlunos_DF["Nota2"]+notasAlunos_DF["Nota3"]+notasAlunos_DF["Nota4"]) / 4
print(notasAlunos_DF)

notasAlunos_DF.to_json(path_or_buf="D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\arq3.json", orient=None, date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=str, lines=False, compression='infer', index=True, indent=None, storage_options=None, mode='w', )
