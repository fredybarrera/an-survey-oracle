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
