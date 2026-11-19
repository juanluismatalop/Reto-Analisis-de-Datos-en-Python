import requests

def formula_a_farengeit(celsius):
    return((celsius * 9/5) + 32)

url = "https://archive-api.open-meteo.com/v1/archive"

parametros = {
    "latitude": 37.7796,
    "longitude": -3.7849,
    "start_date": "2025-01-01", 
    "end_date": "2025-01-31",
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Madrid",
}

respuesta = requests.get(url, params=parametros, timeout=30)
respuesta.raise_for_status()
datos = respuesta.json()

diario = datos["daily"]
fechas = diario["time"]
medias = diario["temperature_2m_mean"]
maximas = diario["temperature_2m_max"]
minimas = diario["temperature_2m_min"]

registros = {}

for fecha, media, maxima, minima in zip(fechas, medias, maximas, minimas):
    registros[fecha] = {
        "media": media,
        "maxima": maxima,
        "minima": minima,
    }

print(registros)

