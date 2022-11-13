import os
import requests
from datetime import datetime

base_dir = os.getcwd()

shop_list = [{'id': 1026, 'name': 'PradoN'}]

#username = 'api@karemexico.com'
password = 'u20a7r2u'
dash = 'perfTurn'
url = 'https://reports.kare.de/pentaho/dataUpload'
fecha = str(datetime.now().strftime("%d%m%Y"))
csv_folder = r'../kare_conexion_api_performance/'

for shop in shop_list:
    print('Subiendo para la tienda : ', shop['name'])
    parameters = {'shop_id': shop['id'], 'dash': dash, 'user': username}

    with open(os.path.join(csv_folder, 'kare_performance_' + shop['name'] + '_' + fecha + "_gusardi" + '.csv'), 'r') as f:
        reader = f.read()
        # print (reader_stationary)

    r_request = requests.post(url=url, params=parameters, data=reader.encode('utf-8'), auth=(username, password))
    print(r_request.text)
