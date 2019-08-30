#programa para aprovar o emprestimo bancario para a compra de uma casa
#ler : >> valor da casa ; >> o salario do comprador ; >> quantos anos para pagar
# calcular o valor da prestação mensal ( prestacao = vcasa / anosppagar) ;
# se prestacao  > 30% de salario , nega o emprestimo ; senao, valida o emprestimo
from time import sleep
from math import ceil
print("-=-"*20)
print("  B  A  N  C  O  DO  P  O  V  O  ")
print("-=-"*20)
print("Empréstimo para casa nova\n")
print("-=-"*20)
print("Para obter seu empréstimo é necessário verificar alguns dados")
nome = str(input("Qual o seu nome? ")).strip()
vcasa = float(input("Qual o valor da casa que deseja comprar? R$"))
anosppagar = int(input("Em quantos anos deseja quitar o pagamento? "))
salario = float(input("Qual o seu salário? R$"))
print("-=-"*20)
print("Analisando....\nAguarde...")
sleep(0.8)

prestacao = vcasa/(anosppagar*12)
intprest = ceil(prestacao)
trintapsal = salario * 0.30
print("-=-"*20)
if intprest > trintapsal:
    print(f"Prezado(a) {nome},\nInfelizmente não podemos conceder o empréstimo para"
          f"a compra da sua nova casa.")
else:
    print(f"Prezado(a) {nome},\nParabéns! Nosso banco concederá o emprestimo para"
          f"a aquisição da sua casa nova!")
print("-=-"*20)
print("\nObrigada por escolher o nosso banco!")
