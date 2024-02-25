# ENG : We shall say that an 𝑛 -digit number is pandigital if it makes use of all the digits 1 to 𝑛 exactly once. 
# For example, 2143 is a 4 -digit pandigital and is also prime. What is the largest 𝑛 -digit pandigital prime that exists?

# TR : 𝑛 -basamaklı bir sayı, 1'den 𝑛'ye kadar olan tüm rakamları tam olarak bir kez kullanıyorsa pandigital olduğunu söyleyeceğiz. 
# Örneğin 2143 4 basamaklı bir pandigitaldir ve aynı zamanda asaldır. Var olan en büyük 𝑛 -basamaklı pandijital asal sayı nedir?


import itertools
import sympy

number = "1234567"

numbers = list(itertools.permutations(number))

numbers.sort(reverse=True)

for i in numbers:
    i = "".join(i)
    if sympy.isprime(int(i)):
        print(i)
        break

