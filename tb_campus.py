import pandas as pd
import csv

# Importamos los datos de cursos profesores
cur_prof  = pd.read_csv('cursos_profesores.csv', sep=",") 

# Quitamos registros duplicados y seleccionamos la columna "campus"
df_campus = pd.DataFrame(cur_prof.campus.unique(), columns= ['campus'])
print(df_campus.count())
df_campus

# Convertimos a diccionario
campus= df_campus.to_dict('records')
campus