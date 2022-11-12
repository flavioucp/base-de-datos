import pandas as pd
import csv

df_alum  = pd.read_csv('Alumnos.csv', sep=",") 

gender_alum = pd.DataFrame(df_alum.gender.unique(), columns= ['gender'])
gender_alum

df_prof  = pd.read_csv('Profesores.csv', sep=",") 
gender_prof = pd.DataFrame(df_prof.gender.unique(), columns=['gender'])
gender_prof

tb_gender = pd.concat([gender_alum, gender_prof])
tb_gender.duplicated()

tb_gender = tb_gender.drop_duplicates()
tb_gender

gender2= tb_gender.to_dict('records')
gender2