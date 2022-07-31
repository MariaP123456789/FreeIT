import requests
import logging
import task8_addition
from datetime import datetime, timedelta


logging.basicConfig(filename='log_file.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Start')

# получение курсов валют из источника
def get_courses(date):
	result = None
	str_access = f"https://openexchangerates.org/api/historical/{date}.json?app_id={task8_addition.my_ID}"
	try:
		response = requests.get(str_access)	
		result = response.json()
	except Exception as e:
		logging.info(str(e))
	return result
	
# получение словаря валют из источника
def get_currencies():
	result = None
	str_access = f"https://openexchangerates.org/api/currencies.json?app_id={task8_addition.my_ID}"	
	try:
		response = requests.get(str_access)
		result = response.json()
	except Exception as e:
		logging.info(str(e))
	return result	
	
# запись данных в файл
def filing(file_name, file_encoding, info, appending = False, date = ''):
	try:
		with open(file_name, 'a' if appending else 'w', encoding=file_encoding) as currency_file:
			#currency_file.write(date, '\n')
			for key, value in info.items():
				currency_file.write('{0}: {1} \n'.format(key,value))
			#currency_file.write('\n')
	except Exception as e:
		logging.info(str(e))
	
# получение словаря валют
dt = get_currencies()
if dt != None:
	filing('currencies.txt', 'utf-8', dt)

# получение курсов валют
today = datetime.now()
appending = False	
for i in range(task8_addition.days_number):	
	strftime = datetime.strftime(today, '%Y-%m-%d')
	dt = get_courses(strftime)
	if dt != None:
		filing('courses.txt', 'utf-8', dt['rates'], appending, strftime)
	if i == 0:
		appending = True	
	today = today - timedelta(days=1)

logging.info('End')
