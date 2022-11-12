import pandas as pd
import csv
import datetime

# Importo el CSV que contiene los datos de alumnos
alum  = pd.read_csv('Alumnos.csv', sep=",") 
df_alum = pd.DataFrame(alum)
df_alum

# Reemplazo los puntos por nada en el campo "personal_id"
df_alum['personal_id'] = df_alum['personal_id'].str.replace('.','')
print(df_alum.dtypes)

# Convierto personal_id a entero
df_alum['personal_id'] = df_alum['personal_id'].astype('int64')
print(df_alum.dtypes)

#Convierto columna datebirth a formato fecha
df_alum['birthdate'] = pd.to_datetime(df_alum['birthdate'], yearfirst= True)
print(df_alum.dtypes)
df_alum

df_alum.duplicated()
df_alum.drop_duplicates('personal_id')
df_alum.drop_duplicates('email')
df_alum.count()

# Tomo una muestra de 20 registros para probar
df_alum2 = df_alum.iloc[1:, 0:8] #con iloc selecciono una parte del DF. En este caso, una muestra de 10 filas de las col 1 a 8
df_alum2 = df_alum2[['first_name', 'last_name','email','birthdate', 'personal_id']]
df_alum2

#Lo transformo en diccionario
alum2= df_alum2.to_dict('records')
alum2

