#programa que leia um num inteiro e converta p base escolhida pelo usuario:
from time import sleep
print(">>___<<"*10)
print("             C  O  N  V  E  R  S  O  R         "
      "\n        D E        S   I   S   T   E   M   A   S ")
print(">>___<<"*10)

valorinicial = int(input("Digite um valor em decimal a ser convertido: "))
escolha = int(input("Escolha para qual base deseja converter:"
                    "\n>>[1] digite [1] para binário"
                    "\n>>[2] digite [2] para octal"
                    "\n>>[3] digite [3] para hexadecimal:\n "))
if escolha == 1:
    totbin = ""
    valor = valorinicial
    while valor != 0:
        bin = valor % 2
        totbin = totbin + str(bin)
        valor = valor // 2
    inverte = totbin[::-1]
    print(f" o valor {valorinicial} em decimal, corresponde ao valor {inverte} em binário")

elif escolha == 2:
    totoct = ""
    valor = valorinicial
    while valor != 0:
        oct =  valor % 8
        totoct = totoct + str(oct)
        valor = valor // 8
    inverte = totoct[::-1]
    print(f" o valor {valorinicial} em decimal, corresponde ao valor {inverte} em octal")

elif escolha == 3:
    tothexa = ""
    valor = valorinicial
    while valor != 0:
        hexa = valor % 16
        if hexa == 10:
            hexa = "A"
        elif hexa == 11:
            hexa = "B"
        elif hexa == 12:
            hexa = "C"
        elif hexa == 13:
            hexa = "D"
        elif hexa == 14:
            hexa = "E"
        elif hexa == 15:
            hexa = "F"
        tothexa = tothexa + str(hexa)
        valor = valor // 16
    inverte = tothexa[::-1]
    print(f" o valor {valorinicial} em decimal, corresponde ao valor {inverte} em hexadecimal")
else:
    print("Opção inválida")