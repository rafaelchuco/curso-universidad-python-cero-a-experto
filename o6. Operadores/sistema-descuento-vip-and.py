print("*** Sistema de descuento VIP usando AND ***")

NO_PRODUCTOS_DESCUENTO = 10
cantidad_pructos_por_dia = int(input("Cuantos productos compraste hoy: "))
tine_membresias = input("Tienes membresias? (S/N): ").upper()

es_elegible_descuentoVIP = cantidad_pructos_por_dia >= NO_PRODUCTOS_DESCUENTO and tine_membresias == "S"
print(f"Es elegible el descuento VIP? {es_elegible_descuentoVIP}")