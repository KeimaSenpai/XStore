import requests
from datetime import date


async def tasas_de_cambio(e):
    # Obtén la fecha actual
    fecha_actual = date.today().strftime("%Y-%m-%d")

    # Construye la URL con la fecha actual
    url = f"https://yossthedev.me/kubacash-service/data/{fecha_actual}/informal.json"

    # Realiza la petición GET
    response = requests.get(url)

    # Extraer la moneda
    moneda = response.json()["currency"]

    # Extraer las tasas de cambio y redondear los números
    tasas = response.json()["rates"]
    for moneda, valores in tasas.items():
        tasas[moneda] = {
            "compra": round(valores["buy"]),
            "venta": round(valores["sell"]),
            "medio": round(valores["mid"]),
        }

    # Imprimir los resultados
    for moneda, valores in tasas.items():
        Moneda = f"{moneda}"
        Compra = f'{valores['compra']}'
        print(Moneda)
        #print(f"{moneda} - Compra: {valores['compra']}, Venta: {valores['venta']}, Medio: {valores['medio']}")
