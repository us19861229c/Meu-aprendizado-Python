#crie um programa que leia um valor (metro) e converta para centímetros (cm) e milimetro (mm)

metro = float(input("Digite o valor em metros: "))

print(f"o valor em metros é {metro} m, sua correspondencia em centímetros é {metro * 100} cm, e sua correspondencia em milimetros é {metro * 1000} mm")
print(f" TABELA DE KM HM DAM M DM CM MM \n>>> {metro / 1000} KM; \n>>> {metro / 100} HM;\n>>> {metro / 10} DAM;\n>>> {metro} M;"
      f"\n>>> {metro * 10:0f} DM;\n>>> {metro * 100:0f} CM;\n>>> {metro * 1000:.0f} MM")

