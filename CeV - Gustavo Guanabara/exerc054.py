# ler o ano de nascimento de sete pessoas;
# quem atingiu a maioridade e quem nao

from datetime import date
anoa = date.today().year
maioridade = 0
abaixomaior = 0
for pessoa in range(1, 7+1):
    anon = int(input(f"Qual o ano do nascimento da {pessoa}a. pessoa? "))
    idade = anoa - anon
    if idade >= 21:
        maioridade += 1
    else:
        abaixomaior += 1



print(f"{maioridade} pessoas já atingiram a maioridade", end="")
print(f" e {abaixomaior} pessoas não atingiram")