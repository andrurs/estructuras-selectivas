#Definir constantes
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

# Función para calcular el precio
def calcular_precio(tipo_hamburguesa, medio_pago, cantidad):
    # Definir precios segun el tipo de hamburguesa
    if  tipo_hamburguesa ==1:
        precio = PRECIO_SENCILLA
        descipcion = "Sencilla"
    elif tipo_hamburguesa == 2:
        precio = PRECIO_DOBLE
        descipcion = "Doble"
    elif tipo_hamburguesa ==3:
        precio = PRECIO_TRIPLE
        descipcion = "Triple"
    else:
        return None #Tipo de hamburguesa invalido

    # Calcular el total sin cargos
    total_sin_cargo = precio*cantidad

# Aplicar impuesto si el medio de pago es tarjeta
    if medio_pago ==1:
        impuesto = round(total_sin_cargo*IMPUESTO_TARJETA)
    else:
        impuesto = 0

    total = round(total_sin_cargo+impuesto)

    # Retornar datos relevantes
    return descipcion, precio, cantidad, impuesto, total

# Funcion para generar mensaje
def generar_mensaje(descipcion, precio, cantidad, impuesto, total):
    return (f"Tipo de Hamburguesa: {descipcion}"
            f"Precio: ${precio}\n"
            f"Cantidad: ${cantidad}\n"
            f"Impuesto: ${impuesto}\n"
            f"Total: ${total}")

#Función para validar los datos
def validar_datos(tipo_hamburguesa, medio_pago, cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <=3 and cantidad > 0:
        resultado = calcular_precio(tipo_hamburguesa, medio_pago, cantidad)
        #print("Resultado: ",resultado)
        descipcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descipcion, precio, cantidad, impuesto, total)
        print("------------------------------\n" + mensaje)
    else:
        print("Verifique las opciones ingresadas.")

# Entradas
tipo_hamburguesa = int(input("Ingrese tipo de hamburguesa \n1. Sencilla \n2. Doble \n3. Triple \n"))
medio_pago = int(input("Ingrese medio de pago \n1. Tarjeta \n2. Otro"))
cantidad = int(input("Ingrese la cantidad: "))

#Salidas
validar_datos(tipo_hamburguesa, medio_pago, cantidad)