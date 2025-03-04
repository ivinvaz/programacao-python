from tkinter import *
import pandas as pd 
from random import randint, choice
import time

#lendo os arquivos da lista csv

data = pd.read_csv("programacao-python/Codigos/03\data/french_words.csv")
data.to_dict(orient="records")
carta_atual = {}

#configurando funções dos botões

def Prox_carta():
    global carta_atual, timer
    tela.after_cancel(timer)
    carta_atual = choice(data)
    canva.itemconfig(titulo, text="French", fill="black")
    canva.itemconfig(texto, text=carta_atual["French"], fill="black")
    canva.itemconfig(imagem, image=bg_branco)
    timer = tela.after(3000, func=Flip_carta)

def Flip_carta():
    canva.itemconfig(titulo, text="English", fill="white")
    canva.itemconfig(texto, text=carta_atual["English"], fill="white")
    canva.itemconfig(imagem, image=bg_verde)

#configurando GUI

tela = Tk()
tela.title("Flashy")
tela.config(padx=50,pady=50, bg="#b1ddc6")

timer = tela.after(3000,func=Flip_carta)

bg_verde = PhotoImage(file="programacao-python/Codigos/03/images/card_back.png")
bg_branco = PhotoImage(file="programacao-python/Codigos/03/images/card_front.png")
botao_verde = PhotoImage(file="programacao-python/Codigos/03/images/right.png")
botao_vermelho = PhotoImage(file="programacao-python/Codigos/03/images/wrong.png")

canva = Canvas(width=800,height=526)
canva.config(bg="#b1ddc6", highlightthickness=0)
imagem = canva.create_image(400,268, image=bg_branco)
titulo = canva.create_text(400,150,font=("Arial",40,"italic"), text="French")
texto = canva.create_text(400,253,font=("Arial",60,"bold"), text=carta_atual)

button_check = Button(image=botao_verde, highlightthickness=0,command=Prox_carta)
button_wrong = Button(image=botao_vermelho, highlightthickness=0,command=Prox_carta)

texto1 = Label(text="French")
texto1.config(font=("Arial",40,"italic"),pady=20)
texto2 = Label(text="trouve")
texto2.config(font=("Arial",60,"bold"),pady=20)


canva.grid(row=0,column=0, columnspan=2)
button_check.grid(row=2,column=0)
button_wrong.grid(row=2,column=1)

tela.mainloop()