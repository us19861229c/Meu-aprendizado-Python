#elaborar um programa que calcule o valor a ser pago por um produto;
#preço normal e a condição de pagamento
# A vista dinheiro 10% de desconto; a vista cartao 5% de desconto; 2x cartao preço normal;
# 3x ou mais , +20% no preço do produto

produto = float(input("QUal o valor do produto que deseja levar? R$"))
formadpgto = int(input("Escolha a forma de pagamento: \n"
                       "[1] À vista em dinheiro (10% de desconto):\n"
                       "[2] À vista no cartão (5% de desconto):\n"
                       "[3] 2x no cartão (preço normal): \n"
                       "[4] 3x ou + no cartão (acréscimo de 20%):\n  "))
if formadpgto == 1:
    prec = produto - (produto * 0.10)
    print(f"O valor final do seu produto é R${prec:.2f}")

elif formadpgto == 2:
    prec = produto - (produto * 0.05)
    print(f"O valor final do seu produto é R${prec:.2f}")

elif formadpgto == 3:
    print(f"o valor do seu  produto é R${produto:.2f}")
elif formadpgto == 4:
    parcelas = int(input("Em quantas parcelas deseja dividir? "))
    prec = produto + (produto * 0.20)
    print(f"o valor final do seu produto é R${prec:.2f} dividido em {parcelas} vezes: "
          f"R${prec/parcelas:.2f}")
else:
    print("Opção inválida!")

print("obrigada por comprar na nossa loja")