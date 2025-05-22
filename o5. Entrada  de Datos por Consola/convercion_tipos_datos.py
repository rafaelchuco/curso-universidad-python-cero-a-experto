# Conversión de tipos de datos

# Convertir de cadena a numero

numero_cadena = "10"
print(numero_cadena)
print(numero_cadena * 3)
numero_entero = int(numero_cadena)
print(numero_entero)
print(numero_entero * 3)

# Convertir de cadena a flotante

numero_cadena = "3.14"
print(numero_cadena)
print(numero_cadena * 3)
numero_flotante = float(numero_entero)
print(numero_flotante)
print(numero_flotante * 3)

# Convertir de numero a cadena
numero_entero = 20
numero_cadena = str(numero_entero)
print(numero_cadena)

# Convertir de numero a booleano

# Tipo booleano es falso en los siguientes casos
# Si el valor es 0
# Si el valor es una cadena vacía
# Si el valor es None

# Si el valor es verdadero en los siguientes casos
# Si el valor es distinto de 0
# Si el valor es una cadena no vacía
# Si el valor es no None

numero_entero = 0
numero_booleano = bool(numero_entero)
print(numero_booleano)

numero_entero = 5
numero_booleano = bool(numero_entero)
print(numero_booleano)

cadena = ""
cadena_bool = bool(cadena)
print(cadena_bool)

cadena = "hola"
cadena_bool = bool(cadena)
print(cadena_bool)

variable = None
variable_bool = bool(variable)
print(variable_bool)

variable = "hola"
variable_bool = bool(variable)
print(variable_bool)








