

num = 0
while num <= 100: 
    
    
    num += 1

    if num %3 ==0  and num % 5 == 0:
        
      print("fizzbuzz")
      
    elif num % 5 == 0:
        
      print("buzz")
      
    elif num % 3 == 0:
        
      print("fizz")

    else:
    
        print(num)
        

