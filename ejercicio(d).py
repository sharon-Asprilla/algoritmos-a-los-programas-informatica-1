print("este programa (d) sirve para calcular el salario semanal de la sucursal")
print()
sucursal= input("ingrese la surcursal en la que trabaja(A y B) en mayuscula: ")

horas= int(input("ingresa las horas trabajadas: "))

pago_sucursal_a = 10 
pago_hora_extra_sucursal_a = 20
horas_sucursal_a = 39
horas_extra_a = horas - horas_sucursal_a 

#variables de sucursales b
pago_sucursal_b = 12
pago_hora_extra_sucursal_b = 25
horas_sucursal_b = 44
horas_extra_b = horas - horas_sucursal_b

if sucursal == "A":
    if horas > horas_sucursal_a:
        salario_semanal = (pago_sucursal_a * horas_sucursal_a) + (pago_hora_extra_sucursal_a * horas_extra_a)
    else:
        salario_semanal =pago_sucursal_a * horas
else:
    if horas> horas_sucursal_b:
        salario_semanal = pago_sucursal_b * horas 
    else:
        salario_semanal = (pago_sucursal_b * horas_sucursal_b ) + ( pago_hora_extra_sucursal_b * horas_extra_b)

print("el salario semanal de el trabajo es de $: ", salario_semanal)
