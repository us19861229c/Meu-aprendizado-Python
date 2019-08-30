'''
#027: Faça um programa que leia o nome completo de uma pessoa:
 - mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = input("Digite o seu nome completo: ")
listanome = nome.split()
print(' seu primeiro nome é', listanome[0],'\n seu último nome é', listanome[-1])