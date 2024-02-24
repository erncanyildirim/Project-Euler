# ENG : An irrational decimal fraction is created by concatenating the positive integers: 
# 0.123456789101112131415161718192021⋯ 
# It can be seen that the 12 th digit of the fractional part is 1 . 
# If 𝑑 𝑛 represents the 𝑛 th digit of the fractional part, find the value of the following expression.

# TR : Pozitif tam sayıların birleştirilmesiyle irrasyonel bir ondalık kesir oluşturulur: 
# 0.123456789101112131415161718192021⋯ 
# Kesirli kısmın 12. basamağının 1 olduğu görülmektedir. 
# Eğer 𝑑 𝑛 kesirli kısmın 𝑛'inci basamağını temsil ediyorsa aşağıdaki ifadenin değerini bulun.


number = "0."
additive = 1

while len(number) < 1000002:
    number += str(additive)
    additive += 1

product = 1
for i in range(7):
    product *= int(number[10 ** i + 1])

print(product)