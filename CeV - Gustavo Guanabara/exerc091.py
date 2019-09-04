# criar um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios (randint)
# guarde esses resultados num dicionario, no final, coloque esse dicionario em ordem,
# sendo que o primeiro lugar é o vencedor, aquele que tirou o maior numero no dado

"""
=- Gerar os dados -=
sleep()
O {jogador1} tirou {6}
O {jogador2} tirou {1}
O {jogador3} tirou {6}
O {jogador4} tirou {5}
chave {jogador} valor {randint}
-= Ordenar o dicionario =-
Ranking dos jogadores

"""
from random import randint
from time import sleep
from operator import itemgetter
apostas = {}
ranking = []

print("EXERC 91 - JOGADORES DE DADOS")

apostas = {'Jogador_1': randint(1,6), 'Jogador_2': randint(1,6),
           'Jogador_3': randint(1,6), 'Jogador_4': randint(1,6)
           }
print("_"*20)
print("ROLEM OS DADOS!")
print("_"*20)
for k, v in apostas.items():
    print(f">>{k} tirou {v} no dado")
    sleep(0.6)
print("-="*20)
print(" =====  RANKING =====  ")
ranking = sorted(apostas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"   {i+1}o. Lugar: {v[0]} com {v[1]}")
    sleep(0.5)



