import urllib.parse
import requests
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = input("Ingrese la ubicación de origen: ")  # origen
dest = input("Ingrese la ubicación de destino: ")  # destino 
key = "mGxZsj4S1lbrrsK2BEol4HSRG9NTBSKr"

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "locale": "es_ES"})
json_data = requests.get(url).json()

# obtiene la duracion del viaje en segundos desde json
duration_in_seconds = json_data["route"]["time"]

# obtiene la narrativa del viaje
narrative = json_data["route"]["legs"][0]["maneuvers"]

# Imprimir la narrativa del viaje
print("Narrativa del viaje:")
for step in narrative:
    print(step["narrative"])

# obtiene informacion del viaje en segundos a horas, minutos y segundos
horas = int(duration_in_seconds / 3600)
minutos = int((duration_in_seconds % 3600) / 60)
segundos = int(duration_in_seconds % 60)

distancia = json_data["route"]["distance"]  # obtiene distancia
distancia_km = round(distancia * 1.60934, 2)  # Conversion de millas a kilometros con 2 decimales

# obtiene la informacion del viaje en horas, minutos y segundos
print(f"Duracion del viaje: {horas} horas, {minutos} minutos, {segundos} segundos.")
print(f"Distancia del viaje: {distancia_km} km")  # se ve los kilometros