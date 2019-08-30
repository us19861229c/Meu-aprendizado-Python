#perguntar quanto quer sacar (inteiro), informar quantas cedulas de cada valor
# cedulas 50, 20, 10 e 1 .

print("="*20)
print("BANCO DO POVO")
print("="*20)

saque = int(input("Qual valor deseja sacar? R$"))
u = saque // 1 % 10
print(u)
d = saque // 10 % 10
print(d)
c = saque // 100 % 10
print(c)
cedula1 = 1
cedula2 = 10
cedula3 = 20
cedula4 = 50
if u < 10:
    u = u * cedula1
if d

