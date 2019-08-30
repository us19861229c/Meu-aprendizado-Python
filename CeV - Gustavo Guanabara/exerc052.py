#leia um numero e diga se ele é primo ou nao
print("É PRIMO OU NAO É?")
numero = int(input("Digite um numero: "))
tot = 0
for c in range (1, numero+1):

    if numero % c == 0:
        print('\033[34m', end = " ")
        tot += 1
    else:
        print('\033[31m', end = " ")
    print(f"{c}", end=" ")

if tot == 2:
    print("\033[m\nEsse numero é primo")
elif tot >= 3:
    print("\033[m\nEsse numero não é primo")

