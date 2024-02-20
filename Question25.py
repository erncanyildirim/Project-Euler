# ENG : The Fibonacci sequence is defined by the recurrence relation: 
# 𝐹 𝑛 = 𝐹 𝑛 − 1 + 𝐹 𝑛 − 2 , where 𝐹 1 = 1 and 𝐹 2 = 1 . 
# Hence the first 12 terms will be:
# 𝐹 1 = 1 
# 𝐹 2 = 1 
# 𝐹 3 = 2 
# 𝐹 4 = 3 
# 𝐹 5 = 5 
# 𝐹 6 = 8 
# 𝐹 7 = 13 
# 𝐹 8 = 21 
# 𝐹 9 = 34 
# 𝐹 10 = 55 
# 𝐹 11 = 89 
# 𝐹 12 = 144 
# The 12 th term, 𝐹 12 , is the first term to contain three digits. 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# TR : Fibonacci dizisi yineleme ilişkisiyle tanımlanır: 
# 𝐹 𝑛 = 𝐹 𝑛 − 1 + 𝐹 𝑛 − 2 , burada 𝐹 1 = 1 ve 𝐹 2 = 1 . 
# Dolayısıyla ilk 12 terim şöyle olacaktır: 
# 𝐹 1 = 1 
# 𝐹 2 = 1 
# 𝐹 3 = 2 
# 𝐹 4 = 3 
# 𝐹 5 = 5 
# 𝐹 6 = 8 
# 𝐹 7 = 13 
# 𝐹 8 = 21 
# 𝐹 9 = 34 
# 𝐹 10 = 55 
# 𝐹 11 = 89 
# 𝐹 12 = 144 12. terim olan 𝐹 12, üç rakam içeren ilk terimdir. 
# Fibonacci dizisindeki 1000 basamaklı ilk terimin indeksi nedir?


a = 1
b = 1

step = 2

while True:
    a, b = b, a + b
    step += 1
    if(len(str(b))) == 1000:
        print(step)
        break