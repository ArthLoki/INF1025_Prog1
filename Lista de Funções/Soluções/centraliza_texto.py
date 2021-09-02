'''
l) Faça uma função que recebe uma string,o tamanho da linha (número de caracteres)
e um símbolo.

Esta função deve retornar uma string centralizada, precedida e sucedida pelo simbolo.

Exemplo:
centraliza( 'Lalá', 10, '*') --> '***Lalá***'

'''

def centralizaString (texto, tamLinha, simbolo):

    tamTexto = len(texto)
    nReplica = (tamLinha - tamTexto) // 2
    qtdSimbolo = simbolo * nReplica

    centralizada = qtdSimbolo + texto + qtdSimbolo

    return centralizada

texto = input("Digite o texto a ser centralizado: ")
tamLinha = int(input("Digite o tamanho total da string resultante: "))
simbolo = input("Digite o símbolo a ser replicado e agregado a string centralizada: ")
  
centralizada = centralizaString (texto, tamLinha, simbolo)
print(A string centralizada é:\ncentralizada\n)
