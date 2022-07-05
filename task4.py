from datetime import datetime
import os


#4.1 Имеется список a = list(range(0, 11)). На основании списка ‘a’ cгенерировать список, 
#каждым элементом которого является словарь, ключем которого является элемент списка ‘a’, 
#а значением квадрат ключа. ([{0:0}, {1:1}, {2:4}, etc…])

a = list(range(0, 11))
b = []
for element in a:
	b.append({element:element**2})
print(b)

#4.2 Имеется словарь d1 = {‘a’: 1} и словарь d2 = {‘b’: 2} 
#необходимо обновить значение ключа ‘b’ словаря ‘d2’ с 2 на 5. 
#Вывести словарь ‘d3’, представляющий из себя содержимое словаря ‘d1’ и ‘d2’.

d1 = {'a': 1}
d2 = {'b': 2} 

d2['b'] = 5
print(d2)

d3 = {}
for key, value in d1.items():
	d3[key] = value
for key, value in d2.items():
	d3[key] = value
print(d3)

d3 = d1.copy()
d3.update(d2)
print(d3)

#4.3 Имеется словарь d1 = {‘key1’: 1, ‘key2’: 2}, в нем необходимо сменить ключи и значения местами, 
#заменив ‘key’ на ‘value’ ({1: ‘value1’, 2: ‘value2’})
d1 = {'key1': 1, 'key2': 2}
print({value:key for key, value in d1.items()})
	
#4.4 вывести список файлов из текущей директории.
currentDirectory = os.getcwd()
filesList = os.listdir(path = currentDirectory)
print(filesList)

#4.5 Организовать вывод текущего времени и даты в формате “hh-mm MM-dd-YYYY”
currentDate = datetime.today()
strDate = currentDate.strftime('%H-%M %m-%d-%Y')
print(strDate)
