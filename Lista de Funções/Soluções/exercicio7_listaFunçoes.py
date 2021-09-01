'''
Escreva uma função que receba o código de um produto (valor inteiro com 4 algarismos) e,
utilizando a função calcula_percent, criada em exercício anterior,
retorne o valor total a pagar pelo
produto. O valor básico do produto e percentual de desconto são obtidos do código do produto de
acordo com a seguinte regra:


• Código do produto: XXYY

• Preço básico: XX * 15,00 + YY

• Percentual de desconto: YY


Exemplo para o código do produto 2314:


    Preço básico: 23 * 15,00 + 14,00 -> 359,00
    Percentual de desconto: 14%
    Total a pagar: 308,74


'''
import exercicio5_listaFunçoes as ex5

def valor_a_pagar(cod):

    primParte = cod // 100
    segParte = cod % 100
    precoBasico = primParte * 15.00 + segParte
    precoDesconto = ex5.calcula_percent(precoBasico, segParte)
    precoFinal = precoBasico - precoDesconto
    return precoFinal

cod = int(input("Digite o seu código: "))
valorAPagar = valor_a_pagar(cod)

print("O valor a ser pago é de %.2f reais\n"%(valorAPagar))
