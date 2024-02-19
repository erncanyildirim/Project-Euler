# ENG : 𝑛 ! means 𝑛 × ( 𝑛 − 1 ) × ⋯ × 3 × 2 × 1 . 
# For example, 10 ! = 10 × 9 × ⋯ × 3 × 2 × 1 = 3628800 , 
# and the sum of the digits in the number 10 ! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 . 
# Find the sum of the digits in the number 100 ! .

# TR : 𝑛 ! = 𝑛 × ( 𝑛 − 1 ) × ⋯ × 3 × 2 × 1 anlamına gelir. 
# Örneğin 10 ! = 10 × 9 × ⋯ × 3 × 2 × 1 = 3628800 
# ve 10 sayısının rakamlarının toplamı ! 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27'dir. 
# 100 sayısının rakamlarının toplamını bulun! .

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    print(fact)

    str_fact = str(fact)
    sum = 0
    
    for i in str_fact:
        sum += int(i)
    print(sum)

factorial(100)

