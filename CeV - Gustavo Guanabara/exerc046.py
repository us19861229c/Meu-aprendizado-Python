#programa que mostra a contagem regressiva (10 a 0) com pausa de 1 segundo entre os numeros
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("Feliz Ano Novo!!!")