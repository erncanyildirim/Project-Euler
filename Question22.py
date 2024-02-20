# ENG : Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score. 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53 , is the 938 th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714 . What is the total of all the name scores in the file?

# TR : Beş binin üzerinde ad içeren 46K'lık bir metin dosyası olan labels.txt'yi (sağ tıklayın ve 'Bağlantıyı/Hedefi Farklı Kaydet...') kullanarak, dosyayı alfabetik sıraya göre sıralayarak başlayın. 
# Daha sonra her ismin alfabetik değerini hesaplayın ve bir isim puanı elde etmek için bu değeri listedeki alfabetik konumuyla çarpın. 
# Örneğin liste alfabetik sıraya göre sıralandığında 3 + 15 + 12 + 9 + 14 = 53 değerindeki COLIN listede 938. sırada yer alıyor. 
# Yani COLIN 938 × 53 = 49714 puan alacaktır. Dosyadaki tüm ad puanlarının toplamı nedir?


#create random name file
'''
import random

def generate_names(num_names):
    names = []
    for _ in range(num_names):
        first_name = random.choice(["John", "Emma", "Michael", "Sophia", "Matthew", "Olivia", "Daniel", "Isabella", "David", "Ava"])
        last_name = random.choice(["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"])
        full_name = f"{first_name} {last_name}"
        names.append(full_name)
    return names

def write_to_file(names, filename):
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')

if __name__ == "__main__":
    num_names = 5000
    names = generate_names(num_names)
    filename = "D:/isimler.txt"  # The path to create the file
    write_to_file(names, filename)
    print(f"{num_names} isim {filename} dosyasına yazıldı.")
'''



import string

with open("D:/isimler.txt", "r") as f:
    names = f.read()

dict1 = dict()
alphabet = string.ascii_uppercase
letter_value = 1
for letter in alphabet:
    dict1 [letter] = letter_value
    letter_value += 1

list.sort(names)
index = 1
sum = 0

for name in names:
    sub_total = 0
    name = name[1: len(name) - 1]
    for letter in name:
        sub_total += dict1[letter]
    sum += sub_total * index
    index += 1

print(sum)