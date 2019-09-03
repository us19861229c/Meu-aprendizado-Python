# faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# o programa vai perguntar quantos jogos serão gerados, e vai sortear seis numeros
# de 1 a 60, para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
sorteiofim = []
sorteiomega = []
cont = 0
esc = contador = 1
print("="*30)
print(" GERADOR DE JOGOS DA MEGA-SENA")
print("="*30)
jogos = int(input("Quantos jogos deseja fazer? "))
while esc < jogos + 1:
    while cont < 6:
        nmega = randint(1, 60)
        if nmega not in sorteiomega:
            sorteiomega.append(nmega)
            cont += 1
    sorteiomega.sort()
    sorteiofim.append(sorteiomega[:])
    sorteiomega.clear()
    cont = 0
    esc +=1
print(f"=-=-=-= SORTEANDO {jogos} JOGOS =-=-=-=")
for posi in range(0, jogos):
        print(f"Jogo {posi+1}: {sorteiofim[posi]}")
        sleep(0.5)
print(">====<"*2, end="")
print("BOA SORTE", end="")
print(">====<"*2)
