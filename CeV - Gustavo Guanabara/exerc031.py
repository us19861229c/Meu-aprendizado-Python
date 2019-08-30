#031 programa que leia a distancia de uma viagem e calcule o custo
# 0.50 por km até 200 km; mais de 200km , 0.45 por km

distancia = int(input("Qual a distância percorrida em Km para realizar sua viagem? "))

if distancia < 200:
    custo = distancia * 0.50
    print(f"A sua viagem será de {distancia}km. "
          f"O custo da viagem é de R${custo:.2f}.")
else:
    custo = distancia * 0.45
    print(f"A sua viagem será de {distancia}km. "
          f"O custo da viagem será de R${custo:.2f}. ")