import requests
import csv
import json

# Função para fazer a solicitação à API e obter dados CSV
def get_csv_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Falha ao obter os dados da API")

# Função para converter dados CSV para JSON
def csv_to_json(csv_data):
    csv_reader = csv.DictReader(csv_data.splitlines(), delimiter=';')
    json_data = []
    for row in csv_reader:
        json_data.append(row)
    return json_data
class Laptop:
	def __init__(self, name, processor):
		self.name = name
		self.processor = processor
	
  
# Função para cadastrar os valores dos campos em uma estrutura de dados
def register_data(json_data):
    registered_data = {}  # Usar um dicionário para armazenar os dados
    for entry in json_data:
        campo1, campo2, campo3, campo4, campo5, campo6, campo7 = entry  # Supondo três campos no CSV
        data = campo1
        tipo = campo2
        classifica = campo4
        valor = campo5
        Laptop(campo1,campo2)
        print(str(Laptop[data]))
        
    return Laptop

def main():
    api_url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI=12/08/2023&DATAFIM=22/08/2023"
    csv_data = get_csv_data_from_api(api_url)
    json_data = csv_to_json(csv_data)
    registered_data = register_data(json_data)
    print("Dados cadastrados:")
    print(json.dumps(registered_data, indent=4))

if __name__ == "__main__":
    main()
