"""
13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
H)Para homens: (72.7*h) - 58
M)Para mulheres: (62.1*h) - 44.7

"""
gen = str(input("Digite o seu sexo [Masculino/Feminino]: ")).strip().upper()[0]
while gen not in "FM":
    gen = str(input("Desculpe, valor inválido. Tente novamente.\n"
                    "Digite seu sexo [Masculino/Feminino]: ")).strip().upper()[0]
if gen == "M":
    h = str(input("Digite a sua altura: ")).replace(",", ".")
    pesoideal = 72.7*float(h) - 58
    mcm = h.split(".")
else:
    h = str(input("Digite a sua altura: ")).replace(",", ".")
    pesoideal = 62.1 * float(h) - 44.7
    mcm = h.split(".")

print(f"Sua altura é {mcm[0]}m e {mcm[1]}cm. Seu peso ideal é {pesoideal:.2f}Kg")
