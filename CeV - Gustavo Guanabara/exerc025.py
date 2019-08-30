#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Qual o seu nome? ").upper()
tnome = nome.split()
print(tnome)

if "SILVA" in tnome:
    print("Você possui Silva no seu nome!")
else:
    print("Você não possui Silva no seu nome!")