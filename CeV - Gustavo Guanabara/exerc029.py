#029: escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km, será multado em 7 reais cada km extra.

vel = float(input("Qual a velocidade do seu carro? "))

if vel > 80:
    multa = (vel - 80) * 7
    print(f"Você estava acima do limite de velocidade!\n"
          f"Sua multa será de R${multa:.2f}")
print("Tenha um bom dia!")