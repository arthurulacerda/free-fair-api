import csv
import requests

BASE_URL = 'http://127.0.0.1:5000'

with open('data/DEINFO_AB_FEIRASLIVRES_2014.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0 or len(row) < 2:
            line_count += 1
        else:
            data = {
                'longitude':row[1],
                'latitude':row[2],
                'setcens':row[3],
                'areap':row[4],
                'coddist':row[5],
                'distrito':row[6],
                'codsubpref':row[7],
                'subpref':row[8],
                'regiao5':row[9],
                'regiao8':row[10],
                'nome_feira':row[11],
                'registro':row[12],
                'logradouro':row[13],
                'numero':row[14],
                'bairro':row[15],
                'referencia':row[16]
            }

            response = requests.post(f'{BASE_URL}/v1/fair', data)
