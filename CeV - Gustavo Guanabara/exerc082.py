# ler varios numeros (quer continuar s/n),
# tres listas: todos os valores, só os pares e só os impares

valores1 = []
valorespar = []
valoresimpar = []
while True:
    numero = int(input("Digite um valor: "))
    valores1.append(numero)
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print(f"A lista : {valores1}")
for v in valores1:
    if v % 2 == 0:
        valorespar.append(v)
    else:
        valoresimpar.append(v)
print(f"Lista dos pares : {valorespar}")
print(f"Lista dos impares: {valoresimpar}")