# crie um programa onde o usuario possa digitar varios valores (perguntar se ele deseja continuar);
# cadastre esses numeros numa lista ; caso o numero já exista ele nao será adicionado
#  mostrar todos os valores unicos digitados em ordem crescente

valores = []

while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor já adicionado.")
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print(valores)
valores.sort()
print(f"Os valores em ordem crescente: {valores}")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente: {valores}")