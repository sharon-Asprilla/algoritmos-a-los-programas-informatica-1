print("programa (g) para calcular el consumo")
print()

consumo = int(input("ingrese el consumo: "))

estracto = int(input("ingrese el estrato: "))


if consumo <= 10 :
    precio = 6
elif  consumo >= 13 :
    precio =  5 
else: 
    precio = 9
subtotal = consumo * precio 
total = subtotal + 50 



if  estracto == 1 or estracto == 2:
    total = total -  (total *0.20)

print("total a pagar: ", total )




