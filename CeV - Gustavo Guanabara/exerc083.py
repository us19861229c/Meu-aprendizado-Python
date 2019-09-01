n = list(str(input("Digite a expressão: ")))
if n.count("(") == n.count(")"):
    print("A expressão está correta!")
else:
    print("A expressão não está correta!")