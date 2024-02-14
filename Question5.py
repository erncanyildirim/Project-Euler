# ENG : 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

# TR : 2520, 1'den 10'a kadar olan sayılara kalansız bölünebilen en küçük sayıdır. 
#1'den 20'ye kadar tüm sayılara tam olarak bölünebilen en küçük pozitif sayı nedir?

import math
import functools

#EBOB FunctionProblem
def gcd(x, y):              
    return math.gcd(x, y)

#EKOK Function
def lcm(x, y):
    return (x * y) // gcd(x, y)

liste = range(1, 21)

result = functools.reduce(lcm, liste)

print(result)



    
    


