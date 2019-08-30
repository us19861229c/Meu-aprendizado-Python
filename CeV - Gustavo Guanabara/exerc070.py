#programa que leia nome e preço de produtos; usuario decide quando parar
# mostrar: - total da compra;  quantos produtos >1000,00 ; nome do produto mais barato
totalcompra = topcaros = baratinho = compra = 0
nbaratinho = ""
print("~><~   "*5)
print("LOJA PRA PESSOA COMPRAR COISAS VARIADAS")
print("~><~   "*5)

print("SACOLA DE COMPRAS:")
while True:
    produto = str(input("Nome do produto:"))
    preço = float(input("Preço: R$"))
    totalcompra += preço
    compra += 1
    if preço > 1000:
        topcaros += 1
    if compra == 1 or preço < baratinho:
        baratinho = preço
        nbaratinho = produto
    #else:
    #    if preço < baratinho:
    #        baratinho = preço
    #        nbaratinho = produto
    resp = str(input("Deseja continuar comprando? [S/N] ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("Inválido. Deseja continuar comprando? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("-"*20)
print(f">>O valor total da compra foi R${totalcompra:.2f}"
      f"\n>>Foram comprados {topcaros} produtos acima de R$1000.00"
      f"\n>>O produto mais barato registrado foi {nbaratinho}, que custa R${baratinho}")