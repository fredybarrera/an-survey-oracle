#-------------------------------------------------------------------------------
# Name:         main
# Purpose:      
#               
#               
#
# Author:       Fredys Barrera Artiaga <fbarrera@esri.cl>
# Created:      23-07-2020
# Copyright:    (c) fbarrera 2020
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import utils
import constants as const
import requests
import xml.etree.ElementTree as et
import urllib.request as ur
import traceback
import os
import time
import json
from datetime import datetime, timedelta

# Ruta absoluta del script
script_dir = os.path.dirname(__file__)


def main():
    """Main function."""

    timeStart = time.time()
    utils.log("Proceso iniciado..." + str(datetime.now()))

    print("Obteniendo token... ")
    token = utils.get_token()
    print('token: ', token)

    print("Conectando con Oracle... ")
    conn = utils.get_conexion_oracle()

    test_conexion(conn)

    # process(token, conn)

    # end_process(timeStart)




def process(token, conn):
    """Inicio del proceso de obtención de la data y la carga en Oracle."""

    try:
        # Obtengo la cantidad total de registros de la capa.
        response = requests.get(
            const.URL_QUERY_FALLA_MATRIZ, params=utils.get_params_count(token), headers=utils.get_headers())
        response_json = json.loads(response.text)
        cantidad_registros = response_json['count']
        print('Se descargarán un total de {} registros'.format(cantidad_registros))
        utils.log('Se descargarán un total de {} registros'.format(cantidad_registros))

        record_count = 2000
        print('Consultando lotes de {} registros'.format(record_count))
        utils.log('Consultando lotes de {} registros'.format(record_count))

        if cantidad_registros > 0:
            # Divido el total de registros de la capa por 2000
            cantidad_paginas = get_cantidad_por_pagina(cantidad_registros, record_count)
            offset = 0
            print('Cantidad total de lotes: ', cantidad_paginas)
            utils.log('Cantidad total de lotes {}'.format(cantidad_paginas))
            for lote in range(0, cantidad_paginas):
                print('Descargando lote {0}: '.format(lote + 1))
                utils.log('Descargando lote {0}: '.format(lote + 1))
                response = requests.get(
                    const.URL_QUERY_FALLA_MATRIZ, params=utils.get_params_query(token, offset, record_count), headers=utils.get_headers())
                response = json.loads(response.text)
                offset += record_count
                # Proceso los datos obtenidos de las fallas de matrices, obtengo:
                # - Attachments de las fallas
                # - Estanques
                # - Valvulas buenas
                # - Valvulas malas
                # - Cortes
                if len(response['features']) > 0:
                    process_data(response, token, conn)


    except:
        print("Failed process (%s)" % traceback.format_exc())
        utils.error_log("Failed process (%s)" % traceback.format_exc())


def process_data(response, token, conn):
    """
    Guardo las fallas de las matrices.
    Por cada falla, obtengo los attachments, estanques, valvulas buenas y malas y los cortes.
    """

    try:
        fields = []
        data = []
        values = []
        str_values = ''
        for field in response['fields']:
            fields.append(field['name'])

        str_values = ':' + ',:'.join(fields)
        
        # print('str_values: ', str_values)

        for feature in response['features']:
            # print('feature[attributes]: ', feature['attributes'])
            values = []
            for key, val in feature['attributes'].items():
                values.append(val)
            data.append(tuple(values))
        

        table = const.FALLA_MATRIZ
        
        sql = ('insert into {0} {1} values ({2})').format(table, tuple(fields), str_values)

        print('sql: ', sql)
        print('data: ', data)

        utils.insert_data(conn, sql, data)


    except:
        print("Failed process_data (%s)" % traceback.format_exc())
        utils.error_log("Failed process_data (%s)" % traceback.format_exc())


def get_cantidad_por_pagina(cantidad, datos_pagina):
    """Permite obtener la cantidad de registros por página."""

    try:
        page = divmod(cantidad, datos_pagina)
        cantidad_paginas = page[0]
        if page[0] == 0:
            cantidad_paginas = 1
        if page[1] != 0:
            cantidad_paginas = cantidad_paginas + 1
        return cantidad_paginas

    except:
        print("Failed get_cantidad_por_pagina (%s)" % traceback.format_exc())
        utils.error_log("Failed get_cantidad_por_pagina (%s)" % traceback.format_exc())


def test_conexion(conn):
    """Function one."""

    try:
        c = conn.cursor()
        c.execute('select * from CORTE')
        for row in c:
            print (row[0], '-', row[1], '-', row[2])
        conn.close()
    except:
        print("Failed test_conexion (%s)" % traceback.format_exc())
        utils.error_log("Failed test_conexion (%s)" % traceback.format_exc())


def end_process(timeStart):
    """Muestra y registra informacion sobre la ejecución del proceso."""

    timeEnd = time.time()
    timeElapsed = timeEnd - timeStart
    print("Proceso finalizado... " + str(datetime.now()))
    print("Tiempo de ejecución: " + str(utils.convert_seconds(timeElapsed)))
    utils.log("Tiempo de ejecución: " + str(utils.convert_seconds(timeElapsed)))
    utils.log("Proceso finalizado \n")


if __name__ == '__main__':
    main()
