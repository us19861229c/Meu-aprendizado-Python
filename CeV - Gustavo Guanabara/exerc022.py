#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao tdo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Qual é o seu nome? ")
print(">>",nome.upper())
print(">>",nome.lower())
jnome = nome.strip()
v = jnome.count(" ")
print(">>",len(jnome)- v)
pnome = nome.split()
print(">>",len(pnome[0]))

