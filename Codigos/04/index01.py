import smtplib

meu_email = "atividade.python.4@gmail.com"
senha = "nhin rxfx fpjh scml"

with smtplib.SMTP("smtp.gmail.com") as nova_conexao:
    nova_conexao.starttls() #Estabelece uma conexão segura com criptografia
    nova_conexao.login(user=meu_email,password=senha)
    nova_conexao.sendmail(from_addr=meu_email, to_addrs="vaz.ivin@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.")

