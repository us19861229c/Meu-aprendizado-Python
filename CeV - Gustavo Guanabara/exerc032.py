#031: descobrir se o ano é ou nao bissexto
from datetime import date
print("--- DESCUBRA SE O ANO É BISSEXTO! ---")
anobi = int(input("Digite o ano desejado no formato AAAA (ex.: 1992)"
                  "ou se quiser o ano atual, digite 0:"))
if anobi == 0:
    anobi = date.today().year

if anobi % 4 == 0 and anobi % 100 != 0 or anobi % 400 == 0:
    print(f"O ano {anobi} é bissexto!")
else:
    print(f"O ano {anobi} não é bissexto!")
