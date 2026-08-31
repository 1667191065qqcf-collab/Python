import pandas as pd 

#Dataset con csv 
datos= pd.read_csv("data.csv")

#print(datos)

print(datos["LanguagesWorkedWith"][9]) #busqueda de datos

print(datos["Responder_id"] < 10) #control del rango 

filtrar = datos["Responder_id"] < 10

datos_filtrar = datos[filtrar] #llamo a datos con la restriccion de filtrar

print(datos_filtrar)

print(datos.tail(5))  #ultimas x filas de nuestro archivo


