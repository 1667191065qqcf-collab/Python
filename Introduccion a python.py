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

###Sets### No tiene orden, no acepta repetidos, no puede acceder mediante indice.

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




