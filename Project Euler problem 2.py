#Project Euler Problem 2
#Fibonacci Sequence

i = 0
j = 1
n = 0
result = 0

while (n < 4000000):
    if n % 2 == 0:
        result = result + n
    
    i = j
    j = n
    n = i + j
    
print(result)
    
    
    
    
