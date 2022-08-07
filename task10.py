import psycopg2
import task10_addition
import logging
import task8_addition
import requests
from datetime import datetime, timedelta


task10_addition.basicConfig()

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
		
def get_json(url):
	result = None	
	try:
		response = requests.get(url)
		result = response.json()
	except Exception as e:
		logging.info(str(e))
	return result
	
# первый запрос	- создание
query_text_create_tables = "CREATE TABLE currencies 				\
									(cur_id VARCHAR(3) PRIMARY KEY,	\
									cur_name TEXT);					\
							CREATE TABLE currency_data 				\
									(id SERIAL PRIMARY KEY,			\
									cur_code VARCHAR(3),			\
									value DECIMAL,					\
									cur_data DATE,					\
									FOREIGN KEY (cur_code) 			\
									REFERENCES currencies(cur_id));	"
									
execute_raw_sql_query(query_text_create_tables)

# второй запрос - заполнение
dt_currencies = get_json(f"https://openexchangerates.org/api/currencies.json?app_id={task8_addition.my_ID}")
query_text_insertion = "INSERT INTO currencies(cur_id, cur_name) VALUES "
for key, value in dt_currencies.items():
	new_value = value.replace("'", "")
	query_text_insertion += f" ('{key}','{new_value}'), "
	
query_text_insertion = f"{query_text_insertion[:-2]} ; INSERT INTO currency_data(cur_code, value, cur_data) VALUES "
today = datetime.now()
for i in range(task8_addition.days_number):	
	strftime = datetime.strftime(today, '%Y-%m-%d')
	dt = get_json(f"https://openexchangerates.org/api/historical/{strftime}.json?app_id={task8_addition.my_ID}")['rates']
	for key, value in dt.items():
		new_value = float(value)
		query_text_insertion += f" ('{key}','{new_value}', '{strftime}'), "
	today = today - timedelta(days=1)

execute_raw_sql_query(query_text_insertion[:-2])

# третий запрос - выборка
data = execute_raw_sql_query("SELECT value FROM public.currency_data \
											WHERE cur_data = DATE '2022-07-15' \
											AND cur_code = 'BYN'")
print(data)

