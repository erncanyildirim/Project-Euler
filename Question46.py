# ENG : It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square. 
# 9 = 7 + 2 × 1^2 
# 15 = 7 + 2 × 2^2 
# 21 = 3 + 2 × 3^2 
# 25 = 7 + 2 × 3^2 
# 27 = 19 + 2 × 2^2 
# 33 = 31 + 2 × 1^2 
# It turns out that the conjecture was false. 
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# TR : Christian Goldbach her tek bileşik sayının bir asal sayı ile iki katının karesinin toplamı olarak yazılabileceğini öne sürdü. 
# 9 = 7 + 2 × 1^2 
# 15 = 7 + 2 × 2^2 
# 21 = 3 + 2 × 3^2 
# 25 = 7 + 2 × 3^2 
# 27 = 19 + 2 × 2^2 
# 33 = 31 + 2 × 1^2 
# Döner varsayımın yanlış olduğu ortaya çıktı. 
# Bir asal sayı ile iki katın karesinin toplamı olarak yazılamayan en küçük tek bileşik nedir?


from sympy import isprime

number = 9

while True:
    if isprime(number) or number % 2 == 0:
        number += 1
        continue
    writable = False
    n = 1
    while number - 2 * n * n > 0:
        if isprime(number - 2 * n * n):
            writable  =True
            break
        n += 1

    if not writable:
        print(number)
        break
    number += 1
    