"""
palabra_1= {"AMOR"}
palabra_2= {"ROMA"}

if palabra_1.intersection (palabra_2):
    
    print ("Es un anagrama")

else:
    
    print ("No es un anagrama")    
    
No se utiliza intersection para este ejercicio por que no compara letra por letra
    
""" 
from collections import Counter
palabra_1= "CASO"
palabra_2= "SACO"

if Counter(palabra_1) == Counter(palabra_2):
    
    print("Es un anagrama")

else: 
    
    print("No es un anagrama")