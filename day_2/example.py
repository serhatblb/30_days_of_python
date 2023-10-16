# int to float

from distutils.command.build_scripts import first_line_re

num_int = 10
print('num_int:', num_int)
num_float = float(num_int)
print('num_float:', num_float)

# float to int 
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)
# print(num_str/2)

# str to int or float
# num_str = '10.6'
# print('num_int', int(num_str))      # 10
# print('num_float', float(num_str))  # 10.6

#str to list
first_name = 'Serhat'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)

soyad = input('Soyadınızı giriniz: ')
print(soyad)
