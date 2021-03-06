#-------------------------------------------------------------------------------
# Name:         utils
# Purpose:      Utilidades varias
#
# Author:       Fredys Barrera Artiaga <fbarrera@esri.cl>
# Created:      22-10-2020
# Copyright:    (c) fbarrera 2020
# Licence:      <your licence>
#-------------------------------------------------------------------------------

from datetime import datetime
import constants as const
import urllib.request as ur
import requests
import traceback
import json
import os
import platform
import cx_Oracle

script_dir = os.path.dirname(__file__)

# Location oracle client
LOCATION = const.LOCATION
# Credenciales
server_ip = const.SERVER_IP
server_port = const.SERVER_PORT
server_service = const.SERVER_SERVICE
server_username = const.SERVER_USERNAME
server_password = const.SERVER_PASSWORD

#-------------------------------------------------------------------------------
# Retorna un token de acceso a los servicios
#-------------------------------------------------------------------------------
def get_token():
    try:
        url = const.URL + "?f=json&username=" + const.USERNAME + "&password=" + \
            const.PASSWORD + "&referer=" + const.REFERER
        response = requests.get(url)
        data = response.json()
        return data['token']
    except:
        print("Failed get_token (%s)" % traceback.format_exc())
        error_log("Failed get_token (%s)" % traceback.format_exc())

#-------------------------------------------------------------------------------
# Retorna los headers para los request
#-------------------------------------------------------------------------------
def get_headers():

    return {
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json",
        'cache-control': "no-cache",
        'postman-token': "11df29d1-17d3-c58c-565f-2ca4092ddf5f"
    }

#-------------------------------------------------------------------------------
# Retorna los params para un count
#-------------------------------------------------------------------------------
def get_params_count(token):
    return {
        'f': 'json',
        'token': token,
        'where': '1=1',
        'outFields': '*',
        'returnCountOnly': 'true'
    }

#-------------------------------------------------------------------------------
# Retorna los params para una query
#-------------------------------------------------------------------------------
def get_params_query(token, offset, record_count):
    return {
        'f': 'json',
        'token': token,
        'where': '1=1',
        'outFields': '*',
        'orderByFields': 'OBJECTID',
        'resultOffset': offset,
        'resultRecordCount': record_count,
        'returnGeometry': True
    }

#-------------------------------------------------------------------------------
# Retorna un objeto de conexión a Oracle
#-------------------------------------------------------------------------------
def get_conexion_oracle():
    try:
        # print("ARCH:", platform.architecture())
        # print("FILES AT LOCATION:")
        for name in os.listdir(LOCATION):
            # print(name)
            os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]
        dsn_tns = cx_Oracle.makedsn(server_ip, server_port, service_name=server_service) 
        conn = cx_Oracle.connect(user=server_username, password=server_password, dsn=dsn_tns)
        return conn
    except:
        print("Failed get_conexion_oracle (%s)" % traceback.format_exc())
        error_log("Failed get_conexion_oracle (%s)" % traceback.format_exc())

#-------------------------------------------------------------------------------
# Convert seconds into hours, minutes and seconds
#-------------------------------------------------------------------------------
def insert_data(conn, sql, data):
    """insert multiple rows"""

    try:

        with conn.cursor() as cursor:
            # execute the insert statement
            cursor.executemany(sql, data)
            # commit work
            conn.commit()

    except:
        print("Failed insert_data (%s)" % traceback.format_exc())
        error_log("insert_data send (%s)" % traceback.format_exc())

#-------------------------------------------------------------------------------
# Convert seconds into hours, minutes and seconds
#-------------------------------------------------------------------------------
def convert_seconds(seconds):
    """Convert seconds into hours, minutes and seconds."""
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

#-------------------------------------------------------------------------------
# Almacena un log de proceso
#-------------------------------------------------------------------------------
def log(text):
    """Registra un log de proceso. """
    try:
        log_file = os.path.join(script_dir, 'logs.txt')
        f = open(log_file, "a", encoding='utf-8')
        f.write(
            "{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text))
        f.close()
    except:
        print("Failed log (%s)" %
              traceback.format_exc())
        error_log("Failed send (%s)" %
                        traceback.format_exc())

#-------------------------------------------------------------------------------
# Almacena un log de error
#-------------------------------------------------------------------------------
def error_log(text):
    """Registra un log de error. """
    try:
        log_file = os.path.join(script_dir, 'error-logs.txt')
        f = open(log_file, "a")
        f.write(
            "{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text))
        f.write("---------------------------------------------------------------- \n")
        f.close()
    except:
        print("Failed error_log (%s)" %
              traceback.format_exc())
