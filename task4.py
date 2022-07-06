from datetime import datetime
import time
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

#4.6 Организовать последовательный вывод чисел от 0 до 10 с запросом нажатия клавиши enter пользователем для каждого последующего элемента.
for x in range(10):
	print(x)
	input() #???
	#keyboard.wait('enter')

#4.7* Очистить строку string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'  от заглавных букв. Вывод организовать в новой строке. Пробелы так же должны содержаться в результате.
string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'
string2 = ''
for x in string:
	if not x.isupper():
		string2 = string2 + x
print(string2)

#4.8 Из списка с цветами радуги организовать консольный вывод строки вида: “
#Красный – 1 цвет радуги”. Список цветов радуги colors = [“красный”, “оранжевый”, “желтый”, “зеленый”, “голубой”, “синий”, “фиолетовый”]. 
#Название цвета выводить с заглавной буквы.
colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
for element in colors:
	num = colors.index(element) + 1
	print(element.capitalize() + ' - ' + str(num) + ' цвет радуги')

#4.9 Организовать цикл while, который будет выполнять вывод чисел от 0 до бесконечности в течении 10 секунд. 
x = 0;
currentTime = time.time()
while time.time() - currentTime < 10:
	print(x)
	x+=1

#4.10 При помощи цикла for организовать консольный вывод вида:
for x in range(1,11):
	string = ''
	for y in range(x):
		string = string + str(x)
	print(string)
