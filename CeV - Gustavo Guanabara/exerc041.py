#ler o ano de nascimento do atleta e sua categoria de acordo com a idade;
# ate 9 anos : mirim;  ate 14: infantil; ate 19: junior; ate 20: senior; +20: master

import datetime
anoatual = datetime.date.today().year
anonasc = int(input("Digite o ano de nascimento (AAAA). Ex. 1986: "))
idade = anoatual - anonasc

if idade > 25:
    print("sua categoria é MASTER")
elif idade <= 9:
    print("sua categoria é MIRIM")
elif idade <= 14:
    print("sua categoria é INFANTIL")
elif idade <= 19:
    print("sua cateforia é JUNIOR")
elif idade <= 25:
    print("sua categoria é SENIOR")