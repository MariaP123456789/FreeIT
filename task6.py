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
except TypeError:
	print("I told 'Input a number from 1 to 12'")

def func_2(times_of_the_year, num):
	for year_time in times_of_the_year:
		if num in times_of_the_year[year_time]:
			return year_time

print(func_2(times_of_the_year, num))

