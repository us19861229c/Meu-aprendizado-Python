#programa que leia dos valores inteiros e os compare;
# se a > b , se b > a ou se b = a .
from time import sleep
print("Qual é o maior valor!?")
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

if a > b :
    print(f"o PRIMEIR valor é maior {b}")
elif b > a:
    print(f"o SEGUNDO valor é maior {a}")
else:
    print("os dois valores são iguais!")
    sleep(0.5)
    print("pare com isso . Jogue direito ¬_¬' ")