print(" Sistema de Prestamo de libros")

DISTANCIA_PREMITIDA_KM = 3
tiene_credencial = input("¿Tiene credencial de estudiante? (S/N): ")
distancia_biblioteca_km = int(input("¿A cuántos km vives de la biblioteca?: "))
es_elegible_prestamo = tiene_credencial.strip().upper() == "S" or distancia_biblioteca_km <= DISTANCIA_PREMITIDA_KM

print("Eres elegible para un prestamo de libros? ", es_elegible_prestamo)