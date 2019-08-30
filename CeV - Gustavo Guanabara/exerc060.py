#leia um numero e faça o fatorial

n = int(input("Digite um numero para saber seu fatorial: "))
fat = 1
nfat = n
while nfat >= 1:
    fat = fat * nfat
    print(f"{nfat}", end="")
    print("x " if nfat > 1 else "= ", end="")
    nfat -= 1
print(f"{fat}")
print(f"{n}! = {fat}")

fato = 1
valori = int(input("Digite um numero para saber o seu fatorial: "))
valor = valori
for v in range(valor, 0, -1):
    fato = fato * valor
    print(f"{valor}", end="")
    print("x" if valor > 1 else "= ", end=" ")
    valor -= 1
print(f"{fato}")
print(f"{valori}! = {fato}")