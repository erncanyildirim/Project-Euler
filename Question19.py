# ENG : You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# TR : Size aşağıdaki bilgiler verilmiştir, ancak kendiniz için biraz araştırma yapmayı tercih edebilirsiniz.
# 1 Ocak 1900 Pazartesi idi.
# Otuz gün Eylül var,
# Nisan, Haziran ve Kasım
# Geri kalanların hepsinde otuz bir var,
# Yalnızca şubatı kurtarmak,
# Yirmi sekizi olan, yağmur ya da güneş
# Ve artık yıllarda, yirmi dokuz
# Artık yıl, 4'e eşit olarak bölünebilen herhangi bir yılda oluşur, ancak 400'e bölünemeyen bir yüzyılda olmaz.
# Yirminci yüzyılda (1 Ocak 1901'den 31 Aralık 2000'e kadar) ayın ilk günü kaç Pazar'a denk geliyordu?

from datetime import date

sundays = 0

for year in range(1901, 2001):
    for month in range(1,13):
        if date(year, month, 1).weekday() == 6:
            sundays += 1

print(sundays)