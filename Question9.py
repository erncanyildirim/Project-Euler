# ENG : A Pythagorean triplet is a set of three natural numbers, 𝑎 < 𝑏 < 𝑐 , for which, 𝑎^2 + 𝑏^2 = 𝑐^2 . 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 . There exists exactly one Pythagorean triplet for which 𝑎 + 𝑏 + 𝑐 = 1000 . 
# Find the product 𝑎 𝑏 𝑐 .

# TR : Bir Pisagor üçlüsü, 𝑎 < 𝑏 < 𝑐 olmak üzere üç doğal sayıdan oluşan bir kümedir, bunun için 𝑎^2 + 𝑏^2 = 𝑐^2 . 
# Örneğin, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 . 𝑎 + 𝑏 + 𝑐 = 1000 olan tam olarak bir Pisagor üçlüsü vardır. 
# Ürünü bulun 𝑎 𝑏 𝑐 .

done = False

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 -a -b
        if c*c == a*a + b*b:
            print(a * b * c)
            done = True
            break
    if done:
        break
    


