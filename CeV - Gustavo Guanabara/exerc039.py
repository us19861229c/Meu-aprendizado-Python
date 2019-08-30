# ler a idade de um jovem e determinar ;
# falta x anos para ele atingir a idade de se alistar;
# ele esta na idade de se alistar;
# já passaram x anos do alistamento;
import datetime
anoatual = datetime.date.today().year

anonasc = int(input("Digite o ano do seu nascimento (formato AAAA), ex.: 1986: "))

if anoatual - anonasc == 18:
    print("Você deve se alistar")
elif anoatual - anonasc > 18:
    atraso = (anoatual - anonasc) - 18
    print(f"É, tá barril, vc tá atrasado em {atraso} ano(s). Veja aí o que vc vai fazer, maluco")
else:
    falta = abs((anoatual - anonasc) - 18)
    print(f"Aproveite, vc ainda eh criança e falta(m) {falta} ano(s) pra vc.")
print("Valeu!")