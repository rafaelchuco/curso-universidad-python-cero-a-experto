print ("***Operadores de asignacion****")
numero = 5
print(f"El numero es {numero}")
numero = 10
print(f"El numero es {numero}")
cadena = "Python"
print(f"La cadena es {cadena}")
cadena = "Java"
print(f"La cadena es {cadena}")

print("***Operadores de asignacion multiple***")
x, y, z = 5 , "hola", -9.3
print(f"El valor de x es {x}, el valor de y es {y} y el valor de z es {z}")

print("***Operadores de asignacion encadenada***")
a = b = c = 10
print(f"El valor de a es {a}, el valor de b es {b} y el valor de c es {c}")
# intercambio de valores de una variable sin utilizar variables temporales

x,y = 10,5
print(f"Los valores iniciales son: de x es {x} y el valor de y es {y}")

# Aplicando el concepto de asignacion multiple intercambiamos los valores
x,y = y,x
print(f"El valor de x es {x} y el valor de y es {y}")

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input("Ingrese su nombre y apellido separados por coma: ").split(" ,")
print(f"Su nombre es {nombre} y su apellido es {apellido}")