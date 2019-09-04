# Crie um programa que leia nome, sexo e idade de varias pessoas (quer continuar S/N?) , guardando os dados num dicionario
# e todos os dicionarios numa list() [lista.append(dicionario.copy()). No final mostrar:
# Quantas pessoas foram cadastradas -len(list)- ; a media de idade do grupo ; uma lista com todas as mulheres,
# uma lista com todas as pessoas ( e seus dados) que têm idade acima da media

'''
-= Leia dados =-
Nome: Gustavo
Sexo [M/F] (repetir caso o valor not in FM) : M
Idade: 40
Quer continuar [S/N] (idem MF)?
(...)
- o grupo tem {len(list())} pessoas
- A media de idade é {somaidade/len(list())
- As mulheres cadastradas foram Fulana e Fulana (listamulheres)
- Lista das pessoas com idade acima da media:

<<encerra>>
'''

cadastro = []
pessoas = {}
somaidade = 0
listamulheres = []
listaacimamedia = []
print("EXERC094 - LER NOME, SEXO E IDADE, CADASTRAR E ANALISAR")
print("-" * 30)
print("DADOS CADASTRAIS")
print("-" * 30)
while True:
    pessoas['nome'] = str(input("NOME: ")).strip()
    pessoas['sexo'] = str(input("SEXO [F/M]: ")).strip().upper()[0]
    while pessoas['sexo'] not in "FM":
        pessoas['sexo'] = str(input("Erro. Digite apenas M ou F.\nSEXO [F/M]: ")).strip().upper()[0]
    if pessoas['sexo'] == 'F':
        listamulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input("IDADE: "))
    somaidade += pessoas['idade']
    cadastro.append(pessoas.copy())
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("Erro. Digite apenas S ou N.\nDeseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
mediaidade = somaidade/len(cadastro)

print(cadastro)
print(f"A)O grupo tem {len(cadastro)} pessoas cadastradas")
print(f"B)A média de idade é {mediaidade:.2f}")
print(f"C)As mulheres cadastradas foram {listamulheres}")
for k in cadastro:
    if k['idade'] > mediaidade:
        listaacimamedia.append(k)
print("D) A lista de pessoas com idade acima da média é:")
for e in listaacimamedia:
    for k, v in e.items():
        print(f"{k} = {v};", end=" ")
    print()
print("<<ENCERRADO>>")
