núm = [[],[]]
valor = 0
print("EXERC 085b - PROFESSOR:")
for c in range(1,8):
    valor = int(input(f"Digite o {c}o. valor:"))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f"Os valores pares digitados foram : {núm[0]}")
print(f"Os valores impares digitados foram : {núm[1]}")