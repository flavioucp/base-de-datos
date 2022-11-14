import pandas as pd
import csv

# Trae los datos de los alumnos y extraigo los referidos a la locación geográfica
df_alum  = pd.read_csv('Alumnos.csv', sep=",") 
geo_alum = df_alum[["country","city","town","state"]]
geo_alum

# Trae los datos de los profesores y extraigo los referidos a la ubicación geográfica
df_prof  = pd.read_csv('Profesores.csv', sep=",") 
geo_prof = df_prof[["country","city","town","state"]]
geo_prof

# Concatena los 2 dataframes de ubicación para obtener un solo listado exhaustivo de todas las localidades
geo = pd.concat([geo_alum, geo_prof])
geo

# Elimino registros duplicados 
localidades = geo.drop_duplicates()
localidades

### Ver si hay que separar en más tablas