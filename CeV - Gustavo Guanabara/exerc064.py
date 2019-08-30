#leia varios numeros ; pare no n = 999 ; conte qnts numeros e some , desconsiderando o flag
from time import sleep
cont = 1
v = 0
soma = 0
while v != 999:
    v = int(input(f"Digite o {cont}o. valor [999 para parar!]: "))
    if v != 999:
        cont += 1
        soma += v
sleep(0.3)
print("\033[31m FLAG!\033[m")
sleep(0.5)
print(f"Foram digitados {cont - 1} numeros e o valor da soma desses numeros é {soma}")