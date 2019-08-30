print("Gerador de PA")
i = int(input("Digite o termo: "))
p = int(input("Digite a razão: "))
termo = i
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{cont}o. Termo: {termo}...", end="")
        termo += p
        cont += 1
    print('Espera')
    mais = int(input("Quantos termos mais? "))
print(f"Foram solicitados {total} termos.")