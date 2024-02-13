# ENG: If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3 , 5 , 6 and 9 . 
#The sum of these multiples is 23 . Find the sum of all the multiples of 3 or 5 below 1000 .

# TR:10'un altındaki 3 veya 5'in katı olan tüm doğal sayıları sıralarsak 3, 5, 6 ve 9'u elde ederiz.
#Bu katların toplamı 23'tür. 1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.

sum = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i
print(sum)
