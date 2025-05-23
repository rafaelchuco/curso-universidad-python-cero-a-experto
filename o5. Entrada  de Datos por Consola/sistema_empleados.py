print("*** Sistema de Empleados ***")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))
is_boss = input("¿Es un jefe de departamento? (Si/No): ").lower() == "si"
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Salario: {salario:.2f}")
print(f"Es boss: {is_boss}")
