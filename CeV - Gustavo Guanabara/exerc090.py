# programa que leia nome e média de um aluno, guardando também a situação em um dicionário (aprovado, reprovado ou recuperação)
# mostrar no final o conteúdo na tela
'''
=- Leitura dos dados -=
Nome: Joaquim
Média do {Joaquim}:  4.5
-= Tempo para a resposta =-
>>nome é igual a Joaquim
>>média é igual a 4.5
>>situação é igual a reprovado
# nome, media e situação são chaves
#Joaquim, 4.5 e reprovado/aprovado são valores
#valor reprovado ou aprovado é condicional verificado após média
'''
from time import sleep
aluno = {}

print("EXERC 090 - BOLETIM DO ALUNO")
print("-"*30)
aluno['Nome'] = str(input("NOME: ")).upper()
aluno['Média'] = float(input(f"MÉDIA DE {aluno['Nome']}: "))

if aluno['Média'] >= 7:
    aluno['Situação'] = "Aprovado"
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = "Recuperação"
else:
    aluno['Situação'] = "Reprovado"
print("-"*30)
print(f"BOLETIM DE {aluno['Nome']}")
print("-"*30)
sleep(0.3)
for k, v in aluno.items():
    print(f"  >>{k} é igual a {v}")

print("\n>>Agradecemos a consulta.")