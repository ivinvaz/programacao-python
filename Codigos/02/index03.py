import pandas as pd
import csv

nome_final = ""
data = pd.read_csv("/Estudo/GIT/programacao-python/Codigos/02/nato_phonetic_alphabet.csv")
dict_nato = data.to_dict()
df_nato = pd.DataFrame(dict_nato)
nome = input("Digite o nome: ").upper() 
novo_nome = []
list_nome = list(nome)
list_letras = list_nome
for letra in list_nome:
    nova_letra = {letra: row.code for (index,row) in df_nato.iterrows() if letra == row.letter}
    if len(nova_letra) > 0:
        novo_nome.append(nova_letra)
        nova_letra = {}
list_final = [list(x.values())[0] for x in novo_nome]
nome_final = ",".join(list_final)
print(nome_final)