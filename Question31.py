# ENG : In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation: 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p). 
# It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p 
# How many different ways can £2 be made using any number of coins?

# TR : Birleşik Krallık'ta para birimi pound (£) ve peni (p)'den oluşur. Genel dolaşımda sekiz madeni para vardır: 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) ve £2 (200p). 
# Şu şekilde 2 £ kazanmak mümkündür: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p 
# Herhangi bir sayıda madeni para kullanılarak 2 £ kaç farklı şekilde kazanılabilir? ?

def count_ways_to_make_pounds():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]

print(count_ways_to_make_pounds())

