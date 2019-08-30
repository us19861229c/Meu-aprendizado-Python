'''FAÇA UM PROGRAMA QUE LEIA NA TELA UM NUMERO INTEIRO, SEU ANTECESSOR E SEU SUCESSOR.
'''
# o numero N , seu antecessor (N - 1) e seu sucessor (N + 2)
n = int(input("Digite um numero: "))
print(f'o numero escolhido foi {n} , seu antecessor é {n-1} e o seu sucessor é {n+1}')
print(f'\n >>>NUMERO: {n:^10} \n >>>SUCESSOR: {n+1:^10} \n >>>ANTECESSOR: {n-1:^10}')