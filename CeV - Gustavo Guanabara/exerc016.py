#programa que leia um numero real qualquer e mostre na rela a sua porção inteira
from math import trunc

numr = float(input("digite um numero real qualquer: "))

print(f"O numero digitado foi {numr} e sua parte inteira "
      f"é {trunc(numr)}")

print(f"O numero digitado foi {numr} e sua parte inteira "
      f"é {int(numr)}")

print(f"O numero digitado foi {numr} e sua parte inteira "
      f"é {numr:.0f}")