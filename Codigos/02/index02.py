altura = float(input("Altura: "))
peso = int(input("Peso: "))

if altura > 3:
    raise ValueError("Não existe humano acima de 3 metros.")

imc = peso/altura ** 2
print(imc)