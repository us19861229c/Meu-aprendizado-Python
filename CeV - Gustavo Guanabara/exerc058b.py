import random
from time import sleep

print("-="*15)
print("Jogo de adivinhação")
print("-="*15)
print("--- Adivinhe o numero que o computador está pensando ---")
pcn = random.randint(1,10)
n = int(input("Escolha um numero de 1 a 10: "))
palpites = 1
while n != pcn:
    print("Você errou!", end=" ")
    if n > pcn:
        print("Tente um número\033[34m mais baixo...\033[m")
    else:
        print("Tente um numero\033[31m mais alto... \033[m")
    n = int(input("Escolha outro numero de 1 a 10: "))
    palpites += 1
print(f"Você acertou em \033[32m{palpites} tentativa(s)!\033[m Parabéns!")
print("fim de jogo!")