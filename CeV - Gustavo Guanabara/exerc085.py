# crie um programa onde o usuario possa digitar sete valores numericos ,
# cadastre-os em uma lista única que mantenha separados os valores pares e impares,
# mostre os valores pares e impares em ordem crescente.
usuario = []
mlista = []
par = []
impar = []
c = 0
print("EXERC 085 - DIGITE SETE VALORES E CADASTRE NUMA LISTA UNICA"
      "\nDEPOIS MOSTRE A LISTA DOS VALORES PARES E IMPARES\nEM ORDEM CRESCENTE\n")
while c < 7:
    n = int(input(f"Digite {c+1}o. valor: "))
    if n % 2 == 0:
     par.append(n)
    else:
     impar.append(n)
    c += 1
mlista.append(par)
mlista.append(impar)
print("-"*30)
print(f"Lista de todos os valores: {mlista}")
print(f"Lista dos valores pares: {par}\nLista dos valores impares: {impar}")
par.sort()
impar.sort()
print(f"Listas em ordem crescente: \nPAR: {par}\nIMPAR: {impar}")