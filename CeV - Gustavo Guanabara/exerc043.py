#calcular imc

print("Calcule o seu IMC")

nome = str(input("Qual o seu nome? ")).strip()
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso / (altura ** 2)

if imc < 16:
    print(f"{nome}: seu indice aponta magreza grave e pode causar insuficiência cardíaca, "
          f"\nanemia grave e enfraquecimento do sistema imunológico.")
elif 16 <= imc < 17:
    print(f"{nome}: seu indice aponta magreza moderada, o que pode levar à "
          f"\ninfertilidade, queda de cabelo")
elif 17 <= imc < 18.5:
    print(f"{nome}: seu indice aponta magreza leve, o que pode resultar em estresse, "
          f"\nansiedade e fadiga.")
elif 18.5 <= imc < 25:
    print(f"{nome}: seu indice é considerado saudável, apresentando menor risco para doenças.")
elif 25 <= imc < 30:
    print(f"{nome}: seu indice indica sobrepeso ")
elif 30 <= imc < 35:
    print(f"{nome}: aponta obesidade de grau I")
elif 35 <= imc < 40:
    print(f"{nome}: aponta obesidade grau II")
else:
    print(f"{nome}: aponta obesidade de grau III (mórbida),")
print("Para maiores orientações procure o seu médico.")