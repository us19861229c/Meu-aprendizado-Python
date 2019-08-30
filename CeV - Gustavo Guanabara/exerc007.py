#um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nome = input("NOME DO ALUNO:")
n1 = float(input("NOTA 1: "))
n2 = float(input("NOTA 2: "))
media = (n1 + n2)/2

print(f"O aluno {nome}  teve média {media:1f} !")