"""
8.Faça um Programa que pergunte quanto você ganha por hora e
o número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês.

"""
from datetime import date

mesatual = date.today().month
mesesano = ["janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"
            ]

ganhahora = float(input("Quanto você ganha por hora?: R$"))
trabalhohora = str(input("Quantas horas você trabalha por dia [hh:mm]?: ")).split(":")
diastrabalho = int(input(f"Quantos dias você trabalhou no mês de {mesesano[mesatual-1]}: "))
if len(trabalhohora) > 1:
    convmin = int(trabalhohora[1]) / 60
else:
    convmin = 0
convhora = int(trabalhohora[0])
horatotal = (convhora + convmin)
salario = (horatotal * diastrabalho) * ganhahora
print(f"Seu salario é R${salario:.2f}")
