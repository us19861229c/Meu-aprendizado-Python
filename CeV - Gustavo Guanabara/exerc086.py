# crie um programa que leia uma matriz 3 x 3 e preencha com valores lidos no teclado,
# no final mostre a matriz na tela com a formatação correta.
llista = []
clista = []
c = 0
print("EXERC086 - CRIAR A MATRIZ")
for c in range(0,3):
    for d in range (0,3):
        llista.append(int(input(f"Digite um valor para ({c},{d}): ")))
        #print(llista)
        d +=1
    #print()
    clista.append(llista[:])
    llista.clear()
    c +=1

#print(clista)

for lin in range(0,3):
    for col in range (0,3):
        print(f"[ {clista[lin][col]:^5} ]", end =" ")
    print()

#print(f"\n{clista[0]}\n{clista[1]}\n{clista[2]}")