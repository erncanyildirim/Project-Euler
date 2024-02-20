# ENG : A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are: 
# 012 021 102 120 201 210 What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# TR : Permütasyon nesnelerin sıralı bir düzenlemesidir. Örneğin 3124, 1, 2, 3 ve 4 rakamlarının olası bir permütasyonudur. 
# Tüm permütasyonların sayısal veya alfabetik olarak listelenmesine sözlükbilimsel sıra diyoruz. 
# 0, 1 ve 2'nin sözlükbilimsel permütasyonları şunlardır: 
# 012 021 102 120 201 210 0, 1, 2, 3, 4, 5, 6, 7, 8 ve 9 rakamlarının milyonuncu sözlüksel permütasyonu nedir?


from itertools import permutations

digits = "0123456789"

numbers = list(permutations(digits))

result = numbers[999999]
#print(result)

result2 = "".join(result)
print(result2)