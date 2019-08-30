# ler seis numeros inteiros, somar os pares apenas
soma = 0
for c in range(1, 6+1):
    n = int(input(f"Digite o {c}o. valor: "))
    if n % 2 == 0:
        soma += n
    else:
        print(f"EI! esse valor({n}) não entra na soma!")
print(f"A soma é {soma}")