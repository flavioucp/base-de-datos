import pandas as pd
import csv

prof  = pd.read_csv('Profesores.csv', sep=",") 
df_prof = pd.DataFrame(prof)
df_prof

df_prof['personal_id'] = df_prof['personal_id'].str.replace('.','')
print(df_prof.dtypes)

# Convierto personal_id a entero
df_prof['personal_id'] = df_prof['personal_id'].astype('int64')
print(df_prof.dtypes)

#Convierto columna datebirth a formato fecha
df_prof['birthdate'] = pd.to_datetime(df_prof['birthdate'], yearfirst= True)
print(df_prof.dtypes)
df_prof

# Elimino registros duplicados: toda la fila, en el campo personal id y mail.
df_prof.duplicated()
df_prof.drop_duplicates('personal_id')
df_prof.drop_duplicates('email')
df_prof.count()

df_prof2 = df_prof.iloc[0:,1:8]
df_prof2 = df_prof2[['first_name', 'last_name','email','birthdate', 'personal_id']]
df_prof2

#Lo transformo en diccionario
prof2= df_prof2.to_dict('records')
prof2

#hola