"""
10. Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.

"""

celcs = float(input("Digite o grau em Celcius: "))
faren = (celcs * 9)/ 5 + 32

print(f"O grau {celcs:.1f}ºC corresponde a {faren}ºF")
