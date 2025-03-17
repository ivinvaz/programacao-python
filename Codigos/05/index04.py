import requests
import smtplib
from datetime import datetime

parametros = {
    "lat":"-15.826691",
    "lng":"-47.921822",
    "formatted":"0",
}
data = requests.get(url="https://api.sunrise-sunset.org/json", params=parametros)
data.raise_for_status()
data = data.json()
por_do_sol = data["results"]["sunset"].split("T")[1].split(":")[0]

data2 = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_lat_atual = data2.json()["iss_position"]["latitude"]
iss_lng_atual = data2.json()["iss_position"]["longitude"]
lat_atual = -15.826691
lng_atual = -47.921822

meu_email = "atividade.python.4@gmail.com"
senha = "nhin rxfx fpjh scml"

agora = datetime.now().hour

if abs(lat_atual - float(iss_lat_atual)) <= 1 and abs(lng_atual - float(iss_lng_atual)) <= 1 and agora >= por_do_sol:
    with smtplib.SMTP("smtp.gmail.com") as nova_conexao:
        nova_conexao.starttls() 
        nova_conexao.login(user=meu_email,password=senha)
        nova_conexao.sendmail(from_addr=meu_email, to_addrs="vaz.ivin@gmail.com", msg="Subject:ISS Próxima\n\nOlhe para cima!.")

print(f"ISS latitude atual: {iss_lat_atual}\nISS longitude atual: {iss_lng_atual}\nLatitude atual: {lat_atual}\nLongitude atual: {lng_atual}\nHora por do Sol: {por_do_sol}\nHora agora: {agora}")