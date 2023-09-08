import datetime as date

class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
            self.nome = nome
            self.sobronome = sobrenome
            self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobronome
    
    def calcula_idade(self):
        ano_atual = date.datetime.now().year
      
        self.ano_nascimento = int(ano_atual - self.data_nascimento)
        return self.ano_nascimento
    



a1 = Funcionarios('Elena', 'Cabral',2009)
a2 = Funcionarios('samoel', 'maciel',1982)
a3 = Funcionarios('marceli', 'lauxen',1982)


print(Funcionarios.nome_completo(a2))
print(Funcionarios.calcula_idade(a2))