# ENG : The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17 . Find the sum of all the primes below two million.

# TR : 10'un altındaki asal sayıların toplamı 2 + 3 + 5 + 7 = 17'dir. İki milyonun altındaki tüm asal sayıların toplamını bulun.

import math

sum = 0

def check_prime(x):
    is_prime = True
    if x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                is_prime = False
                break
        return is_prime        

number = 2

while True:
    if check_prime(number):
        sum += number

    if number == 2000000:
        break
    number += 1

print(sum)

