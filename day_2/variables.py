# Python Degiskenler
from math import radians

print( 'Day 2: 30 Days of python programming')

first_name = "Serhat"
last_name = "Bulbul"
country = "Turkey"
city = "Istanbul"
age = 27
is_married = False
skills = ["Python", "C++", "HTML", "CSS"]
person_info = {'first_name':'Serhat', 'last_name':'Bulbul', 'country':'Turkey', 'city':'Istanbul'}

# degiskenlerin yazdirilmasi

print('First_name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person info:', person_info)

# tek satırda birden fazla degiskenin yazdirilmasi

first_name, last_name, country, city, age, is_married = "Serhat", "Bulbul", "Turkey", "Istanbul", 27, False

print(first_name, last_name, country, city, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)

print('\n')
print('######## Exercises: Level 2 ##########')

print(type(first_name))
print(len(last_name))

num_one = 5
num_two = 4
toplam = num_one + num_two
print(toplam)
fark = num_one - num_two
print(fark)
carpma = num_one * num_two
print(carpma)
bolme = num_one / num_two
print(bolme)

print('\n')

# 5.The radius of a circle is 30 meters.
# radius = 30
# area_of_circle = 3.14 * radius ** 2
# circum_of_circle = 2 * 3.14 * radius

radius = int(input('Dairenin yaricapini giriniz: '))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print('Girdiginiz degerin alani:', area_of_circle)
print('Girdiginiz degerin cevresi:', circum_of_circle)

print('\n')

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

isim = input('Isminizi giriniz: ')
soyisi = input('Soyadinizi giriniz: ')
ulkeniz = input('Ulkenizi giriniz: ')
yasiniz = int(input('Yasinizi giriniz: '))

# 7. use help function 

print(help(input))
