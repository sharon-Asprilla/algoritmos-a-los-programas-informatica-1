print("Programa para verificar seguridad de una contraseña")

contraseña = input("Ingrese la contraseña: ")

# Verificar longitud
for c in contraseña:
    if (c >= 8 and c <= 20):
        print("ok")
    else:
        print(" La contraseña no cumple con minimo 8 y 20 caracteres")

#  Verificar si tiene letras
tiene_letra = False
for c in contraseña:
    if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z"):
        tiene_letra = True
        
if tiene_letra:
    print(" ok")
else:
    print(" No contiene letras")

# 3. Verificar si tiene números
tiene_numero = False
for c in contraseña:
    if c >= "0" and c <= "9":
        tiene_numero = True
        

if tiene_numero:
    print(" ok")
else:
    print(" No contiene números")

# 4. Verificar si tiene caracteres especiales
especiales = '!"#$%&/()=?+*'
tiene_especial = False
for c in contraseña:
    if c in especiales:
        tiene_especial = True
        

if tiene_especial:
    print(" ok")
else:
    print(" No contiene caracteres especiales")

#falta verificar si la palabra es palindroma 