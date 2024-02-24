# ENG : If 𝑝 is the perimeter of a right angle triangle with integral length sides, { 𝑎 , 𝑏 , 𝑐 }
# there are exactly three solutions for 𝑝 = 120 . { 20 , 48 , 52 } , { 24 , 45 , 51 } , { 30 , 40 , 50 } 
# For which value of 𝑝 ≤ 1000 , is the number of solutions maximised?

# TR : Eğer 𝑝, kenarlarının tam uzunluğu { 𝑎 , 𝑏 , 𝑐 } olan dik açılı bir üçgenin çevresi ise
# 𝑝 = 120 için tam olarak üç çözüm vardır. { 20 , 48 , 52 } , { 24 , 45 , 51 } , { 30 , 40 , 50 } 
# Hangi 𝑝 ≤ 1000 değeri için çözüm sayısı maksimumdur?


import time 

start = time.time()
perimeters = dict()

for b in range(1 ,500):
    for c in range(500 - b):
        a = (b ** 2 + c ** 2) ** 0.5
        if a + b + c > 1000:
            break
        else:
            if a == int(a):
                perimeter = int(a) + b + c
                if perimeter in perimeters:
                    perimeters[perimeter] += 1
                else:
                    perimeters[perimeter] = 1

for k,v in perimeters.items():
    if v == max(perimeters.values()):
        print(k)

finish = time.time()

print(finish - start)

