import pandas as pd
import csv

# Importamos los datos de cursos_profesores
cur_prof  = pd.read_csv('cursos_profesores.csv', sep=",") 

# Quitamos duplicados y seleccionamos la columna "branch"
df_branch = pd.DataFrame(cur_prof.branch.unique(), columns= ['branch'])
print(df_branch.count())
df_branch

#Lo transformo en diccionario
branch= df_branch.to_dict('records')
branch