# ler o nome, a idade e o sexo de 4 pessoas;
# 1- a media de idade do grupo (media/4) ; 2- qual nome do homem mais velho;
# 3- quantas mulheres têm menos de 20 anos
idademaior = 0
idadetot = 0
idademulher = 0
for pessoas in range(1,4+1):
    nome = str(input("Qual o seu nome? "))
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("[F/M] ? ")).strip().upper()
    idadetot += idade
    if idade > idademaior and sexo == "M":
        idademaior = idade
        nomemaior = nome
    if idade < 20 and sexo == "F":
        idademulher += 1

print(f"A média de idade do grupo é \033[34m{idadetot/4}")
print(f"\033[mO nome do homem mais velho é : \033[31m{nomemaior}\033[m, com a idade de {idademaior} anos ")
print(f"O grupo tem \033[33m{idademulher}\033[m mulheres abaixo de 20 anos")