# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta,
# no final mostre um boletim contendo a media de cada aluno
cadastro =[]
listaalunnotamedia =[]
notas = []
while True:
    cadastro.append(str(input("Nome do Aluno: ")).strip().capitalize())
    listaalunnotamedia.append(cadastro[:])
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))
    listaalunnotamedia.append(notas[:])
    media = (notas[0] + notas[1])/2
    print(">>",media)
    print(">>",notas)
    print((">>",cadastro))
    print(">>",listaalunnotamedia)
    cadastro.clear()
    notas.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar cadastrando? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("="*30)
print("teste 2")
print(f"{notas}") # zerado
print(f">>{cadastro}") #zerado
print(f">>>>{listaalunnotamedia}")