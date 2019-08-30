from random import randint
randnum = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print("valores sorteados: ", end="")
for numeros in randnum :
    print(f"{numeros}", end=", ")
print(f"\nO maior numero foi {max(randnum)}\nE o menor foi {min(randnum)}")

