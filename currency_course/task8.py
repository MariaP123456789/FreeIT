import requests
import logging
from datetime import datetime, timedelta


logging.basicConfig(filename='log_file.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Start')

def get_courses(date):
	str_access = "https://openexchangerates.org/api/historical/" + date + ".json?app_id=caba407f4e844254b6b5b6abc2046365"
	try:
		response = requests.get(str_access)
		return response.text
	except Exception:
		logging.warning('Ошибка доступа к API по адресу ' + str_access)
		return ''
	
def get_currencies():
	str_access = "https://openexchangerates.org/api/currencies.json?app_id=caba407f4e844254b6b5b6abc2046365"	
	try:
		response = requests.get(str_access)
		return response.json()
	except Exception:
		logging.warning('Ошибка доступа к API по адресу ' + str_access)
		return None	
	
# получение словаря валют
dt = get_currencies()
if dt != None:
	try:
		with open('currencies.txt', 'w', encoding='utf-8') as currency_file:
			for key, value in dt.items():
				currency_file.write('{0}: {1} \n'.format(key,value))
	except Exception:
		logging.warning('Ошибка записи в файл currencies.txt')

# получение курсов валют
today = datetime.now()
for i in range(30):	
	strftime = datetime.strftime(today, '%Y-%m-%d')
	try:
		with open('courses' + strftime + '.txt', 'w') as course_file:
			course_file.write(get_courses(strftime))
	except Exception:
		logging.warning('Ошибка записи в файл ' + 'courses' + strftime + '.txt')	
	today = today - timedelta(days=1)

logging.info('End')
