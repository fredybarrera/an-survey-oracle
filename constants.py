
#-------------------------------------------------------------------------------
# Name:         constants
# Purpose:      Constantes del script
#
# Author:       Fredys Barrera Artiaga <fbarrera@esri.cl>
# Created:      22-10-2020
# Copyright:    (c) fbarrera 2020
# Licence:      <your licence>
#-------------------------------------------------------------------------------

from decouple import config

# **********************************************************************************************
# Workspace
WORKSPACE = config('FOLDER_WORKSPACE')

# **********************************************************************************************
# Credenciales para obtener token
USERNAME = config('TOKEN_USERNAME')
PASSWORD = config('TOKEN_PASSWORD')
REFERER = config('TOKEN_REFERER')
URL = config('TOKEN_URL')

# **********************************************************************************************
# Tabla encuestas
URL_REST_FALLA_MATRICES = config('URL_ENCUESTA_FALLA_MATRICES')
TABLE_FALLA_MATRIZ = config('TABLE_FALLA_MATRIZ')
TABLE_ESTANQUES = config('TABLE_ESTANQUES')
TABLE_VALVULAS_BUENAS = config('TABLE_VALVULAS_BUENAS')
TABLE_VALVULAS_MALAS = config('TABLE_VALVULAS_MALAS')
TABLE_CORTE = config('TABLE_CORTE')

URL_QUERY_FALLA_MATRIZ = URL_REST_FALLA_MATRICES + '/' + TABLE_FALLA_MATRIZ + '/query'
URL_QUERY_ESTANQUES = URL_REST_FALLA_MATRICES + '/' + TABLE_ESTANQUES + '/query'
URL_QUERY_VALVULAS_BUENAS = URL_REST_FALLA_MATRICES + '/' + TABLE_VALVULAS_BUENAS + '/query'
URL_QUERY_VALVULAS_MALAS = URL_REST_FALLA_MATRICES + '/' + TABLE_VALVULAS_MALAS + '/query'
URL_QUERY_CORTE = URL_REST_FALLA_MATRICES + '/' + TABLE_CORTE + '/query'

# URL_ATTACHMENT_CAMBIOS = URL_REST_FALLA_MATRICES + '/0/queryAttachments'
# URL_ATTACHMENT_VISITAS = URL_REST_FALLA_MATRICES + '/1/queryAttachments'

# **********************************************************************************************
# Conexion Oracle
LOCATION = config('ORACLE_LOCATION')
SERVER_IP = config('ORACLE_SERVER_IP')
SERVER_PORT = config('ORACLE_SERVER_PORT')
SERVER_SERVICE = config('ORACLE_SERVER_SERVICE')
SERVER_USERNAME = config('ORACLE_SERVER_USERNAME')
SERVER_PASSWORD = config('ORACLE_SERVER_PASSWORD')

# **********************************************************************************************