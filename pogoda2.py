import requests
from pprint import pprint
import json


city = "New York"
def main():
	response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f69f7dd713845517316a0aa6896c3840&units=metric")
	weather = response.json()
	pprint(weather)
	print("The weather for", weather['name'])
	print(weather['main']['temp'])
	print(weather['weather'][0]['description'])


if __name__ == '__main__':
	main()

