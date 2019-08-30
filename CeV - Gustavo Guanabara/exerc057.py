# leia o sexo, aceitando apenas M ou F,
#em caso de erro solicitar a digitação novamente até o valor correto

sexo = str(input("Digite o seu sexo [F/M]: ")).strip().upper()[0]
while sexo not in "FfMm":
        sexo = str(input("Dado inválido.\nDigite o seu sexo [F/M]: ")).strip().upper()[0]
print("Agradecemos a participação")

sexo = str(input("Digite o seu sexo [F/M]: ")).strip().upper()[0]
print(sexo)
while sexo != "M" and sexo != "F":
        sexo = str(input("Dado inválido. \n Digite o seu sexo [F/M]: ")).strip().upper()[0]
        print(sexo)
print(f"Sexo {sexo} registrado com sucesso.")
print("Agradecemos sua participação")
