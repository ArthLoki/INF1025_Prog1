# Exercício 3 - Lista Funções

def f2c (fah):
    celsius = (fah - 32) * 5/9
    return celsius
    
fah = float(input("Digite a temperatura em fahrenheit: "))
cels = f2c(fah)

print(cels)
