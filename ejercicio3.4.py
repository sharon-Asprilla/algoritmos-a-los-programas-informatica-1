print("Programa: ocultar mensajes")

mensaje = input("Ingrese un mensaje: ")

pares = ""
impares = ""

indice = 0
for caracter in mensaje:
    # Cambiar vocales por números
    if caracter == "a" or caracter == "A":
        caracter = "1"
    elif caracter == "e" or caracter == "E":
        caracter = "2"
    elif caracter == "i" or caracter == "I":
        caracter = "3"
    elif caracter == "o" or caracter == "O":
        caracter = "4"
    elif caracter == "u" or caracter == "U":
        caracter = "5"

    # Separar pares e impares
    if indice % 2 == 0:
        pares = pares + caracter
    else:
        impares = impares + caracter

    indice = indice + 1

mensaje_oculto = pares + impares

print("Mensaje original:", mensaje)
print("Mensaje oculto:", mensaje_oculto)
