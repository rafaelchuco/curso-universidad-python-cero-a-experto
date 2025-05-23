from random import randint
print("***Sistema Generador de ID Unico***")

print("***Ingrese los siguientes datos***")
nombre =  input("ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nacimiento = input("Ingrese su fecha de nacimiento(yyyy): ")

id = nombre.upper()[0:2] + apellido.upper()[0:2] + nacimiento[2:4] + str(randint(1000, 9999))
print(f"Hola {nombre}, \n \t Tu número de identificación ID generado por el sistema es: {id} \n \t Gracias por usar nuestro sistema." )