print("prgrama (j) para Convertir binario a decimal")

decimal = 0 # acomulador del resultado en base 10
residuo= 1   # empieza en 2^0 ( representa la potencia)
potencia = 0 #cada digito que se extrae del binario

binario = int(input("Ingrese el número binario: "))

while binario > 0:
    residuo = binario % 10 #toma el ultimo numero del binario
    decimal = decimal + (residuo * (2 **potencia)) # duma eldigito multplicado por la potencia
    binario = binario // 10   # división entera para quitar el último dígito
    potencia = potencia + 1 # sigue ala siguente potencia

print("Decimal:", decimal)
