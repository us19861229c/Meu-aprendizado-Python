#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input("Digite um numero: ")
space = " ".join(numero)
print(space)
lista = space.split()
print(lista)
tamanho = len(lista)
print(tamanho)
if tamanho == 4:
    print(f"Unidade: {lista[3]:>2}\n"
          f"Dezena: {lista[2]:>3}\n"
          f"Centena: {lista[1]:>2}\n"
          f"Milhar: {lista[0]:>3}")
if tamanho == 3:
    print (f"Unidade: {lista[2]:>2}\n"
           f"Dezena: {lista[1]:>3}\n"
           f"Centena: {lista[0]:>2}")
if tamanho == 2:
    print(f"Unidade: {lista[1]:>2}\n"
          f"Dezena: {lista[0]:>3}")
if tamanho == 1:
    print(f"Unidade: {lista[0]:>2}")