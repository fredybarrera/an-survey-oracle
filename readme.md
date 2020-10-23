# Script integracion Survey123 - Oracle

Proyecto desarrollado en Python 3.8.0

## Propósito

Script que permite la lectura de encuestas de survey123 desde Arcgis Online y escribe los datos en una base de datos Oracle.

## Instalación

Descargar el proyecto y descomprimir en una ubicación dentro del disco C:

Se recomienda la instalación dentro de un entorno virtual de [miniconda](https://docs.conda.io/en/latest/miniconda.html).

Instalar miniconda en el sistema operativo y crear un entorno virtual con Python x.x:
```bash
conda create -n nombre_entorno python==3.8.0
```
Activar al entorno virtual:
```bash
activate nombre_entorno 
```
Navegar hasta la ubicación del proyecto e instalar las dependencias:

```bash
pip install -r requirements.txt
```

Crear un archivo **.env** en la raiz del proyecto, tomando como referencia el archivo **.env_example** y completar los valores correspondientes para las variables:
```bash
VARIABLE=""
```

## Uso

Ejecutar el archivo **main.py**
```bash
cd C:\Miniconda3\envs\nombre_entorno\
python.exe C:\Users\user_1\script\main.py
```
