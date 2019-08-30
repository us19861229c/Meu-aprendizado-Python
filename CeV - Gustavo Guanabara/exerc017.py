#Programa que leia o cateto oposto e o adjacente de um triangulo retangulo
#e mostre o comprimento da hipotenusa

cat_o = float(input("comprimento do cateto oposto: "))
cat_a = float(input("comprimento do cateto adjacente: "))

c_hip = (cat_o ** 2 + cat_a ** 2) ** (1/2)

print(f" A hipotenusa mede {c_hip:.2f}")

import math
ca = float(input("Comprimento do cateto adjacente: "))
co = float(input("Comprimento do cateto oposto: "))

hipt = math.hypot(ca, co)

print(f"A hipotenusa mede {hipt:.2f}")