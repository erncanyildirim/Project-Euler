# ENG: A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2 -digit numbers is 9009 = 91 × 99 . 
#Find the largest palindrome made from the product of two 3 -digit numbers.

# TR: Palindromik bir sayı her iki şekilde de aynı şeyi okur. 
#2 basamaklı iki sayının çarpımından elde edilen en büyük palindrom 9009 = 91 × 99'dur. 
#3 basamaklı iki sayının çarpımından elde edilen en büyük palindromu bulun.


def check_palindrome(x):
    str_number = str(x)
    reverse_number = str_number[::-1]
    if str_number == reverse_number:
        return True
    else:
        return False
    

big_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if check_palindrome(i * j) and i * j > big_palindrome:
            a = i
            b = j
            big_palindrome = i * j

print(f'First number: {a}\nSecond number: {b}')
print(f'Result: {big_palindrome}')
    
