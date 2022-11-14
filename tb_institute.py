import pandas as pd
import csv

# Importamos los datos de "Cursos_profesores"
cur_prof  = pd.read_csv('cursos_profesores.csv', sep=",") 

#Convertimos a dataframe, conservamos registros únicos y seleccionamos la columna "institute"
df_institute = pd.DataFrame(cur_prof.institute.unique(), columns= ['institute'])
print(df_institute.count())
df_institute

# Convertimos en diccionario
institute= df_institute.to_dict('records')
institute