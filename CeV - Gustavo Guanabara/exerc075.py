#ler quatro valores, guardar em tuplas

núm = (int(input(f"Digite o valor:")),
       int(input(f"Digite o valor:")),
       int(input(f"Digite o valor:")),
       int(input(f"Digite o valor:")))
print(f"Você digitou os valores: {núm}")
print(f"O número nove apareceu {núm.count(9)} vezes.")
if 3 in núm:
    print(f"O número três apareceu na {núm.index(3) +1}ª posição.")
else:
    print("O número três não aparece em nenhuma posição")
print("O valores pares digitados foram: ", end="")
for n in núm:
    if n % 2 == 0:
        print(n, end=" ")