#Coding in UTF-8
i = "1" 
while(i == "1"):
    val = float(input("Quantos metros? "))
    print("Isso equivale:", val*100,"centimetros")
    q = input("Deseja continuar?(s/n) ")
    if q == "n":
        break