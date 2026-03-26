print("algoritmo para  calcular las millas/hora")

millas= int(input("ingrese la velocidad en millas:  "))

kmh= millas * 1609
ms= kmh * 1000/3600

print(f"las millas/hora son: {millas} equivale a kmh: {kmh} y a ms: {ms} ")