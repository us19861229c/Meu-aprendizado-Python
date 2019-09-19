"""
11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
>> o produto do dobro do primeiro com metade do segundo .
>> a soma do triplo do primeiro com o terceiro.
>> o terceiro elevado ao cubo.

"""

int1 = int(input("Digite um valor inteiro: "))
int2 = int(input("Digite outro valor inteiro: "))
nreal = float(input("Digite um valor real: "))

a = (int1 * 2) + (int2 / 2)
b = (int1 * 3) + nreal
c = nreal ** 3

print(f">>o 1º número: {int1}\n>>o 2º número: {int2}\n>>o 3º número: {nreal}\n")
print(f"o produto do dobro do primeiro com metade do segundo é {a}")
print(f"a soma do triplo do primeiro com o terceiro é {b}")
print(f"o terceiro elevado ao cubo é {c:.2f}")
