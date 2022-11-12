
import csv


# Importo el CSV que contiene los datos de alumnos
alum  = open("Alumnos.csv")
alum = csv.DictReader(alum, delimiter= ',')
lista_alumno = list(alum)
print(lista_alumno)

