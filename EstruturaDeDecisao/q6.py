#Faça um Programa que leia três números e mostre o maior deles. 
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
n3 = float(input("Digite mais um número: "))
if n2 > n1 and n2 > n3:
    print(n2,'é o maior número')
elif n3 > n1 and n3 > n2:
    print(n3,'é o maior número')
else:
    print(n1,'é o maior número')