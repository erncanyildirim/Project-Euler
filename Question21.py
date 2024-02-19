# ENG : Let 𝑑 ( 𝑛 ) be defined as the sum of proper divisors of 𝑛 (numbers less than 𝑛 which divide evenly into 𝑛 ). 
# If 𝑑 ( 𝑎 ) = 𝑏 and 𝑑 ( 𝑏 ) = 𝑎 , where 𝑎 ≠ 𝑏 , then 𝑎 and 𝑏 are an amicable pair and each of 𝑎 and 𝑏 are called amicable numbers. 
# For example, the proper divisors of 220 are 1 , 2 , 4 , 5 , 10 , 11 , 20 , 22 , 44 , 55 and 110 ; therefore 𝑑 ( 220 ) = 284 . 
# The proper divisors of 284 are 1 , 2 , 4 , 71 and 142 ; so 𝑑 ( 284 ) = 220 . 
# Evaluate the sum of all the amicable numbers under 10000 .

# TR : 𝑑 ( 𝑛 ), 𝑛'nin uygun bölenlerinin toplamı olarak tanımlansın (𝑛'ye eşit olarak bölünen 𝑛'den küçük sayılar). 
# Eğer 𝑑 ( 𝑎 ) = 𝑏 ve 𝑑 ( 𝑏 ) = 𝑎 , burada 𝑎 ≠ 𝑏 ise, o zaman 𝑎 ve 𝑏 dost bir çifttir ve 𝑎 ve 𝑏'nin her birine dost sayılar denir. 
# Örneğin, 220'nin tam bölenleri 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 ve 110'dur; dolayısıyla 𝑑 ( 220 ) = 284 . 
# 284'ün tam bölenleri 1, 2, 4, 71 ve 142'dir; yani 𝑑 ( 284 ) = 220 . 
# 10000'in altındaki tüm dost sayıların toplamını değerlendirin.


def d(x):
    div_list = list()
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            div_list.append(i)
    return sum(div_list)

amicables = list()

for i in range(1, 10001):
    if d(d(i)) == i and i != d(i):
        amicables.append(i)

print(sum(amicables))
    
