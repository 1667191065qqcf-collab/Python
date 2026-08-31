from matplotlib import pyplot as plt
import numpy as np
#Es literalmente lo que hacemos en matlab pero en python

#print(plt.style.available)
plt.style.use("Solarize_Light2")

"""
valor_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

x_indexes= np.arange(len(valor_x))
widht=0.25
      
valor_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

plt.bar(x_indexes-widht, valor_y,width=widht, label="Todos los desarrolladores")

valor_y_2 = [45372, 23232, 34564, 94873, 18276, 35456, 17827, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

plt.bar(x_indexes, valor_y_2,width=widht, label ="Python")

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]


plt.bar(x_indexes+widht, js_dev_y,width=widht, label ="javascript")

plt.title("Salario medio")
plt.xlabel("Años")
plt.ylabel("Salario")

plt.legend()
#plt.legend(["todos los desarrolladores","Python"]) otra forma de implementar la leyenda

plt.grid(True)
plt.tight_layout()

plt.savefig("plot.png")

plt.xticks(ticks=x_indexes, labels=valor_x) #Etiquetas

plt.show()

#formato de linea -> al manual

"""

#lectura de archivo csv con el modulo estandar

"""
import csv


with open("data.csv") as csv_file:
    
    csv_reader = csv.DictReader(csv_file)
    row=next(csv_reader)
    print(row["LanguagesWorkedWith"].split(";"))

#Contador de datos

from collections import Counter


with open("data.csv") as csv_file:
    
    csv_reader = csv.DictReader(csv_file)
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

language=[]
popularity=[]
#print(language_counter.most_common(3))

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])
    
language.reverse()
popularity.reverse()

plt.barh(language, popularity)

plt.title("Most popular language")

plt.xlabel("Number of people who use")

plt.show()
"""
#Lectura de archivo csv con panda

import pandas as pd 
from collections import Counter

data=pd.read_csv("data.csv")
ids=data["Responder_id"]
lang_response=data["LanguagesWorkedWith"] #Carga el archivo y lo guarda en dos columnas

language_counter=Counter() #Aqui aun no esta contando nada


for response in lang_response:
        language_counter.update(response.split(";"))
         
        #print(response) veria tal cual como se ve en el archivo csv

#print(response) #lo que se ve es el valor que toma response en ultima vuelta del bucle


language=[]
popularity=[]

for item in language_counter.most_common(5): #aqui CUENTA las 5 mas populares, es decir ya se cuantas veces aparece cada lenguaje y lo guardo en item.
    language.append(item[0]) #El leguaje lo guardo con el indice 0 
    popularity.append(item[1])
    
    #print(item) #Aqui muestra los 5 mas populares y las veces que aparece en el archivo.



print(language)
print(popularity)

#imprimo el lenguaje y la popularidad por separado

language.reverse()
popularity.reverse()

plt.barh(language, popularity)

plt.title("Most popular language")

plt.xlabel("Number of people who use")

plt.show()

