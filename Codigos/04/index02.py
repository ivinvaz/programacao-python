import datetime as dt
import smtplib
from random import choice

hoje = dt.datetime.now()
meu_email = "atividade.python.4@gmail.com"
senha = "nhin rxfx fpjh scml"

if hoje.weekday() == 6:
    with open("programacao-python/Codigos/04/data/quotes.txt") as data:
        data_list = list(data)
        frase_do_dia = choice(data_list)
        with smtplib.SMTP("smtp.gmail.com") as nova_conexao:
            nova_conexao.starttls()
            nova_conexao.login(user=meu_email,password=senha)
            nova_conexao.sendmail(from_addr=meu_email, to_addrs="vaz.ivin@gmail.com", msg=f"Subject:Frase Motivacional do Dia\n\n{frase_do_dia}.")


