#analisar o peso de cinco pessoas d indicar o maior e o menor pesos lidos

maiorpeso = 0
menorpeso = 0
for pessoa in range(1, 5+1):
    peso = float(input(f"Peso da {pessoa}a. pessoa: "))
    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso


print(f"O maior peso foi {maiorpeso}kg e o menor peso foi {menorpeso}kg")
