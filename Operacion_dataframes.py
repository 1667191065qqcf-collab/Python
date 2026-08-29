import pandas as pd 

df=pd.read_csv("data.csv")

print(df)

#Acceso a elementos mediante nombres
print(df.loc[2,"LanguagesWorkedWith"]) 

#Modificar nuestro archivo

df["Nueva fila"]= pd.Series(["Prueba1", "Prueba2", "Prueba3"])

print(df)

#Nuevo_fila=df.pop("Nueva fila") #Eliminar columnas

df.to_csv("data.csv", index=False)

print(df)

