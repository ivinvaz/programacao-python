import datetime as dt
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.header import Header

meu_email = "atividade.python.4@gmail.com"
senha = "nhin rxfx fpjh scml"

hoje = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv("programacao-python/Codigos/04/data/data_nasc01.csv")
datas_aniv = {(data_row["Mes"],data_row["Dia"]): data_row for (index,data_row) in data.iterrows()}
if hoje in datas_aniv:
    pessoa_aniv = datas_aniv[hoje]
    with open("programacao-python/Codigos/04/data/mensagem.txt", encoding="utf-8") as data:
        conteudo = data.read()
        conteudo = conteudo.replace("[NOME]", pessoa_aniv["Nome"])
    msg = MIMEText(conteudo, 'plain', 'utf-8')
    msg['Subject'] = Header('Feliz Aniversário', 'utf-8')
    msg['From'] = meu_email
    msg['To'] = pessoa_aniv["Email"]
    with smtplib.SMTP("smtp.gmail.com", 465) as nova_conexao:
        nova_conexao.starttls()
        nova_conexao.login(user=meu_email,password=senha)
        nova_conexao.sendmail(msg)