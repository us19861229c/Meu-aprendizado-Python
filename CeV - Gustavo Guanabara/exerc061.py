print("Gerador de PA:")
i = int(input("Digite o valor desejado: "))
p = int(input("Digite a razão: "))
c = 1

while c <= 10:
    print(f"{c:>2}o. Termo: {i:>2}", end="...")
    i += p
    c += 1
print("\nFim")

