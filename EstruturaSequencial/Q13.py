#Coding in UTF-8
a = float(input("Digite sua altura: "))
g = input("Homem(h) ----- Mulher(m) \n")
if g == "h":
    r = (72.7*a) - 58
    print("Seu peso ideal é de:",round(r,2))
elif g == "m":
    r = (62.1*a) - 44.7
    print("Seu peso ideal é de:",round(r,2))
else:
    print("Gênero inválido!")

