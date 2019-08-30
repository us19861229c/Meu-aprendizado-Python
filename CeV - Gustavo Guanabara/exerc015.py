#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado.
#DIARIA R$60 , R$ 0,15 p KM rodado

diaria = int(input("Digite a quantidade de dias de uso do veículo : "))
kmr = float(input("Digite o numero de km rodados: "))

usodia = diaria * 60
usokmr = kmr * 0.15

pagamento = usodia + usokmr

print(f" O veículo foi alugado por {diaria} dias e registrou o uso por {kmr:.1f} Km, "
      f"\n O valor total a pagar é R${pagamento:.2f}")