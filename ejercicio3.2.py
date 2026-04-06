print("Programa para cambiar espacios por un signo elegido")


oracion = input("Ingrese una oración: ")


signo = input("Ingrese el signo por el cual quiere cambiar los espacios: ")

resultado = ""

# se recorreo  cada carácter de la oración con el in
for caracter in oracion:
    if caracter == " ":
        resultado = resultado + signo
    else:
        resultado = resultado + caracter

print("resultado de la oracion:", resultado)
