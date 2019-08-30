#leia idade e sexo de varias pessoas; perguntar se quer continuar S/N;
# - qnts pessoas +18 ; - qnts homens; - qnts mulheres <20:
qntidade = 0
qnthomem = 0
qntmulher = 0
qntpessoas = 0
print("-"*20)
print(" C A D A S T R O  DE  P E S S O A S")
print("-"*20)
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F/M]: ")).strip().upper()[0]
    while sexo not in "FM":
        sexo = str(input("Sexo [F/M]: ")).strip().upper()[0]
    qntpessoas += 1
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if idade > 18:
        qntidade += 1
    if sexo == "M":
        qnthomem += 1
    if sexo == "F" and idade < 20:
        qntmulher += 1
    if resp != "S":
        break
print("--- Cadastros ---")
print(f"\n>>Foram cadastradas {qntpessoas} pessoas"
      f"\n>>Foram cadastradas {qntidade} pessoas maiores de 18 anos"
      f"\n>>Foram cadastrados {qnthomem} homens"
      f"\n>>Foram cadastradas {qntmulher} mulheres abaixo de 20 anos")