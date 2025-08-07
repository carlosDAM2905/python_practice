# Simular una encuesta donde los clientes valoran distintos aspectos de un servicio (por ejemplo, un restaurante) del 1 al 5.
cliente = {}

while True:
    nombreCliente = input("Introduce tu nombre ('fin para salir de la encuesta'): ")
    if nombreCliente == "fin":
        break

    comida = float(input("comida 1-5:\n"))
    while comida  < 1 or comida > 5:
        comida = float(input("¡La puntuación debe ser entre 1 y 5!\ncomida 1-5:\n"))

    servicio = float(input("servicio 1-5\n"))
    while servicio  < 1 or servicio > 5:
        servicio = float(input("¡La puntuación debe ser entre 1 y 5!\ncomida 1-5:\n"))

    ambiente = float(input("ambiente 1-5:\n"))
    while ambiente  < 1 or ambiente > 5:
        ambiente = float(input("¡La puntuación debe ser entre 1 y 5!\ncomida 1-5:\n"))

    cliente[nombreCliente] = {
        'comida': comida,
        'servicio': servicio,
        'ambiente': ambiente
        }
    
    
# analisis de la encuesta:
totalComida = 0
totalServicio = 0
totalAmbiente = 0
totalClientes = len(cliente)
mejorCliente = ""
mejorValoracion = 0



for usuario, info in cliente.items():
    
    print(f"{usuario}:")
    print(f" comida: {info['comida']}")
    print(f" servicio: {info['servicio']}")
    print(f" ambiente: {info['ambiente']}")


    promedio = (info['comida'] + info['servicio'] + info['ambiente']) / 3

    if promedio > mejorValoracion:
        mejorValoracion = promedio
        mejorCliente = usuario
    
    


for info in cliente.values():
    totalComida += info['comida']
    totalServicio += info['servicio']
    totalAmbiente += info['ambiente']

print("\n===Estadísticas encuesta===")
print("media global comida: ", totalComida / totalClientes)
print("media global servicio: ", totalServicio / totalClientes)
print("media global ambiente: ", totalAmbiente / totalClientes)
print(f"el cliente con mejor valoración es {mejorCliente} con una valoración media de: {mejorValoracion:.2f}")





    

    

