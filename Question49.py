# ENG : The arithmetic sequence, 1487 , 4817 , 8147 , in which each of the terms increases by 3330 , is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4 -digit numbers are permutations of one another. 
# There are no arithmetic sequences made up of three 1 -, 2 -, or 3 -digit primes, exhibiting this property, 
# but there is one other 4 -digit increasing sequence. What 12 -digit number do you form by concatenating the three terms in this sequence?

# TR : Terimlerin her birinin 3330 arttığı 1487, 4817, 8147 aritmetik dizisi iki açıdan olağandışıdır: 
# (i) üç terimin her biri asaldır ve (ii) 4 basamaklı sayıların her biri birbirinin permütasyonları. 
# Bu özelliği sergileyen, 1-, 2- veya 3 basamaklı üç asal sayıdan oluşan aritmetik dizi yoktur, ancak 4 basamaklı artan bir dizi daha vardır. 
# Bu dizideki üç terimi birleştirerek hangi 12 basamaklı sayıyı oluşturursunuz?


from sympy import primerange
import time

start = time.time()

primes = list(primerange(1488, 10001))

def nums_to_dict(x):
    dict_ = dict()
    for i in str(x):
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    return dict_

def same_digits(x, y, z):
    if nums_to_dict(x) == nums_to_dict(y) and nums_to_dict(x) == nums_to_dict(z):
        return True
    return False

ok = False

for i in range(len(primes)):
    if ok: break
    for j in range(i + 1, len(primes)):
        prime1 = primes[i]
        prime2 = primes[j]
        prime3 = 2 * prime2 - prime1
        if prime3 in primes:
            if same_digits(prime1, prime2, prime3):
                print(prime1, prime2, prime3)
                ok = True
                break

finish = time.time()
print(finish - start)