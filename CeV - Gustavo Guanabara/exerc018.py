import math
angulo = float(input("Digite o ângulo desejado: "))
coss = math.cos(math.radians(angulo))
ssen = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f'O cosseno do angulo {angulo} é {coss:.2f}'
      f'\nO seno do angulo {angulo} é {ssen:.2f}'
      f'\nA Tangente do anguo {angulo} é {tang:.2f}')
print("-->>_<<"*35)

from math import radians, cos, sin, tan
ang = float(input("Digite o ângulo desejado: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tange = tan(radians(ang))

print(f">>O COSSENO de {ang} é {cosseno:.2f}"
      f"\n>>O SENO de {ang} é {seno:.2f}"
      f"\n>>A TANGENTE de {ang} é {tange:.2f}")