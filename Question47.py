# ENG : The first two consecutive numbers to have two distinct prime factors are: 
# 14 = 2 × 7 
# 15 = 3 × 5. 
# The first three consecutive numbers to have three distinct prime factors are: 
# 644 = 2 2 × 7 × 23 
# 645 = 3 × 5 × 43 
# 646 = 2 × 17 × 19. Find the first four consecutive integers to have four distinct prime factors each. 
# What is the first of these numbers?

# TR : İki farklı asal çarpanı olan ilk iki ardışık sayı: 
# 14 = 2 × 7 
# 15 = 3 × 5. 
# Üç farklı asal çarpanı olan ilk üç ardışık sayı: 
# 644 = 2 2 × 7 × 23 
# 645 = 3 × 5 × 43 
# 646 = 2 × 17 × 19. Her biri dört farklı asal çarpana sahip ilk dört ardışık tam sayıyı bulun. 
# Bu sayıların ilki nedir?


def prime_factors_count(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)

def find_consecutive_integers_with_prime_factors(num_consecutive):
    count = 0
    n = 1
    while True:
        if all(prime_factors_count(n + i) == num_consecutive for i in range(num_consecutive)):
            return [n + i for i in range(num_consecutive)]
        n += 1

first_four_consecutive = find_consecutive_integers_with_prime_factors(4)
print("The first four consecutive integers to have four distinct prime factors each:", first_four_consecutive)
print("The first of these numbers:", first_four_consecutive[0])



