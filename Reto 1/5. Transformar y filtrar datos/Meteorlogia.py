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

# for i, temp in enumerate(datos['daily']['temperature_2m_mean']):
#     datos['daily']['temperature_2m_mean'][i] = formula_a_farengeit(temp)
#     print(f"Temperatura media del día {i+1}: {datos['daily']['temperature_2m_mean'][i]} °F")


# temperaturas = datos['daily']['temperature_2m_mean']
# media = sum(temperaturas) / len(temperaturas)
# temperaturas_menores = [temp for temp in temperaturas if temp <= media]
# temperaturas_superiores = [temp for temp in temperaturas if temp > media]
# print(f"Temperaturas menores o iguales a la media ({media:.2f} °C): {temperaturas_menores}")
# print(f"Temperaturas superiores a la media ({media:.2f} °C): {temperaturas_superiores}")

temperaturas = datos['daily']['temperature_2m_mean']
temperaturas_inferiores = [temp for temp in temperaturas if temp < 15]
print(f"Temperatures inferiores a 15ºC: {temperaturas_inferiores}")

temperaturas_superiores = [temp for temp in temperaturas if temp > 15]
print(f"Temperaturas superiores a 15 °C: {temperaturas_superiores}")

temperaturas_de15 = [temp for temp in temperaturas if temp == 15]
print(f"Temperaturas iguales a 15 °C: {temperaturas_de15}")

tuplas_temperaturas = [(temp, round(formula_a_farengeit(temp), 1)) for temp in temperaturas]
print(f"Tuplas de temperaturas (°C, °F): {tuplas_temperaturas}")

variaciones = [temperaturas[i] - temperaturas[i-1] for i in range(1, len(temperaturas))]
print(f"Variaciones respecto al día anterior: {round(sum(variaciones), 1)}")

for temp in temperaturas:
    if temp > 15:
        print(f"{temp} hace calor")
    elif temp < 15:
        print(f"{temp} hace frio")
    else:
        print(f"{temp} esta templao el dia")