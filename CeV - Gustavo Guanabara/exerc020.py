import random
a1 = input("Digite o nome do 1o. aluno: ")
a2 = input("Digite o nome do 2o. aluno: ")
a3 = input("DIgite o nome do 3o. aluno: ")
a4 = input("Digite o nome do 4o. aluno: ")
ordem = [a1, a2, a3, a4]

print(f"Os alunos que apresentarão os trabalhos são:"
      f"\n- {a1} \n- {a2} \n- {a3} \n- {a4}")
random.shuffle(ordem)
print("-->><<"*21)
print(f"a ordem de apresentação dos trabalhos será: "
      f"\n - {ordem}")

from random import  shuffle
ordem = [a1, a2, a3, a4]

print(f"Os alunos que apresentarão os trabalhos são:"
      f"\n- {a1} \n- {a2} \n- {a3} \n- {a4}")
shuffle(ordem)
print("-->><<"*21)
print(f"a ordem de apresentação dos trabalhos será: "
      f"\n - {ordem}")
