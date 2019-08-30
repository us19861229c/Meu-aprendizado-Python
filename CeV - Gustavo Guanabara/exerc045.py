#jokenpo
import random
import time
jokenpo = ["Pedra", "Papel", "Tesoura"]
pcjoke = random.choice(jokenpo)
print("CAMPEONATO DE JOKENPO")
print("HOMEM x MAQUINA!")
print("Escolha sua arma: \n")

escolha = int(input("[1] Pedra , [2] Papel , [3] Tesoura: "))
time.sleep(0.3)
print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PO!")
time.sleep(0.3)
if escolha == 1:
    if pcjoke == jokenpo[0]:
        print("Você escolheu Pedra,\nO computador escolheu Pedra!")
        print("Houve um empate!")
    elif pcjoke == jokenpo[1]:
        print("Você escolheu Pedra,\nO computador escolheu Papel")
        print("O computador venceu!")
    else:
        print("Você escolheu Pedra,\nO computador escolheu Tesoura")
        print("Você venceu!")
elif escolha == 2:
    if pcjoke == jokenpo[0]:
        print("Você escolheu Papel,\nO computador escolheu Pedra")
        print("Você venceu!")
    elif pcjoke == jokenpo[1]:
        print("Você escolheu Papel,\nO computador escolheu Papel")
        print("Houve um empate!")
    else:
        print("Você escolheu Papel,\nO computador escolheu Tesoura")
        print("O computador venceu")
elif escolha == 3 :
    if pcjoke == jokenpo[0]:
        print("Você escolheu Tesoura,\nO computador escolheu Pedra")
        print("O computador venceu!")
    elif pcjoke == jokenpo[1]:
        print("Você escolheu Tesoura,\nO computador escolheu Papel")
        print("Você Venceu!")
    else:
        print("Você escolheu Tesoura,\nO computador escolheu Tesoura")
        print("Houve um empate")
else:
    print("Opção inválida. Tente novamente")

print("Obrigada por participar de nosso jogo")