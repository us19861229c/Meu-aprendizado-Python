#crie um programa que leia quanto dinheiro  uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

dreal = float(input("Quantos reais você possui? R$"))
ddolar = dreal / 3.27

print(f"Com R${dreal:2f}, você pode comprar U${ddolar:2f} ")