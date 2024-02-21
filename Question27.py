# ENG : Euler discovered the remarkable quadratic formula: 
# 𝑛 2 + 𝑛 + 41 
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ 𝑛 ≤ 39 . 
# However, when 𝑛 = 40 , 40 2 + 40 + 41 = 40 ( 40 + 1 ) + 41 is divisible by 41 , and certainly when 𝑛 = 41 , 41 2 + 41 + 41 is clearly divisible by 41 . 
# The incredible formula 𝑛 2 − 79 𝑛 + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ 𝑛 ≤ 79 . 
# The product of the coefficients, − 79 and 1601 , is − 126479 . 
# Considering quadratics of the form: 
# 𝑛 2 + 𝑎 𝑛 + 𝑏 , where | 𝑎 | < 1000 and | 𝑏 | ≤ 1000 
# where | 𝑛 | is the modulus/absolute value of 𝑛 
# e.g. | 11 | = 11 and | − 4 | = 4 Find the product of the coefficients, 𝑎 and 𝑏 , 
# for the quadratic expression that produces the maximum number of primes for consecutive values of 𝑛 , starting with 𝑛 = 0 .
    
# TR : Euler dikkat çekici ikinci dereceden formülü keşfetti: 
# 𝑛 2 + 𝑛 + 41 Formülün ardışık 0 ≤ 𝑛 ≤ 39 tamsayı değerleri için 40 asal sayı üreteceği ortaya çıktı. 
# Ancak 𝑛 = 40 olduğunda, 40 2 + 40 + 41 = 40 ( 40 + 1 ) + 41 41'e bölünebilir ve 𝑛 = 41 olduğunda 41 2 + 41 + 41 kesinlikle 41'e açıkça bölünebilir. 
# Ardışık 0 ≤ 𝑛 ≤ 79 değerleri için 80 asal sayı üreten inanılmaz formül 𝑛 2 − 79 𝑛 + 1601 keşfedildi. 
# − 79 ve 1601 katsayılarının çarpımı − 126479'dur. 
# Formun ikinci dereceden ifadeleri dikkate alındığında: 
# 𝑛 2 + 𝑎 𝑛 + 𝑏 , burada | 𝑎 | < 1000 ve | 𝑏 | ≤ 1000 
# burada | 𝑛 | 𝑛'nin modülü/mutlak değeridir; 
# | 11 | = 11 ve | − 4 | = 4 𝑛 = 0'dan başlayarak ardışık 𝑛 değerleri için maksimum asal sayı sayısını üreten ikinci dereceden ifade için 𝑎 ve 𝑏 katsayılarının çarpımınıbulun.


import sympy

prime_count = 0

for a in range(-1000, 1000):
    for b in sympy.primerange(1, 1000):
        aux_prime_count = 0
        n = 0
        while sympy.isprime(n ** 2 + a * n + b):
            aux_prime_count += 1
            n += 1
        if aux_prime_count > prime_count:
            prime_count = aux_prime_count
            amax = a
            bmax = b
print(amax * bmax)
print(prime_count)