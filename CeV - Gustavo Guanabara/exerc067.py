n2 = 1

while True:
    print("~<>"*16)
    n1 = int(input("Digite um valor para saber sua TABUADA: "))
    print("~<>"*16)
    if n1 < 0:
        break
    print(f"--- Tabuada de {n1} ---")
    while n2 <= 10:
        print(f">>{n1:>2} x {n2:>2} = {n1 * n2:>2}")
        n2 += 1
    n2 = 1
print("Programa encerrado")
print("Obrigada por participar")