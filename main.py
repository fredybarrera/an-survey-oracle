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

import arcinfo
import arcpy
import utils
import constants as const
import requests
import xml.etree.ElementTree as et
import urllib.request as ur
import traceback
import os
import time
import json
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from datetime import datetime, timedelta

# Workspace
arcpy.env.workspace = const.WORKSPACE
# Sobreescribo la misma capa de salida
arcpy.env.overwriteOutput = True
# Set the preserveGlobalIds environment to True
arcpy.env.preserveGlobalIds = True
# Ruta absoluta del script
script_dir = os.path.dirname(__file__)

# Tablas
dataset = const.DATASET
falla_matriz = const.TABLE_FALLA_MATRIZ
falla_matriz_att = const.TABLE_FALLA_MATRIZ_ATT




def main():
    """Main function."""

    try:
        timeStart = time.time()
        utils.log("Proceso iniciado..." + str(datetime.now()))


        gis = GIS("https://www.arcgis.com", "Survey_ESRICHILE", "Aguas2020")

        print('gis: ', gis)
        print("Logged in as: " + gis.properties.user.username)

        encuestas = gis.content.get('c67f67653e274e33a7841d6b6a24567c')
        print('encuestas: ', encuestas)

        feature_layer = FeatureLayer("https://services7.arcgis.com/U3HcuJWWcwbEqVCd/arcgis/rest/services/service_4a5216c4b49c46e88b445be421ce3881/FeatureServer/0")

        query = feature_layer.query()

        if len(query.features) > 0:
            for feature in query.features:
                geometry = feature.geometry
                attributes = feature.attributes
                # print('attributes.objectid: ', attributes['objectid'])
                # attachments = feature_layer.attachments.get_list(oid=attributes['objectid'])
                # print('attachments: ', attachments)
                # print('len attachments: ', len(attachments))

        
        # featureclasses = arcpy.ListFeatureClasses()

        # for fc in featureclasses:
        #     print('fc: ', fc)



        # exit()






        for lyr in encuestas.layers:
            print('lyr.url: ', lyr.url)
            feature_layer = FeatureLayer(lyr.url)
            print('FeatureLayer: ', feature_layer)

            # for f in feature_layer.properties.fields:
                # print(f['name'])

            # query = feature_layer.query()
            # print('len: ', len(query.features))

            # if len(query.features) > 0:
            #     for feature in query.features:
            #         geometry = feature.geometry
            #         attributes = feature.attributes
            #         print('feature', feature)
            #         print('geometry: ', geometry)
            #         print('attributes: ', attributes)

        


        fc = os.path.join(arcpy.env.workspace, dataset, falla_matriz_att)
        print('fc: ', fc)

        field_names = [f.name for f in arcpy.ListFields(fc)]
        print('field_names: ', field_names)


        with arcpy.da.SearchCursor(fc, ["*"]) as cursor:
            for row in cursor:
                print('row: ', row)

        end_process(timeStart)

    except:
        print("Failed main (%s)" % traceback.format_exc())
        utils.error_log("Failed main (%s)" % traceback.format_exc())


def process(token, conn):
    """Inicio del proceso de obtención de la data y la carga en Oracle."""

    try:
        
        return True

    except:
        print("Failed process (%s)" % traceback.format_exc())
        utils.error_log("Failed process (%s)" % traceback.format_exc())


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
