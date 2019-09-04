# criar um programa que leia o nome, o ano de nascimento e a carteira de trabalho e
# realize um cadastro (com idade) em um diciinario e se a CTPS for diferente de 0
# o dicionario recebe tambem o ano de contratção e o salario. Tambem calcular com quantos
# anos a pessoa vai se aposentar
# aposentar depois de 35 anos de contribuição
'''
=- Ler dados -=
Nome: Gustavo
Ano de Nascimento: 1978
Carteira de trabalh (0 se não tiver): 1234
Ano de contratação: 1995
Salario R$: 1000
-= Tempo para resposta =-
Print no dicionario
{'chave' : 'valor', 'chave': 'valor}
for k,v in dicionario:
  print(f' {k} tem o valor {v}')
'''
# na resolução do exercicio: from datetime import datetime >>datetime.now().year
from datetime import date
inf = {}
anoatual = date.today().year
apose = 0

print("EXERC091 - CADASTRO NOME IDADE TRABALHA APOSENTADORIA ")
inf['nome'] = str(input("Nome: ")).strip()
anonasc = int(input("Ano de nascimento: "))
inf['idade'] = anoatual - anonasc
inf['ctps'] = int(input("Carteira de trabalho (0 se não houver): "))
if inf['ctps'] != 0:
    inf['contratação'] = int(input("Ano de contratação: "))
    inf['salário'] = float(input("Salário: R$"))
    apose = (inf['contratação'] - anonasc) + 35
    inf['aposentadoria'] = apose
print("-="*20)
print("DADOS DO SOLICITANTE:")
for k, v in inf.items():
    print(f">>{k} tem o valor {v}")
