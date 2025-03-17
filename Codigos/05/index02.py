from tkinter import *
import requests

#-----------------CONFIGURANDO GERADOR DE FRASE-----------------

def Frase_aleatoria():
    data = requests.get(url="https://api.kanye.rest")
    return canvas.itemconfig(frases_text, text=data.json()["quote"], fill="white")

#-----------------CONFIGURANDO TELA-----------------

tela = Tk()
tela.title("Kanye diz...")
tela.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
imagem_bg = PhotoImage(file="programacao-python/Codigos/05/data/background.png")
canvas.create_image(150,207, image=imagem_bg)
frases_text = canvas.create_text(150,207, text="Kanye dizer jáz aqui",  width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0,column=0)

kanye_img = PhotoImage(file="programacao-python/Codigos/05/data/kanye.png")
kanye_botao = Button(image=kanye_img, highlightthickness=0, command=Frase_aleatoria)
kanye_botao.grid(row=1,column=0)

tela.mainloop()