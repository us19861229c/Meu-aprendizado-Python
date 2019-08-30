# tabuada simplificada

for n1 in range(1,10+1):
    print("-="*8)
    print(f"Tabuada do {n1}:")
    for n2 in range(1, 10+1):
        print(f"{n1:>2} x {n2:>2} =  {n1 * n2:>3}")

n = int(input("Qual numero voce deseja ver a tabuada? "))
for cont in range(1,10+1):
    print(f"{n} x {cont:>2} = {n * cont:>2}")
