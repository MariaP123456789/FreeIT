#3.1 Организовать консольный вывод строки “Hello world!”
print('Hello, world!')
#3.2 Запросить консольный ввод имени пользователя, организовать консольный вывод строки вида: “Hello, {user}!”, где user – введенное пользователем имя.
user1 = input()
print('Hello ' + str(user1))
print(f'Hello {user1}')
print('Hello {}'.format(user1))
