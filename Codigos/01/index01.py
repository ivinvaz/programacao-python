from tkinter import *
from tkinter import messagebox
import random
import json

usuarios = 0
# ---------------------------- Função Search --------------------------- #

def search():
    usuario_website = entrada_website.get()
    try:
        with open("programacao-python/Codigos/01/data_index01.json") as data:
            dic_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="Arquivo não encontrado.")
    else:
            if usuario_website in dic_data:
                email = dic_data[usuario_website]["email"]
                senha = dic_data[usuario_website]["password"]
                messagebox.showinfo(title=usuario_website,message=f"Email: {email}\nSenha: {senha }")
        
    
# ---------------------------- gerar senha ------------------------------- #

def gerar_senha():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    return entrada_senha.insert(0,password)

# ---------------------------- salvar senha ------------------------------- #

def salvar():
    global usuarios
    usuarios += 1
    usuario_website = entrada_website.get()
    usuario_user = entrada_user.get()
    usuario_senha = entrada_senha.get()
    new_data = {usuario_website:{
        "email": usuario_user,
        "password": usuario_senha,
    }}

    if usuario_senha == "" or usuario_user == "" or usuario_website == "":
        messagebox.showerror(title="Erro",message="As informações não podem estar vazias")
    else:
        try:
            with open("programacao-python/Codigos/01/data_index01.json","r") as data:
                data_file = json.load(data)
        except FileNotFoundError:
            with open("programacao-python/Codigos/01/data_index01.json","w") as data:
                json.dump(new_data,data,indent=4)
        else:
            data_file.update(new_data)
            with open("programacao-python/Codigos/01/data_index01.json","w") as data:
                json.dump(data_file,data,indent=4)
        finally:
                entrada_website.delete(0,END)
                entrada_user.delete(0,END)
                entrada_user.insert(0, "@gmail.com")
                entrada_senha.delete(0,END)

# ---------------------------- configuração de interface ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)

imagem = PhotoImage(file="programacao-python/Codigos/01/logo.png")

canva = Canvas(width=200,height=200)
canva.create_image(100,100,image=imagem)
canva.grid(row=0,column=1)

label1 = Label(text="Website:")
label1.config(font=("Arial",14))
label1.grid(row=1,column=0)

label2 = Label(text="Email/Username:")
label2.config(font=("Arial",14))
label2.grid(row=2,column=0)

label3 = Label(text="Password:")
label3.config(font=("Arial",14))
label3.grid(row=3,column=0)

entrada_website = Entry(width=32)
entrada_website.focus()
entrada_website.grid(column=1,row=1,columnspan=1)

entrada_user = Entry(width=52)
entrada_user.insert(0, "@gmail.com")
entrada_user.grid(column=1,row=2,columnspan=2)


entrada_senha = Entry(width=32)
entrada_senha.grid(column=1,row=3)

botao_senha = Button(text="Generate Password", command=gerar_senha)
botao_senha.grid(column=2,row=3)

botao_add = Button(text="Add", width=36, command=salvar)
botao_add.grid(column=1,row=4,columnspan=2, pady=20)

botao_search = Button(text="Search", width=15, command=search)
botao_search.grid(column=2,row=1,columnspan=1, pady=20)

window.mainloop()