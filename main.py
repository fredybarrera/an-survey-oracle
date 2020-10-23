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
import cx_Oracle
from datetime import datetime, timedelta
import platform

# Ruta absoluta del script
script_dir = os.path.dirname(__file__)
LOCATION = r"C:\oracle\instantclient_19_8"


def main():
    """Main function."""

    print("ARCH:", platform.architecture())
    print("FILES AT LOCATION:")

    for name in os.listdir(LOCATION):
        print(name)
        os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

    timeStart = time.time()
    utils.log("Proceso iniciado..." + str(datetime.now()))

    print("Obteniendo token... ")
    token = utils.get_token()

    print('token: ', token)

    function_one()


    


    end_process(timeStart)


def function_one():
    """Function one."""
    try:
        
        dsn_tns = cx_Oracle.makedsn('192.172.2.85', '1521', service_name='siganpub') 
        conn = cx_Oracle.connect(user=r'edicion', password='edicion', dsn=dsn_tns)

        c = conn.cursor()
        c.execute('select * from EDICION.TACAREA')
        for row in c:
            print (row[0], '-', row[1], '-', row[2])
        conn.close()

    except:
        print("Failed function_one (%s)" %
              traceback.format_exc())
        utils.error_log("Failed function_one (%s)" %
                        traceback.format_exc())


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
