# Faça um programa que leia nome e peso de várias pessoas guardando tudo numa lista;
# -deseja continuar s/n- , a) quantas pessoas foram cadastradas; b) pessoas mais pesadas;
# c) pessoas mais leves;

nopeso = []
dados = []
listapeso = []
menorp = maiorp = 0

while True:
    dados.append(str(input("Nome: ")).strip())
    dados.append(int(input("Peso: ")))
    if len(nopeso) == 0:
        maiorp = menorp = dados[1]
        print(maiorp, menorp)

    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
        elif dados[1] < menorp:
            menorp = dados[1]
        print(menorp)
        print(maiorp)
    nopeso.append(dados[:])
    dados.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(nopeso)
print(f">>{len(nopeso)} foram cadastradas no programa")
print(f"o maior peso foi {maiorp}kg. Peso de", end=" ")
for p in nopeso:
    if p[1] == maiorp:
        print(f"{p[0]}", end=" ")
print()
print(f"o menor peso foi {menorp}kg. Peso de", end=" ")
for p in nopeso:
    if p[1] == menorp:
        print(f"{p[0]}", end=" ")

