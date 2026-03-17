def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar gasto\n"))
    print(gasto)
    dinero = int(input("Dinero recibido\n"))
    print(dinero)
    print("\nVuelto")
    vuelto = dinero - gasto
    print("\nPesos:")
    print(int(vuelto))
    centavos = int((vuelto-int(vuelto))*100)
    print("Centavos:")
    print(centavos)
