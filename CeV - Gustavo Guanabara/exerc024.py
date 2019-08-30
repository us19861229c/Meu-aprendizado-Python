#024: Crie um programa que leia o nome de uma cidade e
# diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Qual o nome da cidade? ")).strip().upper()
if cidade.find("SANTO") == 0:
    print("Essa cidade começa com o nome 'Santo'.")
else:
    print("Essa cidade não começa com o nome 'Santo'.")