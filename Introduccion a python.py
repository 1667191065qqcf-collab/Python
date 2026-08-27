my_int_variable=5
my_string_variable="Hola"
print (my_int_variable)

my_int_variable=str(my_int_variable) 
print(my_int_variable)
print(type(my_int_variable))

#convirte un variable entero a un string, simplemente.

print(type(print(my_int_variable)))

# imprimir que tipo es la funcion "print", pero no tiene clase

print(len(my_string_variable))

#len, imprime la longitud de tu variable, en este caso 1 y 4.

#Creacion de variable en una sola linea

name, surname, alias, age = "Ziwang", "chen", "Muxin",25

print("Me llamo:", name, surname, ", Mi edad es:",age, "y mi alias es:", alias)

                        ###Sistema de inputs###
"""

first_name=input("Cual es tu nombre:")

edad=input("Cuantos años tienes:")

print(first_name)

print(edad) 

"""

                        ###Operadores###
print(10 % 2) #Operador de moduloLo que nos devuelve es el resto de la division
print(2**3) 
print(10//3) #Hace una division quita los decimales, dejando solamente la parte entera
print("Hola"*2)
#print("Hola" * 2.5) #Error

print(3>4) ###Comparador###
print(3<4)
print(3<=4)
print(3!=4)

print("aaaa">= "bbbb") 
print(len ("aaaa") >= len ("bbbb"))

print(3>4)

                            ###strings###

new_strings="Esta es una nueva string con salto de linea \n esto es un salto de linea"
print(new_strings)


                            ###formateo###

name, surname,age= "Ziwang", "Chen", 25

print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print ("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

#Los tres casos funciona lo mismo, pero el ultimo caso es mucho mas tedioso.

print(f"Mi nombre es {name} {surname} y mi edad es {age}") #f-string, es la forma mas facil de formatear strings

#Reverse

language="python"
reverse_string=language[::-1] #Esto es un slice, que nos permite invertir el string
print(reverse_string)

                        ###Funciones##

print(language.capitalize()) #Capitaliza la primera letra del string
print(language.upper()) #Convierte todo el string a mayusculas
print(language.count("t")) #Cuenta cuantas veces aparece un caracter en el string
print(language.isnumeric()) #Devuelve True si el string es un numero, False si no
print("1".isnumeric()) #Devuelve True si el string es un numero, False si no
print(language.lower()) #Convierte todo el string a minusculas
print(language.lower().isupper()) #Devuelve True si el string esta en mayusculas, False si no

                        ###Listas###

my_list=[35,24,62,52,12,45,78,96,100]
print(my_list)
print(len(my_list)) #Devuelve la longitud de la lista

my_other_list=["Ziwang", "Chen", 25, 1.75, True]
print(my_other_list)
print(type(my_other_list)) #Devuelve el tipo de la variable, en este caso es una lista

print(my_other_list[0]) #Devuelve el primer elemento de la lista
print(my_other_list[-1]) #Devuelve el ultimo elemento de la lista
print(my_other_list[-3])
print(my_list.count(100)) #Cuenta cuantas veces aparece un elemento en la lista

name, surname, age, height, bolean= my_other_list 
print(height) #Devuelve el valor de la variable height, que es 1.75

print(my_list + my_other_list) #Concatena dos listas

#Añadir elementos a una lista
my_other_list.append("Nueva entrada")
print(my_other_list)

my_other_list.insert(1, "Segunda entrada") #Inserta un elemento en la posicion 1
print(my_other_list)

my_other_list.remove("Segunda entrada") #Elimina un elemento de la lista
print(my_other_list)

print(my_other_list.pop()) #Elimina el ultimo elemento de la lista y lo devuelve
print(my_other_list)

my_other_list[1]="Nuevo valor" #Cambia el valor de un elemento de la lista
print(my_other_list)


                        ###Tuplas###

my_tuple=tuple()
my_tuple=(35,24,62,52,12,45,78,96,100)

print(my_tuple[-1])
print(type(my_tuple)) #Devuelve el tipo de la variable, en este caso es una tupla

print(my_tuple.count(100)) #Cuenta cuantas veces aparece un elemento en la tupla

print(my_tuple.index(100)) #Devuelve el indice de un elemento en la tupla

# my_tuple[1]=33 #Error, no se puede cambiar el valor de un elemento de una tupla, ya que es inmutable
print(my_tuple) #Devuelve la tupla completa

my_tuple=list(my_tuple) #Convierte la tupla en una lista
print(type(my_tuple)) #Devuelve el tipo de la variable, en este caso es una lista
my_tuple[1]=33 #Cambia el valor de un elemento de la lista
print(my_tuple) #Devuelve la lista completa


#Comparacion rapida entre tuplas y listas.

my_prueba=(55,55,44,23,43)

print(type(my_prueba)) #Devuelve el tipo de la variable, en este caso es una 

my_prueba_lista=[22,34,53,21,22,4]

print(type(my_prueba_lista)) #Devuelve el tipo de la variable, en este caso es una lista

                        ###Sets### 
#No tiene orden, no acepta repetidos, no puede acceder mediante indice.

my_set=set()

my_other_set={} #Aqui interpreta como un diccionario.
my_other_set_2={"Ziwang", "Chen", 25, 0, True} #Esto es un set
my_other_set_3={"Chen", "C2", 22, 3, True, "hola"} #Esto es un set, pero no acepta repetidosh


print(type(my_other_set))
print(type(my_other_set_2))

print(len(my_other_set_2)) #Devuelve la longitud del set

#print(my_other_set_2[0]) #Error, no se puede acceder a un elemento de un set por su indice, ya que no tiene orden

my_other_set_2.add("Nueva entrada") #Añade un elemento al set
print(my_other_set_2) #Un set no tiene un orden. Su forma de guardar los elementos es desordenada.

my_other_set_2.add("Nueva entrada")
print(my_other_set_2)  #Un set no puede tener elementos repetidos, por lo que no se añade el elemento "Nueva entrada" dos veces.

print("Ziwang" in my_other_set_2) #Devuelve True si el elemento esta en el set, False si no
print("Hello" not in my_other_set_2) #Devuelve True si el elemento no esta en el set, False si esta

my_other_set_2.remove("Ziwang") #Elimina un elemento del set
print(my_other_set_2)

my_new_set=my_other_set_2.union(my_other_set_3) #Une dos sets, pero no acepta repetidos
print(my_new_set)

print(my_other_set_2.difference(my_other_set_3)) #Devuelve un set con los elementos que no estan en el otro set

print(my_other_set_2.intersection(my_other_set_3)) #Devuelve un set con los elementos que estan en ambos sets

                        ###Diccionarios### 
# Son una estructura de datos que nos permite almacenar pares de clave-valor.


my_dict=dict()
my_other_dict= {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict= {
    "Nombre":"Ziwang",
    "Apellido": "Chen",
    "Edad":25,
    "Idioma":{"Chino", "español", "ingles"},
    1:14122212202,
    } #Dato asociado a un valor

print(my_other_dict)

print(len(my_other_dict))

my_other_dict["Nombre"]="Aiden"
print(my_other_dict["Nombre"])

my_other_dict["Calle"]="Manuela malasaña"
print(my_other_dict) 

del my_other_dict["Calle"]
print(my_other_dict)

#Podemos añadir,eliminar, modificar los contenidos que hay en un diccionario

print("Ziwang" in my_other_dict)
print("Nombre" in my_other_dict)

my_new_other_dic=dict.fromkeys(my_other_dict)
print(my_new_other_dic) #Copiar un diccionario vacio conservando sus claves

print(list(my_other_dict)) #Solo devuelve la clave sin el valor.
print(list(my_other_dict.values())) #Solo devuelve el valor 
print(set(my_other_dict))

                        ###Condicionales###

my_condicion=False

if my_condicion: #Como convencion la condicion se cumple cuando es un TRUE

    print("Se ejecuta mi condicion")

print("La ejecucion se continua")

my_condicion_2 = 5 *2

if my_condicion_2 >= 10:

    print("Se ejecuta la segunda condicion")

my_condicion_3= 2*5

if my_condicion_3 >= 10 and my_condicion_3 <= 15:

    print("Mi numero esta dentro del 10 y 15")

elif my_condicion_3==5:

    print("Aun que no esta en el rango, " \
    "pero cuando sea 5 necesita una accion especial")

else:

    print("No esta dentro del rango entre 10 y 15")

##Condicionales con string

my_string= "" 
if my_string: #Lo interpreta como un false

    print("Imprime esto si mi cadena de texto no esta vacia")

my_string_2="Holis"

if my_string_2:

    print("Imprime esto si mi cadena de texto 2 no esta vacia")

my_string_3= "Hola mundo"

if my_string_3 == "Hola mundo":

    print("La cadena de texto coincide")


                        ### Bucles / Loops / ciclos ###

#while

my_condition=0

while my_condition < 10:
    print(my_condition, "Aun cumple la condicion")
    my_condition+=2

    if my_condition == 4:
        print("Mi condicion ahora es 4")
        break #Indicamos cuando es 4 sale del bucle, aunque sigue 
              #siendo menor que la condicion impuesta.  
else:
    print("Mi condicion ya se ha superado")

#No se acepta elif

#For, nos sirve para iterar un listado de elementos

my_list=[11,22,32,14,32,45,64]

my_other_dict= {
    "Nombre":"Ziwang",
    "Apellido": "Chen",
    "Edad":25,
    "Idioma":{"Chino", "español", "ingles"},
    1:14122212202,
    } #Dato asociado a un valor

my_other_set_2={"Ziwang", "Chen", 25, 0, True} #Esto es un set

for element in my_list:
    print(element)
else:
    print("Se ha acabado el bucle for")

for element in my_other_dict:
    print(element)
    
    if element == "Idioma":
        print("Se ha encontrado el key de idioma")
        break #Acaba el bucle directamen, sin imprimir el codigo de else
        #continue : este ejecuta el contenido del if, continua y acaba el bucle.
else:
    print("Se ha acabado la ejecucion")


                        ### Funciones ###

def my_own_function ():
        
    print("Este es mi propia funcion")

my_own_function()


def suma_de_dos_valores (first_numb, second_numb):
    
     print(first_numb+second_numb)

suma_de_dos_valores("2","3")
suma_de_dos_valores(2,3)

#Aqui no fuerza el tipo de input.


def suma_de_dos_valores_con_retorno (first_numb, second_numb):
    
     my_sum= first_numb + second_numb
     
     return my_sum
 
my_result = suma_de_dos_valores_con_retorno(10, 5) #guardo el resultado en un variable

print(my_result)

def print_name (name, surname):
    
    print(f"{name} {surname}") #La f sirve para formartear al string y para acceder a los valore

print_name("Ziwang", "Chen")
print_name(surname="Ziwang", name="Chen") #cambio el orden.

def print_name_por_defecto(name, surname,sex ="no necesario"):
    
    print(f"{name} {surname} {sex}")
    
print_name_por_defecto("Aiden","Chen", "Masculino")
print_name_por_defecto("Aiden", "Chen")

def print_texto(*text):
    for texts in text:
     print(texts.lower())

print_texto("Hola", "lila") #con * podemos pasar infinitos textos
print_texto("lol", "biba")

                        ### Clases ###

class MyProfile: #Como buena practica la clase se define con mayusculas y sin guiones bajos.
    #self es obligatorio
    def __init__(self, name, surname): #Esta linea da posibilidad a Myprofile a recibir parametros
        #pass #Se deja el pass cuando no se hace nada 
        self.name=name
        self.surnam=surname
        self.full_name= f"{name} {surname}"
    
    def walk (self):
        print(f"{self.full_name} esta caminando")
        
mi_perfil =MyProfile("Ziwang", "Chen")    
  
print(mi_perfil.name)
print(mi_perfil.full_name)
mi_perfil.walk()

MyProfile.full_name = "Aiden" #Cambiar los datos de mi clase
print(MyProfile.full_name)

                        ###Excepciones### 
#manejo de errores try -> except -> else -> finally

numero_1=4
numero_2=9
numero_3="10"

try:
    print(numero_1 + numero_2)

except: 

    print("Se ha producido un error")

else: #Solo se ejecuta si el codigo dentro del try se ejecuto correctamente
    print("La ejecucion continua")

finally: #Se ejecuta siempre
    print("LA EJECUCION CONTINUA")

#else y finally son opcionales, pero un try siempre lleva un except

#Excepciones por tipo

try:
    print(numero_1 + numero_3)

except ValueError:
    print("Se producido un value error")

except TypeError: 
    print("Se ha producido un type error")

#Captura de la informacion de la excepcion


try:
    print(numero_1 + numero_3)

except ValueError as captura_error:

    print(captura_error)

#Capturamos donde esta el error y lo guardamos

except Exception as exception_error:

    print(exception_error)

#La idea es que no se pete nuestro app cuando produce un error como casos anteriores, la cual no podemos ignorar.
#Sino que el programa siga funcionando saltando a bloque de except

                        ### Modulos ###
#Se trata de llamar funciones creado en otros ficheros.

import Fichero_modulo

Fichero_modulo.suma_de_valores(3, 4, 1)

Fichero_modulo.printvalue("Hola mundo")

#Son dos forma de utilizar la llamada de funciones

from Fichero_modulo import suma_de_valores, printvalue

suma_de_valores(3, 5, 1)

printvalue("Hello word")

#Modulos propios del python
import math

print(math.pi)
print(math.cos(0))

from math import pi as renombra_pi #podemos renombrarla.

print(renombra_pi)

