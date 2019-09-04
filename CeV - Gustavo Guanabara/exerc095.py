# aprimorar o desafio 093 para que ele funcione com varios jogadores (quer continuar [s/n])
# incluir um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''


'''
tabelaj =[]
jogador = {}
gols =[]
contador = 1
totgols = 0

while True:
    jogador = {}
    jogador['nome'] = str(input("Nome do jogador: ")).strip().upper()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    if partidas == 0 :
        print()
    else:
        while contador <= partidas:
            g = int(input(f"Quantos gols na partida {contador}?"))
            totgols += g
            gols.append(g)
            contador += 1
    jogador['gols'] = gols
    jogador['total'] = totgols
    tabelaj.append(jogador)
    contador = 1
    totgols = 0
    gols = []
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("Valor inválido. Digite S ou N\nDeseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("=-"*30)
print("cod  ", end="")
for i in jogador.keys():
    print(f"{i:<18}", end="")
print()
print("-"*40)
for k, v in enumerate(tabelaj):
    print(f"{k+1:>3}", end="  ")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()
print("-"*40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (Digite 0 para encerrar)"))
    if busca == 0:
        break
    if busca > len(tabelaj):
        print(f"Erro! Não existe jogador com o código {busca}")
    else:
        print(f'  - LEVANTAMENTO DO JOGADOR {tabelaj[busca-1]["nome"]}')
        for i, g in enumerate(tabelaj[busca-1]["gols"]):
            print(f"   No jogo {i+1} fez {g} gol(s)")
    print("-"*40)
print("<<ENCERRADO>>")