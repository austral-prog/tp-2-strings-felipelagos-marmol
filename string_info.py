def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    repetir = palabra * 3
    decorar = ("***" + palabra + "***")
    print(f"Palabra: {palabra}")
    print(f"Longitud: {len(palabra)}")
    print(f"Primera letra: {palabra[0]}")
    print(f"Ultima letra: {palabra[-1]}")
    print(f"Repetida: {repetir}")
    print(f"Decorada: {decorar}")
