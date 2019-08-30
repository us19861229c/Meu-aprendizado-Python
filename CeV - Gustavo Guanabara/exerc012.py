#um algoritmo que leia o preço de u produto e mostre seu novo preço com 5% de desconto.

prod = float(input("Qual o valor do produto? R$"))

nprod = prod - (prod * 0.05)

print(f"o produto custava R${prod:.2f} , e com 5% de desconto passou a ser R${nprod:.2f}")

#salario do funcionario com 15% de aumento

sal = float(input("Qual o seu salário?R$"))

nsal = sal + (sal * 0.15)

print(f"o salario antigo era R${sal:.2f}, mas com 15% de a créscimo ficou R${nsal:.2f}")