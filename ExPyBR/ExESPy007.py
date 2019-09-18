"""
7.Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.

"""

lado = float(input("Digite o tamanho do lado do quadrado em cm: "))
area = lado ** 2
print(f"A area do quadrado é {area:.2f}cm² e seu dobro é {2*area:.2f}cm²")
