# ENG : A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given: 
# 1 / 2 = 0.5 
# 1 / 3 = 0. ( 3 ) 
# 1 / 4 = 0.25 
# 1 / 5 = 0.2 
# 1 / 6 = 0.1 ( 6 ) 
# 1 / 7 = 0. ( 142857 ) 
# 1 / 8 = 0.125 
# 1 / 9 = 0. ( 1 ) 
# 1 / 10 = 0.1 
# Where 0.1 ( 6 ) means 0.166666 ⋯ , and has a 1 -digit recurring cycle. It can be seen that 1 / 7 has a 6 -digit recurring cycle. 
# Find the value of 𝑑 < 1000 for which 1 / 𝑑 contains the longest recurring cycle in its decimal fraction part.

# TR: Birim kesrin payında 1 bulunur. Paydaları 2'den 10'a kadar olan birim kesirlerin ondalık gösterimi verilmiştir: 
# 1 / 2 = 0.5 
# 1 / 3 = 0. ( 3 ) 
# 1 / 4 = 0.25 
# 1 / 5 = 0.2 
# 1 / 6 = 0.1 ( 6 ) 
# 1 / 7 = 0. ( 142857 ) 
# 1 / 8 = 0.125 
# 1 / 9 = 0. ( 1 ) 
# 1 / 10 = 0.1 Burada 0,1 ( 6 ), 0,166666 ⋯ anlamına gelir ve 1 basamaklı bir yinelenen döngüye sahiptir. 1/7'nin 6 basamaklı tekrar eden bir döngüye sahip olduğu görülmektedir. 
# 1 / 𝑑'nin ondalık kesir kısmında en uzun yinelenen döngüyü içerdiği 𝑑 < 1000 değerini bulun.

max_transfer = 0
dividing = 2
while dividing < 1000:
    divided = 1
    remainders = []

    while True:
        remainder = divided % dividing
        if remainder in remainders:
            first_index = remainders.index(remainder)
            last_index = len(remainders)
            if last_index - first_index > max_transfer:
                max_transfer = last_index - first_index
                searched_number = dividing
            break

        divided = 10 * remainder
        remainders.append(remainder)
    dividing += 1

print(max_transfer)
print(searched_number)