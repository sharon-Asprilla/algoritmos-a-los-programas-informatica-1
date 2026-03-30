print("Convertir binario a decimal")

decimal = 0 # acomulador del resultado en base 10
base = 1   # empieza en 2^0 ( representa la potencia)
residuo = 0 #cada digito que se extrae del binario

binario = int(input("Ingrese el número binario: "))

while binario > 0:
    residuo = binario % 10 #toma el ultimo numero del binario
    decimal = decimal + (residuo * base) # duma eldigito multplicado por la base
    base = base * 2
    binario = binario // 10   # división entera para quitar el último dígito

print("Decimal:", decimal)
