import requests
import json

# Definir la URL de la API y la clave de la API
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "<TU_CLAVE_DE_API_AQUÍ>"

# Pedir al usuario que introduzca el nombre de la ciudad
city = input("Introduce el nombre de la ciudad: ")

# Crear los parámetros para la solicitud de la API
params = {"q": city, "appid": api_key, "units": "metric"}

# Hacer la solicitud a la API y obtener la respuesta
response = requests.get(url, params=params)

# Convertir la respuesta a un objeto JSON
data = json.loads(response.text)

# Imprimir el pronóstico del tiempo de la ciudad
print(f"El pronóstico del tiempo para {city} es:")
print(f"{data['weather'][0]['description']}, {data['main']['temp']}°C")