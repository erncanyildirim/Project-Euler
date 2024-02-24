# ENG : The decimal number, 585 = 1001001001 2 (binary), is palindromic in both bases. 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2 . 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# TR : Ondalık sayı, 585 = 1001001001 2 (ikili), her iki tabanda da palindromiktir. 
# 10 tabanında ve 2 tabanında palindromik olan, bir milyonun altındaki tüm sayıların toplamını bulun. 
# (Her iki tabandaki palindromik sayının baştaki sıfırları içermeyebileceğini lütfen unutmayın.)


def binary(x):
    remainders = []
    while x != 0 :
        remainder = x % 2
        remainders.append(str(remainder))
        x //= 2
    
    result = "".join(remainders)[::-1]
    return result

number = 1
sum = 0

while number < 1000000:
    if str(number) == str(number)[::-1] and binary(number) == binary(number)[::-1]:
        sum += number
    number += 1

print(sum)



