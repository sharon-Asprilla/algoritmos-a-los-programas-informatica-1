print("programa que (h) sirve para determinar la cantidad de los digitos de un numero ")
print()
n = input("ingrese un numero: ")

contador = 0

for digitos in n:
    contador += 1

print(f"La cantidad de dígitos de {n} es {contador}")

