# ENG : The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + . . . + 10^2 = 385. 
#The square of the sum of the first ten natural numbers is, ( 1 + 2 + . . . + 10 ) 2 = 55 2 = 3025. 
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640 . 
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# TR : İlk on doğal sayının karelerinin toplamı 1^2 + 2^2 +. . . + 10^2 = 385. 
#İlk on doğal sayının toplamının karesi, ( 1 + 2 + . . . + 10 ) 2 = 55^2 = 3025'tir. 
#Dolayısıyla ilk on doğal sayının kareleri toplamı arasındaki fark doğal sayılar ve toplamın karesi 3025 − 385 = 2640'tır. 
#İlk yüz doğal sayının kareleri toplamı ile toplamın karesi arasındaki farkı bulun.

#karelerinin toplamı
sum_of_squares = 0

#toplamının karesi
squared_of_sum = 0

sum = 0

for i in range(1, 101):
    sum += i
    squared_of_sum += i * i 

result = (sum * sum) - squared_of_sum

print(result)

