def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """


    nombre_completo = input("Ingrese nombre: ").strip().title()
    email = input("Ingrese email: ")
    nota_1 = int(input("Ingrese nota 1: "))
    nota_2 = int(input("Ingrese nota 2: "))
    nota_3 = int(input("Ingrese nota 3: "))
    espacio = nombre_completo.find(" ")
    nombre = nombre_completo[:espacio]
    apellido = nombre_completo[espacio + 1:]

    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_completo}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")
    print(f"Iniciales: {nombre_completo[0] + nombre_completo[espacio + 1]}")
    print(f"Usuario: {apellido.lower() + '.'+nombre.lower()}")
    print(f"Email valido: {'@' in email}")
    dominio = email[email.find('@') + 1:].lower()
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombrecompleto.replace(' ', '')}")
    print(f"Cantidad de a: {nombre_completo.lower().count('a')}")
    print(f"Codigo secreto: {nombre_completo[::-1].upper()}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    suma = nota_1 + nota_2 + nota_3
    print(f"Suma: {suma}")
    print(f"Promedio: {float(suma / 3)}")
    print(f"Promedio entero: {int(suma / 3)}")
    print("========================")
💀
tinopesce — 3/17/26, 7:46 PM
Image
tano — 3/17/26, 8:11 PM
nombre_completo = input("Ingrese nombre: ").strip().title()
    email = input("Ingrese email: ").lower()
    nota_1 = int(input("Ingrese nota 1: "))
    nota_2 = int(input("Ingrese nota 2: "))
    nota_3 = int(input("Ingrese nota 3: "))
    espacio = nombre_completo.find(" ")
    nombre = nombre_completo[:espacio]
    apellido = nombre_completo[espacio+1:]

    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_completo}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")
    print(f"Iniciales: {nombre_completo[0] + nombre_completo[espacio + 1]}")
    print(f"Usuario: {apellido.lower() + '.' + nombre.lower()}")
    print(f"Email valido: {'@' in email}")
    dominio = email[email.find('@') + 1:].lower()
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombrecompleto.replace(' ', '')}")
    print(f"Cantidad de a: {nombre_completo.lower().count('a')}")
    print(f"Codigo secreto: {nombre_completo[::-1].upper()}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {nota_1 + nota_2 + nota_3}")
    print(f"Promedio: {float((nota_1 + nota_2 + nota_3)/3)}")
    print(f"Promedio entero: {int((nota_1 + nota_2 + nota_3)/3)}")
    print("=" * 24)
