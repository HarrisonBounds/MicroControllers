#Project Euler Problem 1
result = 0

#for i in range(3, 100000000):
#   if i % 3 == 0 or i % 5 == 0:
#      result = result + i
            
#print(result)

i = 0
while(i < 10000000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
        
    i = i + 1
    
print(result)