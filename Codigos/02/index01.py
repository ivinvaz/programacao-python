#resolução de erros

#try, except, else, finally 

try:
    file = open("Arquivoinexistente.txt") 
    dic_ex = {"key": "value"}
    print(dic_ex["item_inexistente"])
except FileNotFoundError:
    file = open("Arquivoinexistente.txt","w")
    file.write("Alguma coisa.\n")
except KeyError as mensagem_erro:
    print(f"O item {mensagem_erro} não existe na lista.")
else:
    conteudo = file.read()
    print(conteudo)
finally:
#   raise KeyError
#   raise TypeError("Erro criado.")
    file.close()
    print("Arquivo fechado.")