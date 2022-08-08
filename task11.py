import time
import requests
import logging
import psycopg2
import task10_addition
from threading import Thread, Lock
from datetime import datetime, timedelta


# создание списка с датами
def create_data_list():
	data_list = []
	today = datetime.now()
	for i in range(task10_addition.days_number):
		strftime = datetime.strftime(today, '%Y-%m-%d')
		data_list.append(strftime)
		today = today - timedelta(days=1)
	return data_list

# обращение к API
def get_json(data_list, url):
	try:
		if data_list != None:
			for data_el in data_list:	
				url = url.replace('DATA', data_el) 		
				response_json = requests.get(url).json()
				lock.acquire()
				n = {data_el:response_json['rates']}
				results.append(n)
				lock.release()
		else:
			response_json = requests.get(url).json()
			results.append(response_json)
	except Exception as e:
		logging.info(str(e))

# асинхронное получение данных
def asynch_launcher(target_func, thread_number, 
					target_list, *args):
						
	thread_list = []	
	for th in range(thread_number):
		thread = Thread(target=target_func, args=(target_list[th::thread_number], *args))
		thread_list.append(thread)
		thread.start()
	for th in thread_list:
		th.join()
		
# выполнение запроса в базе
def execute_raw_sql_query(query_text):
	data = None
	try:
		with psycopg2.connect(**task10_addition.CREDENTIALS) as connection:
			cursor = connection.cursor()
			cursor.execute(query_text)
			if 'SELECT' in query_text:
				data = cursor.fetchall()
			connection.commit()		
	except Exception as e:
		logging.info(str(e))
	return data
	
# формирование текста запроса для создания и заполнения таблиц
def query_text():
	
	# для переопределения
	global results
	
	query_text = "CREATE TABLE currencies 				\
						(cur_id VARCHAR(3) PRIMARY KEY,	\
						cur_name TEXT);					\
					CREATE TABLE currency_data 			\
						(id SERIAL PRIMARY KEY,			\
						cur_code VARCHAR(3),			\
						value DECIMAL,					\
						cur_data DATE,					\
						FOREIGN KEY (cur_code) 			\
						REFERENCES currencies(cur_id));	"
									
	get_json(None, f"https://openexchangerates.org/api/currencies.json?app_id={task10_addition.my_ID}")
	dt_currencies = results[0]
	query_text += "INSERT INTO currencies(cur_id, cur_name) VALUES "
	for key, value in dt_currencies.items():
		new_value = value.replace("'", "")
		query_text += f" ('{key}','{new_value}'), "
	
	results = []
	query_text = f"{query_text[:-2]} ; INSERT INTO currency_data(cur_code, value, cur_data) VALUES "
	start = time.time()
	url = f"https://openexchangerates.org/api/historical/DATA.json?app_id={task10_addition.my_ID}"	
	asynch_launcher(get_json, task10_addition.thread_number, target_list, url)
	end = time.time()
	print(round(end - start, 3))
	
	for i in results:
		for strftime, dt in i.items():
			for key, value in dt.items():
				new_value = float(value)
				query_text += f" ('{key}','{new_value}', '{strftime}'), "
			
	query_text = query_text[:-2]
	
	return query_text
		
	
# основной код
task10_addition.basicConfig()
target_list = create_data_list()
results = []
lock = Lock()
execute_raw_sql_query(query_text())

# отдельный запрос - выборка
data = execute_raw_sql_query("SELECT value FROM public.currency_data \
							WHERE cur_data = DATE '2022-07-15' \
							AND cur_code = 'BYN'")
print(data)
