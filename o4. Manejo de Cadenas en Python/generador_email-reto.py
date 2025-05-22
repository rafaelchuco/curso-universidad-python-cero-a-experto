# Generador de Emails
print("*** Generador de Emails ***")

nombre = "Rafael Diego Chuco Yantas"
empresa = "Python Academy"
dominio = "com"

print("Nombre de usuario: ", nombre)
nombre_normalizado = nombre.lower().replace(" ", ".")
print("Nombre de usuario normalizado: ", nombre_normalizado)

print("Nombre de empresa: ", empresa)
print("Extendion de dominio: ", dominio)
dominio_normalizado = empresa.lower().replace(" ", "") + "." + dominio
print("Dominio de email normalizado:", dominio_normalizado)
email = nombre_normalizado + "@" + dominio_normalizado
print("Email generado: ", email)



