# Faça um programa que leia 5 valores numericos e guarde-os em uma lista
# mostre o maior e o menor valor e suas posições.

from random import randint

valores = []
maiorposi = []
menorposi = []

for num in range(0, 5):
    n = int(input(f"Digite o um valor: "))
    valores.append(n)

for posi, elemento in enumerate(valores):
    if elemento == max(valores):
        maiorposi.append(posi)
    if elemento == min(valores):
        menorposi.append(posi)

print(f"O menor valor digitado foi o {min(valores)} e ele está na(s) posição(ões) {menorposi}")
print(f"O maior valor digitado foi o {max(valores)} e ele está na(s) posição(ões) {maiorposi}")