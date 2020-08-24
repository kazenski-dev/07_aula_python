"""
Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
multiplicação e divisão). O usuário deve informar dois números e o programa deve
fazer as quatro operações.
"""
class Calculadora:

  def operacoes (self, valor1, valor2):
    print("Soma = ", valor1 + valor2)
    print("Subtracao = ", valor1 - valor2)
    print("Multiplicacao = ", valor1 * valor2)
    print("Divisao = ", valor1 / valor2)

operando = Calculadora()

numero = int(input ("Insira o 1º numero: "))
numero2 = int(input ("Insira o 2º numero: "))

operando.operacoes(numero, numero2)