# ler duas notas de um aluno e calcular sua media;
# se m < 5 : reprovado ; 5 =< m =< 6.9 : recuperação ; m > 7 : aprovado

print("=-="*10)
print("B O L E T I M")
print("=-="*10)
nome = str(input("Nome do Aluno: ")).strip()
n1 = float(input("Nota 01:"))
n2 = float(input("Nota 02:"))
m = (n1+n2)/2

if m < 5:
    print(f"{nome}: Infelizmente você foi reprovado")
elif m >= 7:
    print(f"Parabéns, {nome}! Você foi aprovado(a)")
else:
    print(f"{nome}: Você está apto(a) para recuperação")
