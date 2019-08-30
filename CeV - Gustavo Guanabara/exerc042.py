print("--- TRIANGULO ---")
a = int(input("Digite o 1o. valor: "))
b = int(input("Digite o 2o. valor: "))
c = int(input("Digite o 3o. valor: "))

if a < b + c and b < a + c and c < a + b:
    print("Esses valores podem formar um triângulo", end="")
    if a == b == c :
        print (" e esse triangulo é equilátero.")
    elif a != b != c != a:
        print(" e esse triângulo é escaleno.")
    else:
        print (" e esse triângulo é isósceles.")
else:
    print("Esses valores não podem formar um triângulo")
print("Obrigada por participar")