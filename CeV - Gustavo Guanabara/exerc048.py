#a soma de numeros impares ; multiplos de três, intervalo de 1 a 500

soma = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
print(soma)

