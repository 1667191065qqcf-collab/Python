            ###Date###
            
#import datetime  #Creacion de fechas

#now = datetime.datetime 

from datetime import datetime

now=datetime.now()#now es un variable que guarda el resultado del objeto datetime

print(now)
print(now.day, "/",now.month, "/", now.year)
print(now.hour,":" ,now.minute,":", now.second)

timestamp= now.timestamp()

print(timestamp)


def print_date(date): 
    
    print(now.day, "/",now.month, "/", now.year)
    print(now.hour,":" ,now.minute,":", now.second)
    
print_date(now)

#Crear una nueva fecha 

year_2027=datetime(2027, 1, 1)

print(year_2027)

from datetime import time 

current_time=time(16, 7 , 31) #hay que pasar los valores a time()

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#solo entiende parametros de tiempo

from datetime import date

current_date=date(2026, 8  , 9) #hay que pasar los valores a time()

print(current_date.year)
print(current_date.month)
print(current_date.day) 

#solo entiende parametros de fechas

from datetime import timedelta

init_timedelta =timedelta(200, 100, 100, weeks=10)
end_timedelta=timedelta(200, 100, weeks=11)

print(end_timedelta - init_timedelta)
print(end_timedelta+init_timedelta)

                ###List Comprehension###

my_original_list=[0,1,2,3,4,5,6,7,8]
print(my_original_list)

#Estamos haciendo lo mismo pero imagina que necesitamos llegar a numero 3000
#No vas a poner numeros a mano desde 0 hasta 3000 -> range

my_list = [i for i in range(8)] 
print(my_list)


my_list = [i+1 for i in range(8)] #Se guarda en i
print(my_list)

my_list = [i*i for i in range(8)] 
print(my_list)

my_range= range(8)
print(list(my_range))

def sum_five(number):
    
    return number +5 

my_list=[sum_five(i) for i in range (8)]
print(my_list)