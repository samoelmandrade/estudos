from zeep import Client
import requests
from xml.etree import ElementTree as ET
import json

# Nome do arquivo para salvar os resultados
nome_arquivo = 'resultados.json'

# Inicialize uma lista para armazenar todos os resultados
todos_resultados = []

# Definir os parâmetros
user = 'integracao.powerbi'
password = 'Algodoeira@2023'
encryption = 0
offset = 0

while True:
    xml_data = f'''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.senior.com.br">
        <soapenv:Header/>
        <soapenv:Body>
            <ser:Demitidos>
                <user>{user}</user>
                <password>{password}</password>
                <encryption>{encryption}</encryption>
                <parameters>
                    <offset>{offset}</offset>
                </parameters>
            </ser:Demitidos>
        </soapenv:Body>
    </soapenv:Envelope>
    '''

    # URL do serviço web SOAP
    url = 'https://web32.seniorcloud.com.br:36501/g5-senior-services/rubi_Syncbi.consultas?wsdl'  # Substitua pelo URL real do seu serviço web

    # Criar cliente SOAP
    client = Client(url)
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://www.example.com/webservice/SeuMetodo'
    }

    # Envie a requisição POST com o XML
    response = requests.post(url, data=xml_data, headers=headers)

    # Verifique se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Analise a resposta XML
        xml_response = ET.fromstring(response.content)
    
        
        saida_elements = xml_response.findall('.//saida')
        # Encontre o elemento 'DemitidosResponse'
        if not saida_elements:
            break  


        # Inicialize uma lista para armazenar os dados extraídos
        resultado = []

        # Itere sobre os elementos de 'saida' e extraia os valores
        for elemento in saida_elements:
            codCcu = elemento.find('.//codCcu').text
            codFil = elemento.find('.//codFil').text
            datAdm = elemento.find('.//datAdm').text
            datAfa = elemento.find('.//datAfa').text
            desDem = elemento.find('.//desDem').text
            nomCcu = elemento.find('.//nomCcu').text
            nomFun = elemento.find('.//nomFun').text
            numCad = elemento.find('.//numCad').text
            numCpf = elemento.find('.//numCpf').text
            numEmp = elemento.find('.//numEmp').text
            titCar = elemento.find('.//titCar').text

            # Crie um dicionário com os valores e adicione à lista de resultado
            dados = {
                'codCcu': codCcu,
                'codFil': codFil,
                'datAdm': datAdm,
                'datAfa': datAfa,
                'desDem': desDem,
                'nomCcu': nomCcu,
                'nomFun': nomFun,
                'numCad': numCad,
                'numCpf': numCpf,
                'numEmp': numEmp,
                'titCar': titCar,
            }

            resultado.append(dados)

        # Converta a lista de resultado para JSON
        resultado_json = json.dumps(resultado, indent=4)

        # Imprima o resultado em formato JSON
        print(f'offset =  {offset}')
        
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(resultado_json)

        # Aumente o offset em 5000 para a próxima página
        offset += 5000
    else:
        print(f'Erro na requisição HTTP. Código de status: {response.status_code}')
