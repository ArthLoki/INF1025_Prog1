# Exercício 6 - Lista Funções

import exercicio5_listaFunçoes as ex5

def calculaGrauFinal(notaConEsp, notaConGeral, notaMat, notaPort):

    percConEsp = ex5.calcula_percent(notaConEsp, 40)
    percConGeral = ex5.calcula_percent(notaConGeral, 20)
    percMat = ex5.calcula_percent(notaMat, 15)
    percPort = ex5.calcula_percent(notaPort, 25)

    grauFinal = percConEsp + percConGeral + percMat + percPort

    return grauFinal

notaConEsp = float(input("Digite a sua nota de Conhecimento Específico: "))
notaConGeral = float(input("Digite a sua nota de Conhecimento Geral: "))
notaMat = float(input("Digite a sua nota de Matemática: "))
notaPort = float(input("Digite a sua nota de Português: "))

grauFinal = calculaGrauFinal(notaConEsp, notaConGeral, notaMat, notaPort)

print("\nSeu grau final é %.1f\n"%(grauFinal))
