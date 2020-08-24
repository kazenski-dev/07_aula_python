"""
Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
positivo)
"""
class PositivoNegativo:

  def valida_numero (self, valor):
    if valor >= 0:
      print("O valor {0} e Positivo".format(valor))
    else:
      print("O valor {0} e Negativo".format(valor))

teste = PositivoNegativo()

numero = int(input ("Insira o numero: "))

teste.valida_numero(numero)