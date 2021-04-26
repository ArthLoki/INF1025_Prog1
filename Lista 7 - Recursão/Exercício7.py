# Questao 7

def mudaBase(n: int, base: int) -> int:

    # Casos base
    if n == 0:
        return 0
    elif base == 10:
        return n
    
    # Caso recursivo
    resto = n % base
    quociente = n // base
    
    return resto + mudaBase(quociente, base) * 10

def main_exercicio7():
  
    n = int(input("Digite um número na base 10: "))
    base = int(input("Digite a base para o numero n ser convertido: "))
    nBaseNova = mudaBase(n,base)
    
    print("Mudança de base: n = %d na base 10 ----> n = %d na base %d\n"%(n, nBaseNova, base))

    return
  
  main_exercicio7()
