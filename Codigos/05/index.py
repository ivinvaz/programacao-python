import requests

resposta = requests.get(url="http://api.open-notify.org/iss-now.json")
resposta.raise_for_status()
data = resposta.json()["iss_position"]
print(data)