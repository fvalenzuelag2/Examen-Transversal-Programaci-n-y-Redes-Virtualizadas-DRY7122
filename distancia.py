import requests
from geopy.distance import geodesic
import time

# Definir las coordenadas de las ciudades
cities = {
    "Santiago": (-33.4489, -70.6693),
    "Lima": (-12.0464, -77.0428),
    "Arequipa": (-16.4090, -71.5375),
    "Valparaíso": (-33.0458, -71.6197),
    "Iquique": (-20.2307, -70.1357),
    "Tacna": (-18.0066, -70.2463),
}

# Solicitar Ciudad de Origen y Destino
while True:
    print("Ingrese la ciudad de origen (o 'e' para salir):")
    ciudad_origen = input().strip()
    if ciudad_origen.lower() == 'e':
        break

    print("Ingrese la ciudad de destino (o 'e' para salir):")
    ciudad_destino = input().strip()
    if ciudad_destino.lower() == 'e':
        break

    if ciudad_origen not in cities or ciudad_destino not in cities:
        print("Una de las ciudades no está en la lista. Inténtelo de nuevo.")
        continue

    # Calcular la distancia
    coords_origen = cities[ciudad_origen]
    coords_destino = cities[ciudad_destino]
    distancia_km = geodesic(coords_origen, coords_destino).kilometers
    distancia_millas = geodesic(coords_origen, coords_destino).miles

    # Solicitar medio de transporte
    print("Seleccione el medio de transporte:")
    print("1. Avión")
    print("2. Coche")
    print("3. Bicicleta")
    print("4. A pie")

    medio_transporte = input().strip()
    if medio_transporte == '1':
        velocidad_kmh = 800  # velocidad promedio de un avión
    elif medio_transporte == '2':
        velocidad_kmh = 100  # velocidad promedio de un coche
    elif medio_transporte == '3':
        velocidad_kmh = 15   # velocidad promedio de una bicicleta
    elif medio_transporte == '4':
        velocidad_kmh = 5    # velocidad promedio a pie
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        continue

    # Calcular duración del viaje
    duracion_horas = distancia_km / velocidad_kmh
    duracion_horas = round(duracion_horas, 2)
    duracion_minutos = duracion_horas * 60

    # Mostrar resultados
    print(f"\nNarrativa del viaje:")
    print(f"Ciudad de origen: {ciudad_origen}")
    print(f"Ciudad de destino: {ciudad_destino}")
    print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
    print(f"Duración del viaje en {medio_transporte}: {duracion_horas:.2f} horas ({duracion_minutos:.2f} minutos)\n")


