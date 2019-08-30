# faça um programa que leia a LARGURA (larg) e a ALTURA (altu) dde uma parede em metros, calcule sua área [ LARGURA x ALTURA] {area),
# e a quantidade necessárioa de tinta, sabendo que um galao de tinta pinta dois metros.

larg = float(input("qual a largura da parede? "))
altu = float(input("qual a altura da parede? "))
area = larg * altu
tottinta = area/2

#if tottinta > 1:
 #   res = "galões de tinta"
#else:
 #   res = "galão de tinta"

print(f"A parede em questao mede {larg:.2} metro(s) de largura e {altu:.2} metro(s) de altura, \npossui uma area de {area:.2} m²", end= " e ")
print(f"para pintá-la será necessária a compra de {tottinta}l litro(s) de tinta")

