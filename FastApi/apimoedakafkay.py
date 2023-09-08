import requests
import csv
from io import StringIO
from datetime import datetime, timedelta, date
import json
from confluent_kafka import Producer

def fetch_currency_data(chk_moeda, start_date, end_date):
    url = f"https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda={chk_moeda}&DATAINI={start_date}&DATAFIM={end_date}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"A requisição para ChkMoeda {chk_moeda} falhou com o status:", response.status_code)
        return None

def parse_csv_to_json(csv_text, chk_moeda):
    results = []

    csv_data = StringIO(csv_text)
    csv_reader = csv.reader(csv_data, delimiter=';')

    for row in csv_reader:
        if len(row) >= 5:
            data = datetime.strptime(row[0], "%d%m%Y").strftime("%Y-%m-%d")
            tipo_moeda = row[3]  # Posição 3 contém o tipo de moeda
            valor_moeda = row[4]  # Posição 4 contém o valor da moeda

            resultado = {
                "ChkMoeda": chk_moeda,
                "Data": data,
                "TipoMoeda": tipo_moeda,
                "ValorMoeda": valor_moeda
            }

            results.append(resultado)

    return results

def send_to_kafka_topic(data, topic, bootstrap_servers):
    producer_config = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'moedas-producer'
    }

    producer = Producer(producer_config)

    for item in data:
        producer.produce(topic, key=str(item["ChkMoeda"]), value=json.dumps(item))

    producer.flush()

def main():
    chk_moeda_values = [61, 222, 115]
    data_atual = date.today()
    data_ini = data_atual - timedelta(days=5)
    data_atual_str = data_atual.strftime("%d/%m/%Y")
    data_ini_str = data_ini.strftime("%d/%m/%Y")
    resultados_json = []

    for chk_moeda in chk_moeda_values:
        csv_text = fetch_currency_data(chk_moeda, data_ini_str, data_atual_str)
        if csv_text:
            resultados_json.extend(parse_csv_to_json(csv_text, chk_moeda))

    if resultados_json:
        kafka_bootstrap_servers = '20.84.11.171:9094'  # Substitua pelo endereço do seu cluster Kafka
        kafka_topic = 'moeda'  # Substitua pelo tópico desejado

        send_to_kafka_topic(resultados_json, kafka_topic, kafka_bootstrap_servers)
        print("Resultados enviados para o tópico Kafka 'moeda'.")

if __name__ == "__main__":
    main()
