""""
12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

"""

altura = str(input("Digite a sua altura: ")).replace(",",".")
pesoideal = (72.7*float(altura)) - 58
mcm = altura.split(".")


print(f"Sua altura é {mcm[0]}m e {mcm[1]}cm. Assim ", end="")
print(f"seu peso ideal é {pesoideal:.2f}Kg")
