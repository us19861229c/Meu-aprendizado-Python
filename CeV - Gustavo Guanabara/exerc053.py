palavra = str(input("Digite uma palvra: ")).upper().strip().split()
print(palavra)
nfrase = "".join(palavra)

print(nfrase)
print(nfrase[::-1])
if nfrase == nfrase[::-1]:
    print("Essa frase é um palíndromo")
else:
    print("Essa palavra não é um palíndromo")