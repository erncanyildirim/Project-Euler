# ENG : The fraction 49 / 98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly 
# believe that 49 / 98 = 4 / 8 , which is correct, is obtained by cancelling the 9 s. 
# We shall consider fractions like, 30 / 50 = 3 / 5 , to be trivial examples. 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator. 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# TR : 49/98 kesri ilginç bir kesirdir, basitleştirmeye çalışan deneyimsiz bir matematikçi, 9'ların iptal edilmesiyle doğru olan
# 49/98 = 4/8'in elde edildiğine yanlış bir şekilde inanabilir. 
# 30/50 = 3/5 gibi kesirleri önemsiz örnekler olarak ele alacağız. 
# Bu kesir türünün önemsiz olmayan, değeri birden küçük, pay ve paydasında iki rakam bulunan tam olarak dört örneği vardır. 
# Bu dört kesrin çarpımı en düşük ortak terimlerle verilirse paydanın değerini bulun.
#pay=numerator      payda= denominator

import math

ans = []

result_numerator = 1
result_denominator = 1

for i in range(10, 100):
    for j in range(i + 1, 100):
        if i % 10 == 0:
            continue
        if j % 10 == 0:
            continue
        
        stri = str(i)
        strj = str(j)

        if stri[1] == strj[0]:
            if int(stri[0]) / int(strj[1]) == i / j:
                ans.append(str(i) + "/" + str(j))
                result_numerator *= i
                result_denominator *= j

        if stri[0] == strj[1]:
            if int(stri[1]) / int(strj[0]) == i / j:
                ans.append(str(i) + "/" + str(j))
                result_numerator *= i
                result_denominator *= j        

        if stri[1] == strj[1]:
            if int(stri[0]) / int(strj[0]) == i / j:
                ans.append(str(i) + "/" + str(j))
                result_numerator *= i
                result_denominator *= j

        if stri[0] == strj[0]:
            if int(stri[1]) / int(strj[1]) == i / j:
                ans.append(str(i) + "/" + str(j))
                result_numerator *= i
                result_denominator *= j

print(ans)
print(result_denominator // math.gcd(result_denominator, result_numerator))