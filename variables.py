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

# Sistema de inputs
"""

first_name=input("Cual es tu nombre:")

edad=input("Cuantos años tienes:")

print(first_name)

print(edad) 

"""

#Operadores
print(10 % 2) #Operador de moduloLo que nos devuelve es el resto de la division
print(2**3) 
print(10//3) #Hace una division quita los decimales, dejando solamente la parte entera
print("Hola"*2)
#print("Hola" * 2.5) #Error

print(3>4) #Comparador
print(3<4)
print(3<=4)
print(3!=4)

print("aaaa">= "bbbb") 
print(len ("aaaa") >= len ("bbbb"))





