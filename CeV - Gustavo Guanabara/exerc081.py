# ler varios numeros e colocar numa lista (ques continuar SN);
# quantos numeros digitados;  lista ordenada decrescente ; se o valor 5 está ou n na lista

valores = []
qnum = 0
while True:
    numero = int(input("Digite um valor: "))
    qnum += 1
    valores.append(numero)
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print(f"Foram digitados {qnum} valores")
if 5 in valores:
    print(f"O numero 5 está na posição {valores.index(5)}")
else:
    print(f"O numero 5 não está na lista.")
valores.sort(reverse=True)
print(f"Lista em ordem decrescente : {valores}")
