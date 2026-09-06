
#Como defino para que sea divisible entre 1 e i mismo que no haya otro numero mas 


for i in range(2,100): 
    
    es_primo=True
    
    for j in range(2 , i): #no hay la situacion de i=2 y j=2 
                           #Por que en range(2,2) no imprime nada
        
        if i % j == 0: #Para un numero de i tenemos una lista de j que comprobar
            
            es_primo = False
            break 
        
    if es_primo == True: # se ejecuta solo cuando es true 
        
        print(i, "es primo")
        
#(nada en i=2)
#2         ← en i=3
#2 3       ← en i=4
#2 3 4     ← en i=5