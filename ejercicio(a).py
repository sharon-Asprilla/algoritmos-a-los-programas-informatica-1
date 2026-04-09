print("Programa (a) para calcular la hipotenusa ")

# Pedir los catetos
cateto1 = int(input("Ingrese el primer cateto: "))
cateto2 = int(input("Ingrese el segundo cateto: "))

# Calcular la suma de cuadrados
suma = (cateto1 * cateto1) + (cateto2 * cateto2)
#se multiplica y se suma ya que se eleva ala dos entonces multiplicamos el mismo numero por si mismo y luego se suma

#inicializamos las variables aca para poderlas usar en el bucle del while
hipotenusa = 0
i = 1

while i * i <= suma:   # mientras el cuadrado de i sea menor o igual a la suma
    hipotenusa = i
    i = i + 1

# Mostrar resultado
print("La hipotenusa es:", hipotenusa)
