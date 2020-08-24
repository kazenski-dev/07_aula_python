"""
Escreva uma classe que contém um método que calcule se a pessoa é maior de 18
anos ou não. Receba os dados pela console e chame este método.
"""
class ValidaIdade:
  def validar_valor (self, valor):
    if valor >= 18:
      print ("Maior de Idade")
    else:
      print("Menor de Idade.")

teste_idade = ValidaIdade()

idade = int(input ("Insira a idade: "))

teste_idade.validar_valor(idade)