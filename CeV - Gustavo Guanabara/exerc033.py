#033: ler tres numeros e dizer qual o maior e qual o menor:
print("Digite 3 numeros:")
maiorn = 0

n = int(input("Numero 1: "))
if n > maiorn:
    maiorn = n
    menorn = n
n = int(input("Numero 2: "))
if n > maiorn:
    maiorn = n
if n < menorn:
    menorn = n
n = int(input("Numero 3: "))
if n > maiorn:
    maiorn = n
if n < menorn:
    menorn = n
print(f"o maior numero foi {maiorn} e o menor foi {menorn}")
