# sequencia de fibonacci

print("seuqencia de fibonacci")

'''
      a   b   a+b 
1      1   1   2
2      1   2   3
3      2   3   5
4      3   5   8
5      5   8   13
'''
'''n = int(input("N:"))
fb1, fb2 = 1, 1
cont = 1
while cont <= n - 2:
      fb1, fb2 = fb2, fb1 + fb2
      cont = cont + 1

print(f"\nFIB({n}) = {fb2}")'''

fnat = int(input("Digite um numero: "))
contador = 2
t1 = 0
t2 = 1
print(f"{t1}-> {t2}-> ", end="")
while contador <= fnat:
      t3 = t1 + t2
      print(t3, end="-> ")
      t1 = t2
      t2 = t3
      contador += 1
print("Fim!")
print(f"\nFIB({fnat}) = {t2}")