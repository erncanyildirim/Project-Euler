# ENG: The prime factors of 13195 are 5 , 7 , 13 and 29 . What is the largest prime factor of the number 600851475143 ?

# TR: 13195'in asal çarpanları 5, 7, 13 ve 29'dur. 600851475143 sayısının en büyük asal çarpanı nedir?

import math

def Prime_check(x):
    is_prime = True

    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            is_prime = False
            continue
    return is_prime

number = 600851475143

biggest_prime = 1

for i in range(2, int(math.sqrt(number) + 1)):
    if (number % i == 0) and (Prime_check(i)):
        biggest_prime = i

print(biggest_prime)


