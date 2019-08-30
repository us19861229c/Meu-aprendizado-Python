#tupla de zero a vinte (por extenso), usuario escolhe um numero e ele será escrito
#ppor extenso

numero = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
          "oito", "nove", "dez")
cont=""
while cont not in range(0,10+1):
    cont = int(input("Digite um numero entre 0 e 10: "))
print("o numero digitado foi ", numero[cont])
