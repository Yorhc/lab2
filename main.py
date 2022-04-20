import requests
import os

city = "Moscow,RU"
appid = input("Введите API key (appid): ")

result = requests.get("http://api.openweathermap.org/data/2.5/weather",
  params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = result.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
print()


result = requests.get("http://api.openweathermap.org/data/2.5/forecast",
  params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = result.json()

print("Прогноз погоды на неделю:")
for item in data['list']:
  print(f"Дата < {item['dt_txt']} >")
  print(f"Температура < {item['main']['temp']:+3.0f} >")
  print(f"Погодные условия < {item['weather'][0]['description']} >")
  print(f"Скорость ветра < {item['wind']['speed']} >")
  print(f"Видимость < {item['visibility']} >")
  print("____________________________")