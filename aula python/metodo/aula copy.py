my_list = list(range(0,11,2))

for item in my_list:
    print(item)
    
for numero in my_list:
    print(numero**2)

armazem=[   {
      "ShippingInstructionCode":"SPRINT65-ME-FOB-01",
      "Code":"HC1",
      "NewCode":"",
      "ReturnDate":"29/07/2023 14:00",
      "WithdrawalDate":"29/06/2023 14:00",
      "TareWeight":3000,
      "Payload":28000,
      "Seal":"448",
      "Responsible":"",
      "Window":"22/08/2023 5:10",
      "Warehouse":"ISIS"
   }, 
    {
      "ShippingInstructionCode":"SPRINT70-ME-CIF-002",
      "Code":"HC1983",
      "NewCode":"",
      "ReturnDate":"",
      "WithdrawalDate":"29/05/2023 14:00",
      "TareWeight":3000,
      "Payload":28000,
      "Seal":"4499",
      "Responsible":"",
      "Window":"23/08/2023 5:10",
      "Warehouse":"ISIS"
   }]

print(armazem[0]['Window'])


print ('------------------------------------------------------')

class Funcionario():
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return{'nome': self.nome, 'salario': self.salario}

class Admin(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)
    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()
        
fabio = Funcionario('Fabio',7000)

print(fabio.dados())

fernando =Admin("Fernando",14000)

print(fernando.atualizar_dados("fernandinho"))

fernando.dados()

