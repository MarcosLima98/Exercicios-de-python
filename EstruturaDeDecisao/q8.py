#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato. 
p1 = float(input("Preço 1: "))
p2 = float(input("Preço 2: "))
p3 = float(input("Preço 3: "))
if p2 < p1 and p2 < p3:
    print(p2,'é o menor preço')
elif p3 < p2 and p3 < p1:
    print(p3,'é o menor preço')
else:
    print(p1,'é o menor preço')
    