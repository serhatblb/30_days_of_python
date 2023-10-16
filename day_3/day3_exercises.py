from tkinter import PIESLICE

my_age = 27
my_height = 1.79
complex_number = 3 + 5j

print('\n', '########', '\n')

# 4
print('4. Ucgenin alanini hesaplama')
taban = int(input('Ucgenin taban uzunlugunu giriniz: '))
yukseklik = int(input('Ucgenin yuksekligini giriniz: '))
alan = int(taban * yukseklik / 2)
print('Ucgenin alani: ', alan)

# 5 Ucgenin cevresini hesaplama
print('Ucgenin kenarlarini giriniz')
kenar1 = int(input('a kenarinin uzunlugunu giriniz: '))
kenar2 = int(input('b kenarinin uzunlugunu giriniz: '))
kenar3 = int(input('c kenarinin uzunlugunu giriniz: '))
cevre = int(kenar1 + kenar2 + kenar3)
print('Ucgenin cevresi: ', cevre)

# 6 Dikdortgenin alanini ve cevresini hesaplama

print('Dikdortgenin kenarlarini giriniz')
uzunluk = int(input('Dikdortgenin uzunlugunu giriniz: '))
genislik = int(input('Dikdortgenin genisligini giriniz: '))
alan = int(uzunluk * genislik)
cevre = int(2 * (uzunluk + genislik))
print('Dikdortgenin alani: ', alan, 'Dikdortgenin cevresi: ', cevre)

#7 Dairenin alanini ve cevresini hesaplama

print('Dairenin yaricapini giriniz')
r = int(input('Dairenin yaricapini giriniz: '))
pi = 3.14
alan = pi * r ** 2
cevre = 2 * pi * r
print('Dairenin alani: ', alan, 'Dairenin cevresi: ', cevre)

# 12 python and dragon
print('12: ',not len('Python') == len('Dragon'))

# 13 'on' in python
print('13: ','on' in 'Python' and 'on' in 'Dragon')

# 14 jargon
print('14: ', 'jargon' in 'I hope this course is not full of jargon.')

# 15
print('15: ', 'on' not in 'Python' and 'on' not in 'Dragon')

# 16
print(str(float(len('Python'))))

# 17 cift sayi
sayi = int(input('Bir sayi giriniz: '))
if sayi == 0:
    print('sayi sifir ')
elif sayi % 2 == 0:
    print('Cift sayi')
else:
    print('Tek sayi')

# 18

# 19
print(type('10')==type(10))

# 20
print(('9.8') == 10.0)

# 21 saatlik ucret hesaplama

saat = int(input('Kac Saat Calistiniz: '))
ucret = int(input('Saatlik Ucretiniz Ne Kadar: '))
kazanc = saat * ucret
print('Kazanciniz: {} tl'.format(kazanc))

# 22 yıl saniye hesabı
years = int(input('Enter years:'))
saniye =years * 365 * 24 * 60 * 60 * 60
print(f'{saniye} yasadiniz.')

# 23
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
