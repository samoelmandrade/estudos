import requests
import csv
from io import StringIO
from datetime import datetime, timedelta, date
import json

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

def save_to_json_file(data, filename):
    with open(filename, "w") as arquivo_json:
        json.dump(data, arquivo_json, indent=4)

def main():
    chk_moeda_values = [61, 222, 115]
    data_atual = date.today()
    data_ini = data_atual - timedelta(days=1)
    data_atual_str = data_atual.strftime("%d/%m/%Y")
    data_ini_str = data_ini.strftime("%d/%m/%Y")
    resultados_json = []

    for chk_moeda in chk_moeda_values:
        csv_text = fetch_currency_data(chk_moeda, data_ini_str, data_atual_str)
        if csv_text:
            resultados_json.extend(parse_csv_to_json(csv_text, chk_moeda))

    if resultados_json:
        save_to_json_file(resultados_json, "moedas.json")
        print("Resultados salvos no arquivo 'moedas.json'.")

if __name__ == "__main__":
    main()
