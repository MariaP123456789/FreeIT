import math
import time


SQRT_2 = math.sqrt(2)


#6.1 Написать функцию для записи строки в текстовый файл. В качестве аргументов принимает расположение текстового файла, 
#модификатор доступа, строку для записи. Использовать менеджер контекста. Ничего не возвращает
def my_func(path, text = ''):
	with open(path, 'w') as file:
		file.write(text)
		print('Text in the file:', text)
		
my_func('123.txt', 'Have a good day ))) ')


#6.2 Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и
# возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень)

#для закрепления
def func(**kwargs):
	return kwargs	
times_of_the_year = func(Winter = [1,2,12], Spring = list(range(3,6)), Summer = list(range(6,9)), Autumn = list(range(9,12)))

try:
	num = int(input('Input a number from 1 to 12:'))
except ValueError:
	print("I told 'Input a number from 1 to 12'")

def func_2(times_of_the_year, num):
	for year_time in times_of_the_year:
		if num in times_of_the_year[year_time]:
			return year_time

print(func_2(times_of_the_year, num))


#6.3 Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (кортеж значений): 
#периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
	global SQRT_2
	a = [side*4, side*side, side * SQRT_2]
	return a

print(square(4))
	
	
#6.4 Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых 
#(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, 
#и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank(a, years):
	for i in range(years):
		a = a * 1.1;
	return a
	
a = int(input('Input sum:'))
years = int(input('Input amount of years:'))
print(bank(a, years))


#6.5 Написать декоратор, который будет выводить время выполнения декорируемой функции в консоль
def outer(outer_func):
	def inner(*args, **kwargs):
		current_time = time.time()
		result = outer_func(*args, **kwargs)
		return print('outer_2 time: ' + str(time.time() - current_time))
	return inner
	
@outer
def outer_2(x):
	current_time = time.time()
	#просто что-то выполняется 3 секунды
	while time.time() - current_time < 3:
		x+=1
	
outer_2(0)
	
