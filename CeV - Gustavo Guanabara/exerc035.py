#035: ler tres retas e determinar se pode ou n formar um triangulo:

'''
Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior  que o valor absoluto (módulo) da diferença dos outros
dois lados e menor que a soma dos outros dois lados.
Veja o resumo da regra abaixo:

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''

print("--- TRIANGULO ---")
a = int(input("Digite o 1o. valor: "))
b = int(input("Digite o 2o. valor: "))
c = int(input("Digite o 3o. valor: "))

if a < b + c and b < a + c and c < a + b:
    print("Esses valores podem formar um triângulo")
else:
    print("Esses valores não podem formar um triângulo")