# ENG : The prime 41 , can be written as the sum of six consecutive primes: 
# 41 = 2 + 3 + 5 + 7 + 11 + 13. 
# This is the longest sum of consecutive primes that adds to a prime below one-hundred. 
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953 . 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# TR : Asal 41, ardışık altı asal sayının toplamı olarak yazılabilir: 
# 41 = 2 + 3 + 5 + 7 + 11 + 13. 
# Bu, yüzün altındaki bir asal sayıya eklenen ardışık asal sayıların en uzun toplamıdır. 
# Bir asal sayıya eklenen binin altındaki ardışık asal sayıların en uzun toplamı 21 terim içerir ve 953'e eşittir. 
# Bir milyonun altındaki hangi asal sayı ardışık en çok asal sayının toplamı 


import sympy

i = 1
primes = []

while True:
    if sympy.isprime(i):
        if sum(primes) + i > 1000000:
            break
        primes.append(i)
    
    i += 1

max_ = 0
sum = 0

for i in range(len(primes)):
    for j in range(i, len(primes) + 1):
        if sympy.isprime(sum(primes[i : j])):
            if j - i > max_:
                max_ = j - i
                sum = sum(primes[i : j])

print(max_)
print(sum)