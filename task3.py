#3.1 Организовать консольный вывод строки “Hello world!”
print('Hello, world!')
#3.2 Запросить консольный ввод имени пользователя, организовать консольный вывод строки вида: “Hello, {user}!”, где user – введенное пользователем имя.
user1 = input()
print('Hello ' + str(user1))
print(f'Hello {user1}')
print('Hello {}'.format(user1))
#3.3 Объявить переменную строкового типа со значением ‘Hi, I am a string variable’, 
#объявить переменную с целочисленным значением 100. Организовать консольный вывод конкатенации строковой и целочисленной переменных 
#с результатом: ‘Hi, I am a string variable100’
string = 'Hi, I am a string variable'
number = 100
print(string +'{}'.format(number))
#3.4 Организовать консольный вывод факториала от 100
import math
print(math.factorial(100))
