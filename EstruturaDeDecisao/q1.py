#Faça um Programa que peça dois números e imprima o maior deles. 
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
if n1>n2:
    print(n1,"é maior que",n2)
elif n1 == n2:
    print(n1,"é igual a",n2)
else:
    print(n2,"é maior que",n1)