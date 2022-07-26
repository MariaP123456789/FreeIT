import requests
from datetime import datetime, timedelta


def get_courses(date):
	# 2013-02-16
	str_access = "https://openexchangerates.org/api/historical/" + date + ".json?app_id=caba407f4e844254b6b5b6abc2046365"
	response = requests.get(str_access)
	return response.text
	
def get_currencies():
	response = requests.get("https://openexchangerates.org/api/currencies.json?app_id=caba407f4e844254b6b5b6abc2046365")
	return response.json()
	
	
# получение словаря валют
dt = get_currencies()
with open('currencies.txt', 'w', encoding='utf-8') as currency_file:
	for key, value in dt.items():
		currency_file.write('{0}: {1} \n'.format(key,value))

# получение курсов валют
today = datetime.now()
for i in range(30):	
	strftime = datetime.strftime(today, '%Y-%m-%d')
	with open('courses' + strftime + '.txt', 'w') as course_file:
		course_file.write(get_courses(strftime))
	today = today - timedelta(days=1)
