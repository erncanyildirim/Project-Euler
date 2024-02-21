# ENG : Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows: 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101 . 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# TR : 1 rakamından başlayıp saat yönünde sağa doğru ilerleyerek 5'e 5'lik bir spiral şu ​​şekilde oluşturulur: 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# Köşegenlerdeki sayıların toplamının 101 olduğu doğrulanabilir. 
# Aynı şekilde oluşturulmuş 1001'e 1001'lik bir spiralin köşegenlerindeki sayıların toplamı nedir?


matrix = []

for i in range(0, 1001):
    matrix.append([0] * 1001)

direction = "right"
i = 500
j = 500
matrix[i][j] = 1
number = 2

while number < 1001 * 1001:
    while direction == "right" and j < 1000:
        matrix[i][j + 1] = number
        number += 1
        j += 1
        if matrix[i + 1][j] == 0:
            direction = "down"
            break

    while direction == "down":
        matrix[i + 1][j] = number
        number += 1
        i += 1
        if matrix[i][j - 1] == 0:
            direction = "left"
            break
    
    while direction == "left":
        matrix[i][j - 1] = number
        number += 1
        j -= 1
        if matrix[i - 1][j] == 0:
            direction = "up"
            break

    while direction == "up":
        matrix[i - 1][j] = number
        number += 1
        i -= 1
        if matrix[i][j + 1] == 0:
            direction = "right"
            break

for row in matrix:
    print(row)

sum = 0

for i in range(1001):
    sum += matrix[i][i]
    sum += matrix[1000- i][i]

print(sum - matrix[500][500])
