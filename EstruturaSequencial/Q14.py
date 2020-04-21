#Coding in UTF-8
r = float(input("Rendimento da pesca em Kg: "))
if r > 50:
    ex = r - 50
    print("Você prescou",r,"Kg.")
    print("Você excedeu",ex,"e deve pagar R$",ex*4.00,"de multa.")
else:
      print("Você prescou",r,"Kg.")
      print("Você não excedeu o limite.")