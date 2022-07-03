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
#3.5 Организовать консольный вывод переменной tup 
#представляющую из себя кортеж с последовательностью целочисленных значений от нуля до ста с шагом 2.
tup = tuple(range(0,100,2))
print(tup)
#3.6. Создать список, представляющий из себя квадрат значений кортежа tup ([0,4,16...])
lst = [x**2 for x in tup]
print(lst)
#3.7 В строковой переменной ‘sounds/lofi/chillstep.wav’ выполнить замену sounds на midi, выполнить вывод расширения имени файла.
string = 'sounds/lofi/chillstep.wav'
print(string.replace('sounds', 'midi'))
print(string.split('.')[1])
#3.8 Есть список a = [1, 1, 2, 3, 5, 8, 10, 10], выведите только уникальные элементы
a = [1, 1, 2, 3, 5, 8, 10, 10]
print(set(a))
#3.9 Выведите список, состоящий из элементов списка “а”, увеличенных на 1
print([x+1 for x in a])
#3.10 Организовать вывод количества символов ‘p’ в строке “Python is the most popular programming language”
string = 'Python is the most popular programming language'
print(string.count('p'))
print(string.lower().count('p'))
#3.11 Есть список а = [0, 2, 3, 4] и список b = [2, 2, 5], вывести только те элементы из первого списка, которые отсутствуют во втором.
firstLst = [0, 2, 3, 4]
secondLst = [2, 2, 5]
print(set(firstLst) - set(secondLst))
