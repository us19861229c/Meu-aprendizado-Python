# ler o primeiro termo e ler a razao, fazer uma PA de 10 termos

i = int(input("Digite o valor desejado: "))
p = int(input("Digite a razão da soma: "))

for c in range(1, 10+1):
    print(i, end=" -> ")
    i = i + p
print("Acabou!")
