# Questão 6

def inverte (n: int) -> int:

    aux = len(str(n)) # aux recebe o tamanho do número inteiro recebido pela função
    if n < 10: # Caso base
        return n
    resto = n % 10
    aux -= 1  # aux -= 1 <=> aux = aux - 1
    return resto * (10**aux) + inverte(n // 10) # Caso recursivo

def main_exercicio6():
    
    n = int(input("Digite um número qualquer: "))
    invertido = inverte(n)
    print("%d ----> %d\n"%(n,invertido))
    return
    
    main_exercicio6()
