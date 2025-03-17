import requests
from datetime import datetime

parametros = {
    "lat":"-15.826691",
    "lng":"-47.921822",
    "formatted":"0",
}

data = requests.get(url="https://api.sunrise-sunset.org/json", params=parametros)
data.raise_for_status()
data = data.json()
por_do_sol = data["results"]["sunset"].split("T")[1].split(":")
nascer_do_sol = data["results"]["sunrise"].split("T")[1].split(":")

print(f"{por_do_sol}\n{nascer_do_sol}")

agora = datetime.now()
hora = agora.hour