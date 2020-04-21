#Coding in UTF-8
i = 0
while (i != "1"):
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    med = (n1+n2+n3+n4)/4
    if med > 10:
        print("Notas inválidas")
    else:
        print("Média:",med)
        break
    
