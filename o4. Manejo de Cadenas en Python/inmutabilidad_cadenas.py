# Inmutabilidad de cadenas
cadena1 = "Hola mundo"
print(cadena1) 
#cadena1[0] = h # No podemos modificar los caracteres

cadena1 = "Adios"
print(cadena1) 

cadena2 = cadena1
cadena1 = "Vegeta"
cadena2 = "Goku"
print(cadena1)
print(cadena2)
