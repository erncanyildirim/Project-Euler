# ENG : 145 is a curious number, as 1 ! + 4 ! + 5 ! = 1 + 24 + 120 = 145 . 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1 ! = 1 and 2 ! = 2 are not sums they are not included.

# TR : 145 ilginç bir sayıdır, tıpkı 1! + 4! + 5! = 1 + 24 + 120 = 145 . 
# Rakamlarının faktöriyellerinin toplamına eşit olan tüm sayıların toplamını bulun. 
# Not: 1 olarak! = 1 ve 2 ! = 2 toplam değildir, dahil edilmemiştir.


from math import factorial

upper_limit = factorial(9) * 7

sum = 0

for number in range(3, upper_limit):
    sub_total = 0
    temp = number

    while temp != 0:
        digit = temp % 10
        sub_total += factorial(digit)
        temp //= 10

    if sub_total == number:
        sum += number
        print(number)

print(sum)

