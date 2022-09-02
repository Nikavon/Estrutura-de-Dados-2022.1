# numero em formato string
# só aceita numero real natural ou inteiro
# em caso de numero q n se encaixa mensagem de erro
# fornecer o tipo do numero
# 123, -1-2-3, 0, 0.1, 0.2, 0.3
numeroValido = input("Insira o número: ")

if numeroValido.isnumeric():
    print(numeroValido, "é um número natural")

elif numeroValido[0] == "-" and numeroValido[1:].isnumeric():
    print(numeroValido, "é um número inteiro")

else:
    # .find esta sendo usado para localizar o caractere q no caso é o "."
    # o .index estava dando erro de execução

    ponto = numeroValido.find(".")

    if ponto == -1:
        print("Erro:", numeroValido, "não é um número válido!")    
        
    elif numeroValido[0:ponto].isnumeric() and numeroValido[ponto + 1:].isnumeric():
        print(numeroValido, "é um número real")

    elif numeroValido[0] == "-" and numeroValido[1:ponto].isnumeric() and numeroValido[ponto +1:].isnumeric():
        print(numeroValido, "é um número real")

    else:
        print("Erro:", numeroValido, "não é um número válido!")              
