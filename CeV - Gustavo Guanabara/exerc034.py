#034 : programa para ler o salario do funcionario e dar um aumento percentual
# caso o salario seja maior q 1250, dar +10%
# para salario menor q 1250, dar 15%

sal = float(input("Qual o seu salario atual? R$"))

if sal > 1250.00 :
    nsal = sal  + (sal * 0.10)
    print(f'Seu salario antigo era R${sal:.2f}, '
          f'com o acréscimo de 10% seu salário atual é R${nsal:.2f}.')
else:
    nsal = sal + (sal * 0.15)
    print(f'Seu salário antigo era R${sal:.2f}, '
          f'com o acréscimo de 15%, seu salário atual é R${nsal:.2f}.')
