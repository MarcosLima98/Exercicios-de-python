#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
gen = input("Qual o seu gênero? (M/F) \n")
if gen == 'm':
    print("Você é gênero masculino")
elif gen == 'f':
    print("Você é o gênero feminino")
else:
    print("Gênero inválido")
