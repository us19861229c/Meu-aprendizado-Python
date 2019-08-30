
produtos_prec = ("Croissant", 2.0, "Leite", 5.0, "Mix de grãos", 8.0 , "Mix de nozes", 7.55,
                 "Café", 3.45, "Bolo", 13.66, "Torta gelada", 6.77, "Suco", 3.27 )
print("="*38)
print(f"{'LISTAGEM  DE  PREÇOS':^38}")
print("="*38)
prod = 0
while prod < len(produtos_prec):
    print(f'{produtos_prec[prod]:.<28}R$ {produtos_prec[prod+1]:>5.2f}')
    prod +=2
