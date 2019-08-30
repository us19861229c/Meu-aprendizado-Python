#criar tupla com palavras, depois mostrar todas as vogais da palavra

tupvog = ("arara", "peixe", "coruja", "papagaio", "cachorro", "gato", "guaxinim")
for p in tupvog:
    print(f"\nNa palavra {p.upper()} as \033[34mvogais\033[m são ", end="")
    for vog in p:
        if vog.lower() in "aeiou":
            print(vog, end=" ")
    print(".\n E as \033[35mconsoantes\033[m são", end=" ")
    for vog in p:
        if vog.lower() not in "aeiou":
            print(vog, end=" ")
