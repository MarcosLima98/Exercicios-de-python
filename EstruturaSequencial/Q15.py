#Conding in UTF-8
g = float(input("Quando você ganhar por hora: "))
h = float(input("Quantas horas trabalhadas no mês: "))
sb = g*h
inss = sb*0.08
sind = sb*0.05
ir = sb*0.11
print(10*"-")
print("Salário bruto:",sb)
print("INSS:",inss)
print("Sindicato:",sind)
print("Salário líquido:",sb-(inss+sind+ir))

