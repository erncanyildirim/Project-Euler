# We shall say that an 𝑛 -digit number is pandigital if it makes use of all the digits 1 to 𝑛 exactly once; 
# for example, the 5 -digit number, 15234 , is 1 through 5 pandigital. 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254 , containing multiplicand, multiplier, and product is 1 through 9 pandigital. 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital. 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# TR : 𝑛 -basamaklı bir sayı, 1'den 𝑛'ye kadar tüm rakamları tam olarak bir kez kullanıyorsa pandigital olduğunu söyleyeceğiz; 
# örneğin, 5 basamaklı sayı olan 15234 1'den 5'e kadar tam dijitaldir. 
# 7254 çarpımı olağandışıdır, çünkü özdeşlik 39 × 186 = 7254 , çarpanı, çarpanı içerir ve çarpım 1'den 9'a kadar pandigitaldir. 
# Çarpan/çarpan/ürün kimliği 1'den 9'a kadar pandigital olarak yazılabilen tüm çarpımların toplamını bulun. 
# İPUCU: Bazı ürünler birden fazla yolla elde edilebildiğinden, bunları toplamınıza yalnızca bir kez dahil ettiğinizden emin olun.


import itertools
import time

start = time.time()

permutations = itertools.permutations(range(1,10), 9)

result = set()

for i in permutations:
    number1 = i[0] * 10 + i[1]
    number2 = i[2] * 100 + i[3] * 10 + i[4]
    number3 = i[5] * 1000 + i[6] * 100 + i[7] * 10 + i[8]
    if number1 * number2 == number3:
        result.add(number3)

    number1 = i[0] 
    number2 = i[1] * 1000 + i[2] * 100 + i[3] * 10 + i[4]
    number3 = i[5] * 1000 + i[6] * 100 + i[7] * 10 + i[8]
    if number1 * number2 == number3:
        result.add(number3)
finish = time.time()

print(sum(result))
print(finish - start)
