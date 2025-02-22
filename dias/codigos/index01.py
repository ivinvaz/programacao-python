from tkinter import *
from tkinter import messagebox
import random
usuarios = 0
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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

# ---------------------------- SAVE PASSWORD ------------------------------- #

def salvar():
    global usuarios
    usuarios += 1
    usuario_website = entrada_website.get()
    usuario_user = entrada_user.get()
    usuario_senha = entrada_senha.get()

    if usuario_senha == "" or usuario_user == "" or usuario_website == "":
        messagebox.showerror(title="Erro",message="As informações não podem estar vazias")
    else:
        s_n = messagebox.askokcancel(title="Website", message=f"As informações estão corretas: \nEmail:{usuario_user}\nSenha:{usuario_senha}\nSalvar?")

        if s_n:
            with open("programacao-python\dias\itens_gerais\data_index01.txt","a") as data:
                data.write(f"Usuario {usuarios}: {usuario_website} | {usuario_user} | {usuario_senha}\n")
            entrada_website.delete(0,50)
            entrada_user.delete(0,50)
            entrada_user.insert(0, "@gmail.com")
            entrada_senha.delete(0,50)
        else:
            pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)

imagem = PhotoImage(file="programacao-python\dias\itens_gerais\logo.png")

canva = Canvas(width=200,height=200)
canva.create_image(100,100,image=imagem)
canva.grid(row=0,column=1)

label1 = Label(text="Webstite:")
label1.config(font=("Arial",14))
label1.grid(row=1,column=0)

label2 = Label(text="Email/Username:")
label2.config(font=("Arial",14))
label2.grid(row=2,column=0)

label3 = Label(text="Password:")
label3.config(font=("Arial",14))
label3.grid(row=3,column=0)

entrada_website = Entry(width=52)
entrada_website.focus()
entrada_website.grid(column=1,row=1,columnspan=2)

entrada_user = Entry(width=52)
entrada_user.insert(0, "@gmail.com")
entrada_user.grid(column=1,row=2,columnspan=2)


entrada_senha = Entry(width=32)
entrada_senha.grid(column=1,row=3)

botao_senha = Button(text="Generate Password", command=gerar_senha)
botao_senha.grid(column=2,row=3)

botao_add = Button(text="Add", width=36, command=salvar)
botao_add.grid(column=1,row=4,columnspan=2, pady=20)


window.mainloop()