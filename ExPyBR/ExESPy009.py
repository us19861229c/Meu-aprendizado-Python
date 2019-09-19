"""
9.Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a
temperatura em graus Celsius.
C = (5 * (F-32) / 9).

"""

faren = float(input("Digite o grau em Farenheit: "))
celcs = ((faren - 32) * 5)/9
print(f'O grau {faren:.1f}ºF é igual a {celcs:.1f}ºC')
