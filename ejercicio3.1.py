print("Programa para identificar un carácter")

caracter = input("Ingrese un carácter: ")

# primero se comparaa si es un digito
if caracter >= "0" and caracter <= "9":
    print(caracter, "es un dígito")

# si no es digito, ve  si es una letra
elif (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z"):
    # se ve si es vocal
    if caracter in "AEIOUaeiou":
        tipo = "vocal"
    else:
        tipo = "consonante"

    # se compara si es mayuscula o minuscula
    if caracter >= "A" and caracter <= "Z":
        print(caracter, "es una", tipo, "mayúscula")
    else:
        print(caracter, "es una", tipo, "minúscula")

#  y si no es ni digito ni letra
else:
    print(caracter, "no es ni letra ni dígito")
