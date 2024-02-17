# ENG : The following iterative sequence is defined for the set of positive integers: 
# 𝑛 → 𝑛 / 2 ( 𝑛 is even) 
# 𝑛 → 3𝑛 + 1 ( 𝑛 is odd) 
# Using the rule above and starting with 13 , we generate the following sequence: 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1. 
# It can be seen that this sequence (starting at 13 and finishing at 1 ) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1 . 
# Which starting number, under one million, produces the longest chain? 
# NOTE: Once the chain starts the terms are allowed to go above one million.

# TR : Pozitif tam sayılar kümesi için aşağıdaki yinelemeli dizi tanımlanmıştır: 
# 𝑛 → 𝑛 / 2 ( 𝑛 çifttir) 
# 𝑛 → 3𝑛 + 1 ( 𝑛 tektir) 
# Yukarıdaki kuralı kullanarak ve 13 ile başlayarak aşağıdaki diziyi oluştururuz: 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1. 
# Bu dizinin (13'ten başlayıp 1'de biten) 10 terim içerdiği görülmektedir. 
# Henüz kanıtlanamasa da (Collatz Problemi) tüm başlangıç ​​sayılarının 1'de bittiği düşünülmektedir. 
# Bir milyonun altındaki hangi başlangıç ​​numarası en uzun zinciri oluşturur? 
# NOT: Zincir başladıktan sonra terimlerin bir milyonun üzerine çıkmasına izin verilir.

import time

past_numbers = dict()

def collatz(number, past_numbers):
    given = number
    steps = 1
    while number != 1:
        if number in past_numbers:
            steps += past_numbers[number] - 1
            break
        if number % 2 == 0:
            number //= 2
            steps +=1
        else:
            number = (3 * number + 1)
            steps += 1
    past_numbers[given] = steps
    return steps

wanted = 1
max = 1

start = time.time()
for i in range(1, 1000001):
    move_count = collatz(i, past_numbers)
    if move_count > max:
        max = move_count
        wanted = i
final = time.time()

print(str(final - start))
print(wanted)


