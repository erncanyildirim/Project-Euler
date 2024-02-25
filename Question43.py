# ENG : The number, 1406357289 , is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
# but it also has a rather interesting sub-string divisibility property. 
# Let 𝑑 1 be the 1 st digit, 𝑑 2 be the 2 nd digit, and so on. In this way, we note the following: 
# 𝑑 2 𝑑 3 𝑑 4 = 406 is divisible by 2 
# 𝑑 3 𝑑 4 𝑑 5 = 063 is divisible by 3 
# 𝑑 4 𝑑 5 𝑑 6 = 635 is divisible by 5 
# 𝑑 5 𝑑 6 𝑑 7 = 357 is divisible by 7
# 𝑑 6 𝑑 7 𝑑 8 = 572 is divisible by 11 
# 𝑑 7 𝑑 8 𝑑 9 = 728 is divisible by 13 
# 𝑑 8 𝑑 9 𝑑 10 = 289 is divisible by 17 
# Find the sum of all 0 to 9 pandigital numbers with this property.

# TR : 1406357289 sayısı, 0'dan 9'a kadar olan bir tam dijital sayıdır çünkü 0'dan 9'a kadar olan rakamların her birinden belirli bir sırayla oluşur, 
# ancak aynı zamanda oldukça ilginç bir alt dizi bölünebilirlik özelliğine de sahiptir. 
# 𝑑 1 1. rakam olsun, 𝑑 2 2. rakam olsun, vb. Bu şekilde şunu not ediyoruz: 
# 𝑑 2 𝑑 3 𝑑 4 = 406, 2'e bölünür
# 𝑑 3 𝑑 4 𝑑 5 = 063, 3'e bölünür
# 𝑑 4 𝑑 5 𝑑 6 = 635, 5'e bölünür
# 𝑑 5 𝑑 6 𝑑 7 = 357, 7'e bölünür
# 𝑑 6 𝑑 7 𝑑 8 = 572, 11'e bölünür
# 𝑑 7 𝑑 8 𝑑 9 = 728, 13'e bölünür
# 𝑑 8 𝑑 9 𝑑 10 = 289, 17'e bölünür
# Tüm 0'ların toplamını bulun için Bu özelliğe sahip 9 pandigital sayı.


from itertools import permutations


digit = "0123456789"
numbers = permutations(digit)

numberlist = ["".join(number) for number in numbers if not number[0] == "0"]

sum_ = 0
primes = [2, 3, 5, 7, 11, 13, 17]

for number in numberlist:
    is_okey = True
    for i in range(7):
        if int(number[i+1:i+4]) % primes[i] != 0:
            is_okey  =False
            break
    if is_okey:
        sum_ += int(number)

print(sum_)