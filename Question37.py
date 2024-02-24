# ENG : The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797 , 797 , 97 , and 7 . 
# Similarly we can work from right to left: 3797 , 379 , 37 , and 3 . 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left. 
# NOTE: 2 , 3 , 5 , and 7 are not considered to be truncatable primes.

# TR : 3797 sayısının ilginç bir özelliği var. 
# Kendisi asal olduğundan, rakamları soldan sağa sürekli olarak çıkarmak ve her aşamada asal kalmak mümkündür: 3797 , 797 , 97 ve 7 . 
# Benzer şekilde sağdan sola doğru da çalışabiliriz: 3797 , 379 , 37 ve 3 . 
# Hem soldan sağa hem de sağdan sola kesilebilen on bir asal sayının toplamını bulun. 
# NOT: 2, 3, 5 ve 7 kesilebilir asal sayılar olarak kabul edilmez.

import sympy


def truncatable_left(x):
    number = str(x)
    flag = True
    for i in range(len(number)):
        number2 = int(number[i::])
        if sympy.isprime(number2) == False:
            flag = False
    return flag

def truncatable_right(x):
    number = str(x)
    flag = True
    for i in range(len(number)):
        number2 = int(number[:i + 1:])
        if sympy.isprime(number2) == False:
            flag = False
    return flag

truncatable_count = 0
number_tried = 10
truncatable_number =  list()

while True:
    if sympy.isprime(number_tried) and truncatable_right(number_tried) and truncatable_left(number_tried):
        truncatable_number.append(number_tried)

    number_tried += 1

    if len(truncatable_number) == 11:
        break

print(sum(truncatable_number))