# ENG : Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits: 
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 
# 8208 = 8^4 + 2^4 + 0^4 + 8^4 
# 9474 = 9^4 + 4^4 + 7^4 + 4^4 
# As 1 = 1^4 is not a sum it is not included. 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316 . Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# TR : Şaşırtıcı bir şekilde, rakamların dördüncü kuvvetlerinin toplamı olarak yazılabilen yalnızca üç sayı vardır: 
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 
# 8208 = 8^4 + 2^4 + 0^4 + 8^4 
# 9474 = 9^4 + 4^4 + 7^4 + 4^4 
# 1 = 1^4 bir toplam olmadığından dahil edilmemiştir. 
# Bu sayıların toplamı 1634 + 8208 + 9474 = 19316'dır. Rakamlarının beşinci kuvvetlerinin toplamı olarak yazılabilen tüm sayıların toplamını bulun.


number = 2

numbers = []

while number < 1000000:
    temp = number
    sum = 0
    while temp != 0:
        sum += (temp % 10) ** 5
        temp //= 10
    if sum == number:
        numbers.append(number)
    number += 1

print(sum(numbers))