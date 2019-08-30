
soma = cont = 0


while True:
    num = int(input("Digite um valor qualquer: "))
    if num == 999:
        break
    cont += 1
    soma += num

print(f"Foram digitados {cont} valores e o valor da soma entre eles é {soma}")