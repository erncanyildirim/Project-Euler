# ENG : A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28 , which means that 28 is a perfect number. 
# A number 𝑛 is called deficient if the sum of its proper divisors is less than 𝑛 and it is called abundant if this sum exceeds 𝑛 . 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16 , the smallest number that can be written as the sum of two abundant numbers is 24 . 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit. 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# TR : Mükemmel sayı, uygun bölenlerinin toplamı sayıya tam olarak eşit olan bir sayıdır. 
# Örneğin 28'in tam bölenlerinin toplamı 1 + 2 + 4 + 7 + 14 = 28 olur, bu da 28'in mükemmel bir sayı olduğu anlamına gelir. 
# Bir 𝑛 sayısına, uygun bölenlerinin toplamı 𝑛'den küçükse eksik, bu toplam 𝑛'den büyükse bol sayı denir. 
# 12 en küçük bol sayı olduğundan 1 + 2 + 3 + 4 + 6 = 16 olduğundan iki bol sayının toplamı şeklinde yazılabilecek en küçük sayı 24'tür. 
# Matematiksel analizle 28123'ten büyük tüm tam sayıların iki bol sayının toplamı olarak yazılabildiği gösterilebilir.
# Ancak iki bol sayının toplamı olarak ifade edilemeyen en büyük sayının bu sınırdan küçük olduğu bilinse de bu üst sınır analizle daha fazla düşürülemez. 
# Çok sayıda iki sayının toplamı olarak yazılamayan tüm pozitif tam sayıların toplamını bulun.


import math

def divisor_sum(x):
    sum =1
    n = 2
    while (n < math.ceil(math.sqrt(x))):
        if x % n == 0:
            sum += n
            sum += x // n
        n += 1
        if n * n == x:
            sum += n
    return sum

def control(x):
    if divisor_sum(x) > x:
        return True
    else:
        return False

abundant = list()
sum = 0

sum_of_abundant = list()

for i in range(1, 28124):
    if control(i):
        abundant.append(i)

sum_of_abundant = [0] * 28124

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] <= 28123:
            sum_of_abundant[abundant[i] + abundant[j]] = abundant[i] + abundant[j]
print(sum_of_abundant)

for i in range(len(sum_of_abundant)):
    if sum_of_abundant[i] == 0:
        sum += i

print(sum)