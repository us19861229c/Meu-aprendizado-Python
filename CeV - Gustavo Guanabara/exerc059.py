#ler dois valor e perguntar o q deseja fazer com eles ;
#[1] somar ; [2] multiplicar ; [3] maior ; [4] novos numeros; [5] sair
#incremento: invalidar caso nenhum dos numeros seja digitado.
from time import sleep
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
print('''escolha uma das opções abaixo
\033[32m[1]\033[m somar valores
\033[33m[2]\033[m multiplicar valores
\033[34m[3]\033[m qual o maior
\033[35m[4]\033[m alterar números
\033[36m[5]\033[m sair
''')
menu = int(input("Digite sua opção:"))

while menu != 5:
    if menu == 1:
        print("você escolheu \033[32m[1]\033[m somar valores: ")
        print(f">>{n1} + {n2} = {n1+n2}")
        print("-="*10)
        menu = ""
        menu = int(input("Digite sua opção: "))
    elif menu == 2:
        print("Você escolheu \033[33m[2]\033[m multiplicar valores: ")
        print(f">>{n1} x {n2} = {n1*n2}")
        print("-="*10)
        menu = ""
        menu = int(input("Digite a sua opção: "))
    elif menu == 3:
        print("Você escolheu \033[34m[3]\033[m qual o maior número: ")
        if n1 > n2:
            print("o primeiro valor é maior do que o segundo valor")
        elif n2 > n1:
            print("o segundo valor é maior do que o primeiro valor")
        else:
            print("os valores são iguais")
        print("-="*10)
        menu = ""
        menu = int(input("Digite a sua opção: "))
    elif menu == 4:
        print("você escolheu \033[35m[4]\033[m alterar os números:")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print("-="*10)
        menu = ""
        menu = int(input("Digite a sua opção: "))
    else:
        print("Você digitou uma \033[31mopção inválida\033[m. Tente novamente")
        print("-="*10)
        menu = ""
        menu = int(input("Digite a sua opção: "))
print('\033[35mFINALIZANDO...\033[m')
sleep(0.5)
print("Obrigada por participar")