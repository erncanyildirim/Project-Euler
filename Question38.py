# ENG : Take the number 192 and multiply it by each of 1 , 2 , and 3 : 
# 192 × 1 = 192 
# 192 × 2 = 384 
# 192 × 3 = 576 
# By concatenating each product we get the 1 to 9 pandigital, 192384576 . 
# We will call 192384576 the concatenated product of 192 and ( 1 , 2 , 3 ) . 
# The same can be achieved by starting with 9 and multiplying by 1 , 2 , 3 , 4 , and 5 , giving the pandigital, 918273645 , 
# which is the concatenated product of 9 and ( 1 , 2 , 3 , 4 , 5 ) .
# What is the largest 1 to 9 pandigital 9 -digit number that can be formed as the concatenated product of an integer with ( 1 , 2 , … , 𝑛 ) where 𝑛 > 1 ?

# TR : 192 sayısını alın ve 1, 2 ve 3'ün her biriyle çarpın: 
# 192 × 1 = 192 
# 192 × 2 = 384 
# 192 × 3 = 576 
# Her çarpımı birleştirerek 1'den 9'a kadar pandigital, 192384576 elde ederiz. 
# 192384576'ya 192 ile (1, 2, 3)'ün birleştirilmiş çarpımını diyeceğiz. 
# Aynı şey, 9 ile başlayıp 1, 2, 3, 4 ve 5 ile çarpılarak 9 ve (1, 2, 3, 4, 5)'in birleştirilmiş ürünü olan pandigital 918273645'i vererek elde edilebilir. 
# (1, 2,…, 𝑛) ile bir tam sayının birleştirilmiş çarpımı olarak oluşturulabilecek 1'den 9'a kadar 9 basamaklı en büyük tam sayı nedir, burada 𝑛 > 1 olur mu?


myset = set("123456789")

pandigitals = []

for i in range(1, 10000):
    step = 1
    strnumber = ""
    while True:
        number = i * step
        strnumber += str(number)
        if len(strnumber) >= 9:
            if len(strnumber) > 9:
                break
            else:
                if set(strnumber) == myset:
                    pandigitals.append(int(strnumber))
                    break
        step += 1

print(max(pandigitals))