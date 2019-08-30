#ler valores, fazer a media entre eles, maior e menor

cont = 0
soma = 0
maiorn = 0
resp = 'S'

while resp == 'S':
    numero = int(input("Digite um valor: "))
    cont += 1
    soma = soma + numero
    if cont == 1 :
        menorn = numero
        maiorn = numero
    else:
        if numero > maiorn:
            maiorn = numero
        if numero < menorn:
            menorn = numero
    resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
print("Processando...")
print(f">>Você digitou {cont} valores,\n>>O maior deles foi {maiorn}\n>>O menor foi {menorn}"
      f"\n>>A media é {soma/cont}")