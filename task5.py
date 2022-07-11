#для графического интерфейса
import tkinter

#создание окна - Tk()
window = tkinter.Tk()
#заголовок
window.title('Simple calculator')
#размеры окна
window.geometry('430x340')

label = tkinter.Label(window, text='0', font=("Arial Bold", 28))
label.grid(row=0, column=0, columnspan=3, sticky="nsew")

#тут строка с набранными символами
str_number = ''
#тут массив
stack = []

#функция для вывода кнопок
def create_buttons(window):
	
	#кнопочка сброса
	btn = tkinter.Button(window, text = 'CE', font=("Arial Bold", 25), bg="red", fg="white", width=5, command=lambda text1='CE': button_click(text1))
	btn.grid(column=3, row = 0)
	
	# массив кнопок
	buttons = (('7', '8', '9', '/'),
			('4', '5', '6', '*'),
			('1', '2', '3', '-'),
			('0', '.', '=', '+')
			)
			
	# вывод кнопок		
	for button_row in buttons:
		for button_text in button_row:			
			# добавление кнопки - окно, текст, шрифт, бэграунд, форграунд (цвет текста), команда (писать без скобок) или присваиваем переменной текст1 передаваемый текст, и отправляем в функцию
			btn = tkinter.Button(window, text = button_text, font=("Arial Bold", 25), bg="red", fg="white", width=5, command=lambda text1=button_text: button_click(text1))
			btn.grid(column=button_row.index(button_text), row = buttons.index(button_row)+1)
		
def button_click(button_text):
	
	#это глобальные переменные добавила в этот контекст
	global label
	global str_number
	global stack
	
	if button_text == '=':
		str_number = calculate()
		#тут записала в лэйбл получившийся текст
		label.configure(text = str_number)
		str_number = ''
		stack = []
	elif button_text == 'CE':
		label.configure(text = '0')
		str_number = ''
		stack = []	
	else:	
		str_number = str_number + button_text
		label.configure(text = str_number)
		stack.append(button_text)
		print(stack)
		
#тут вычисляем
def calculate():
	global stack
	
	str_num = ''
	stack2 = []
	
	len_stack = len(stack)
	
	for i in stack:
		
		#это пока вместо исключений - если последний или первый символ не являются числом, тогда 0
		if  not '0' <= i <= '9':
			if stack.index(i) == len_stack-1:
				return 0
			elif stack.index(i) == 0:
				return 0
				
		if '0' <= i <= '9' or i == '.':
			str_num = str_num + str(i)
		else:
			stack2.append(float(str_num))
			stack2.append(i)
			str_num = ''
		
	stack2.append(float(str_num))
	print(stack2)
	
	num = 0.0
	current_operator = ''
	
	for el in stack2:

		if type(el) != float:
			
			el1 = stack2[stack2.index(el)-1]			
			el2 = stack2[stack2.index(el)+1]
			
			print('el, el1, el2, num', el, el1, el2, num)
			num = calculate_inside2(el, el1, el2, num)	
			
	print(num)
	return num
	
def calculate_inside2(current_operator, el1, el2, num):
					
	print('INSIDE el, el1, el2, num', current_operator, el1, el2, num)
					
	if num == 0:
		#операции над 2 числами вокруг будут
		num = el1;

	if current_operator == '+':
		num = num + el2
	elif current_operator == '/':
		num = num / el2
	elif current_operator == '*':
		num = num * el2
	elif current_operator == '-':
		num = num - el2
	
	print('INSIDE AFTER el, el1, el2, num', current_operator, el1, el2, num)	
	
	#простите
	return(round(num, 4))

	
create_buttons(window)

#отображение окна
window.mainloop()


