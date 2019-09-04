# criar um programa que gerencia o aproveitamento de um jogador de futebol. O programa
# vai ler o nome do jogador, quantas partidas ele jogou e a quantidade de gols feitos.
# tudo será guardado em um dicionario.

'''
-= Ler dados =-
Nome do Jogador: Joelson
jogos = Quantas partidas {joelson} jogou? 5
for partidas in range(0, jogos):
 quantos gols na partida {partidas+1}?
=- Apresenta o dicionario -=
{'nome': 'Joelson', 'gols': [2, 1, 0, 0,3], 'total': 6}
------------------------------------------
for k , v in dicionario:
  print(f' o campo {k} tem valor {v}')
----------------------------------------
O jogador {nome} jogou {jogos} partidas:
for variavel in dicionario:
 for gols in variavel.values()
  print(f'=> na partida {jogos+1} , fez {listadegols[variavel]} gols.
foi um total de {total} gols.

'''
jogo = {}
gols =[]
contador = 1
totalgols = g = 0
print("EXERC093 - CADASTRAR JOGADOR, PARTIDAS E GOLS")

jogo['jogador'] = str(input("NOME DO JOGADOR: ")).strip().capitalize()
partidas = int(input("QUANTAS PARTIDAS JOGOU? "))
jogo['partidas'] = partidas
if partidas == 0:
    print()
else:
    while contador <= partidas:
        g = (int(input(f"Quantos gols na partida {contador}? ")))
        totalgols = totalgols + g
        gols.append(g)
        contador += 1
contador = 1
jogo['gols'] = gols
jogo['total'] = totalgols
print("-"*30)
print("STATUS 01: Dicionário")
print(jogo)
print("-"*30)
print("STATUS 02: Campos")
for k, v in jogo.items():
    print(f'o campo {k} tem valor {v}')
print("-"*30)
print("STATUS 03 : Chave e Valor")
for goal in gols:
    print(f"=> na partida {contador}, {jogo['jogador']} fez {gols[goal]} gol(s)")
    contador += 1
print(f"O total de gols foi {jogo['total']}")