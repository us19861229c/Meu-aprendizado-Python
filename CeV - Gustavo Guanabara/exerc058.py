import random
from time import sleep
print("--- Adivinhe o numero que o computador está pensando! ---\n ")
numero = int(input("Escolha um numero entre 0 e 5: "))
pcn = random.randint(0,5)
print("PROCESSANDO...")
sleep(1)
palpites = 1
while numero != pcn:
    print(f"O numero escolhido por você foi {numero}\n"
          f"O numero escolhido pelo computador foi {pcn}\n"
          f"Esses numeros são diferentes! Que pena! Você errou!")
    palpites += 1
    numero = int(input("Escolha um numero entre 0 e 5: "))
    pcn = random.randint(0, 5)
    print("PROCESSANDO...")
    sleep(1)

if numero == pcn:
    print(f"O numero escolhido por você foi {numero}\n"
          f"O numero escolhido pelo computador foi {pcn}\n"
          f"Esses numeros são iguais! Parabéns! Você acertou em {palpites} palpites!")

print("Obrigada por participar de nosso jogo!")