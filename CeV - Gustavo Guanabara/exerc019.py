import random
alun1 = input("nome do 1o. aluno: ")
alun2 = input("nome do 2o. aluno: ")
alun3 = input("nome do 3o. aluno: ")
alun4 = input("nome do 4o. aluno: ")

sorteio = [alun1, alun2, alun3, alun4]
escolhido = random.choice(sorteio)

print(f"o aluno escolhido foi {escolhido}")

