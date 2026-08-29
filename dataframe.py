import pandas as pd 
import numpy as np
#dataframe a partir de un diccionario
data= {"Nombre":["Felipe", "Helena", "Andres", "Pedro"], 
       "Carrera":["Ingeneria", "Fisica", "Matematicas", "Arte"],
       "Correro":["Fel@gmail.com", "He@gmail.com", "Ads@gmail.com", "Pdr@gmail.com"]}

estudiantes =pd.DataFrame(data) #Lee el contenido del diccionario y lo guarda 

#Dataframe a partir de una lista 

df=pd.DataFrame([["Felipe", 27],["Lucas", 22], ["David", 12],["Angel", 35]], columns=["Nombre", "Edad"])

print(df)

#Dataframe a partir de un array
data_2=pd.DataFrame(np.random.randn(4,2), columns=["a","b"]) #dimensionar filas y columnas

print(data_2)