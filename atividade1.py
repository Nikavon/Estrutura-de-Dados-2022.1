#Nome valido
#Receber apenas letras
#O primeiro caractere é sempre uma letra maisucula
#

# lista = "abcdef"
# print(lista[2:])

nomeValido = input ("Digite o Nome: ")

if nomeValido[0].isupper() and nomeValido [1:].islower() and nomeValido.isalpha():
    print("Nome válido")
else:
    print("Nome inválido")
    