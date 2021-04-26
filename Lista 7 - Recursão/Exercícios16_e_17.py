# Lista 7 - Exercícios 16 e 17

# Questão 16
def separaLinha(s):

    if len(s) == 0:
        return
    else:
        print(s)
        separaLinha(s[1:]) 
    return

# Questão 17
def separaLinha_invert(s):

    if len(s) == 0:
        return
    else:
        separaLinha_invert(s[1:])
        print(s)
    return

separaLinha('Cana')
separaLinha_invert('Cana')

'''
Explicação:

Quando invertemos as linhas 9 e 10, acabamos por fazer a recursão primeiro
e printamos depois. Com isso, acabamos por inverter a ordem de execução do
nosso programa e isso resulta na inversão do resultado.

Ex:
1. Função separaLinha -> sem inversão

Cana
ana
na
a

2. Função separaLinha_invert -> com inversão

a
na
ana
Cana

'''
