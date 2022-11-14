import pandas as pd
import csv

# Importamos datos de alumnos. Conservamos registros únicos de la columna 'program'
df_alum  = pd.read_csv('Alumnos.csv', sep=",") 
prog_alum = pd.DataFrame(df_alum.program.unique(), columns= ['program'])
print(prog_alum.count())
prog_alum

#hacemos lo mismo con "cursos_profesores"
df_cur_prof  = pd.read_csv('cursos_profesores.csv', sep=",") 
prog_prof = pd.DataFrame(df_cur_prof.program.unique(), columns= ['program'])
print(prog_prof.count())
prog_prof

# Concatenamos ambos dataframes
df_program = pd.concat([prog_alum, prog_prof])
df_program.duplicated()

#Quitamos duplicados
df_program = df_program.drop_duplicates()
print(df_program.count())
df_program

# Convertimos a diccionario
program= df_program.to_dict('records')
program