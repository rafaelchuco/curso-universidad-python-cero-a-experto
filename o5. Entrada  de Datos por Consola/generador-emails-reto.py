print("***Sistema Generador de Emails***")
nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
empresa = input("Ingrese su empresa: ")
dominio = input("Ingrese su dominio: ")

nombre = nombre.lower().replace(" ", ".")
apellidos = apellidos.lower().replace(" ", ".")
empresa = empresa.lower().replace(" ", ".")
dominio = dominio.lower()

email = f"{nombre}.{apellidos}@{empresa}.{dominio}"
print(f"Tu email es: {email}")