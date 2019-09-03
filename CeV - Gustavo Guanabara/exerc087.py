# Aprimore o desafio anterior mostrando no final:
# a) a soma dos valores pares digitados,
# b) a soma da terceira coluna, c) o maior valor da segunda linha.

llista = []
clista = []
soma = soma3c = soma2l = maiorn = 0
c = 0
print("EXERC087 - ANALISANDO A MATRIZ")
for c in range(0, 3):
    for l in range(0, 3):
        llista.append(int(input(f"Digite um valor para ({c},{l}): ")))
    for posi in llista:
        if posi % 2 == 0:
            soma += posi
    l += 1
    clista.append(llista[:])
    llista.clear()
    c += 1

for l in range(0, 3):
    soma3c += clista[l][2]
for valor in clista[1]:
    soma2l += valor
for c in range(0, 3):
    if c == 0 :
        maiorn = clista[1][c]
    elif clista[1][c] > maiorn:
        maiorn = clista[1][c]
print("-" * 30)
print("MATRIZ")
print("-" * 30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f"[ {clista[lin][col]:^5} ]", end=" ")
    print()

print()
print("-" * 30)
print("Somando valores:")
print("-" * 30)
print(f"Soma dos pares: {soma}")
print(f"Soma da 2 linha: {soma2l}")
print(f"Soma da 3 coluna: {soma3c}")
print(f"O maior valor da 2 linha é: {maiorn}")
