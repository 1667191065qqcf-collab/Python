number_1=0
print("0:",number_1)
number_2=1
print("1:",number_2)

for i in range(48): 

   number_3= number_1 + number_2 # 1 2 3 
   
   print(f"{i+2}:",number_3) # 1 2 3 
   
   number_1 = number_2 # 1 1 2
   number_2=number_3  # 1 2 3 
   
   #2,3->5
   #3,5->8
   #5,8->13
   
   
  
   
 