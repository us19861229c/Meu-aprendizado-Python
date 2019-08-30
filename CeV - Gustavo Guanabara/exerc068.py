# jogue par ou impar com o computador,
#o jogo será interrompido quando o jogador perder;
#mostrandoo a quantidade de vitorias consecutivas

from random import randint
from time import sleep
dedosmao = [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vitórias = 0

print("~^~"*16)
print(" P  A  R  OU  I  M  P  A  R!")
print("~^~"*16)
while True:
    pcn = randint(0,10)
    jogador = int(input("Escolha um numero entre 0 e 10: "))
    while jogador not in dedosmao:
        jogador = int(input("Ei!Escolha um numero entre 0 e 10: "))
    sleep(0.1)
    poui = str(input("PAR ou IMPAR? [P/I] ")).strip().upper()[0]
    while poui not in "PI":
        poui = str(input("PAR ou IMPAR? [P/I] ")).strip().upper()[0]
    soma = pcn + jogador
    print("-"*16)
    print(f"Você jogou {jogador} e o Computador jogou {pcn}. E {soma} é", end="")
    print(" \033[35mPAR\033[m"if soma % 2 == 0 else" \033[36mIMPAR\033[m")
    if soma % 2 == 0 and poui == "P":
        print("Você venceu!! =D")
        vitórias +=1
    elif soma % 2 == 1 and poui == "I":
        print("Você venceu!! =D")
        vitórias += 1
    else:
        break
print("Você perdeu! =(")
if vitórias > 1:
    print(f"PLACAR : {vitórias} vitórias consecutivas! Parabéns!")
elif vitórias == 1:
    print("Você venceu uma vez! Parabéns!")
else:
    print("Puxa, você não venceu nenhuma vez!")