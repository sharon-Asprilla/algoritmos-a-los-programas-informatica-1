print("Programa para verificar seguridad de una contraseña")

contraseña = input("Ingrese la contraseña: ")
print()

contador = 0
# Verificar longitud
for c in contraseña:
    contador += 1

if contador >= 8 and contador <= 20:
    print("ok")
else:
    print("La contraseña no cumple con mínimo 8 y máximo 20 caracteres")

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

# ver si la palabra es palindroma 
invertida= ""
for c in contraseña:
    invertida = c + invertida
if contraseña == invertida:
    print("es palindroma")
else:
    print("ok")
    

