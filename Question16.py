# ENG : 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26 . What is the sum of the digits of the number 2^1000 ?

# TR : 2^15 = 32768 ve rakamlarının toplamı 3 + 2 + 7 + 6 + 8 = 26'dır. 2^1000 sayısının rakamlarının toplamı kaçtır?

number = 2 ** 1000

sum = 0

for i in str(number):
    sum += int(i)
print(sum)
