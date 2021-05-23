# Импортируем модуль requests для отправления запросов HTTP
import requests

# Основной URL
url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

# Получение параметров по введенной информации
start = input('Enter the start time ')
end = input('Enter the end time ')
lati = input('Enter the latitude ')
longi = input('Enter the longitude ')
maxr = input('Enter the max radius in km ')
minm = input('Enter the min magnitude ')

# Добавляем в запрос, с помощью метода get, URL и  необходимые параметры(ввиде ключей и значений) для получения необходимой информации о землетрясениях
response = requests.get(url, headers={'Accept':'application/json'}, params={
	'format':'geojson',
	'starttime':start,
	'endtime':end,
	'latitude':lati,
	'longitude':longi,
	'maxradiuskm':maxr,
	'minmagnitude':minm
	})

# Весь объект JSON помещается в переменную data в форме словаря
data = response.json()

# Получаем список по ключу 
earthquake_list = data['features']
count = 0 # Начало отсчета с 0
# Цикл, который перебирает всю информацию в списке
# и выводит на экран подходящие, по введенным выше параметрам,
# место и магнитуда землетрясения  
for earthquake in earthquake_list:
	count += 1
	print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}")