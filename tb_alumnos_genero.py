import pandas as pd
import csv
import datetime
import numpy

# Importo el CSV que contiene los datos de alumnos
alum  = pd.read_csv('Alumnos.csv', sep=",") 
df_alum_gender = pd.DataFrame(alum)
df_alum_gender

# Reemplazo el punto por nada en el campo personal_id y lo convierto en entero
df_alum_gender['personal_id'] = df_alum_gender['personal_id'].str.replace('.','')
df_alum_gender['personal_id'] = df_alum_gender['personal_id'].astype('int64')
print(df_alum_gender.dtypes)

df_alum_gender.drop_duplicates('personal_id')
df_alum_gender.count()

df_alum_gender2 = df_alum_gender[['personal_id','gender']]
df_alum_gender2

alumnos_genero= df_alum_gender2.to_numpy().tolist()
alumnos_genero