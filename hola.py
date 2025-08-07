contactos = {}

while True:
    nombre = input(f"introduce nombre del contacto (o 'fin' para terminar): ")
    if nombre == "fin":
        break

    contactos[nombre] = []

    while True:
        telefono = input(f"introduce número de teléfono (o 'fin' para terminar: )")
        if telefono == "fin":
            break

        contactos[nombre].append(telefono)

        while True:
            telefono = input(f"introduce otro número de teléfono (o 'fin' para terminar: )")
            if telefono == "fin":
                break
            contactos[nombre].append(telefono)


print("\n📞 Contactos registrados:\n")
for nombre, telefono in contactos.items():
    lista_telefonos = ", ".join(telefono)
    print(f"{nombre} → {lista_telefonos}")
    
    





    