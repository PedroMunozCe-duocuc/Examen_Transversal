peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

opcion=None

def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
def leer_opcion():
    try:
        opcion=int(input("Ingrese opción: "))
        return opcion
    except:
        print("Ingrese opción válida")

def validar_titulo(titulo):
    if titulo !=" ":
        return True
    else:
        print("Título no válido")
        return False
def validar_genero(genero):
    if genero!=" ":
        return True
    else:
        print("Género no válido")
        return False
def valida_duracion (duracion):
    if duracion>0:
        return True
    else:
        print("Duración no válida")
        return False
def vaidar_clasificacion(clasificacion):
    if clasificacion=="A" or clasificacion=="B" or clasificacion=="C":
        return True
    else:
        print("Clasificación no válida")
        return False
def validar_idioma(idioma):
    if idioma!=" ":
        return True
    else:
        print("Idioma no válido")
        return False
def validar_3d(tresde):
    tresde=tresde.upper()
    if tresde.lower()=="s" or tresde.lower()=="n":
        return True
    else:
        print("Formao no válido")
        return False
def validar_precio(precio):
    if precio>=0:
        return True
    else:
        print("Precio no válido")
        return False
def validar_cupos(cupos):
    if cupos>=0:
        return True
    else:
        print("Cupos inválidos")
        return False
def buscar_codigo(peliculas,codigo):
    if codigo in peliculas:
        return True
    else:
        print("Codigo no encontrado")
        return False
    

def cupos_genero(peliculas, cartelera):
    total_cupos=0
    genero=input("Ingrese género de película: ")
    for codigo in peliculas:
        if peliculas[codigo][1].upper()==genero.upper():
            total_cupos+=cartelera[codigo][1]
    print(f"El total de cupos para el género {genero} es de {total_cupos}")

def buscar_precio(peliculas, cartelera):
    precio_min=int(input("Ingrese el monto mínimo: "))
    precio_max=int(input("Ingrese el monto máximo: "))
    encontrado=False
    for codigo in cartelera:
        precio=cartelera[codigo][0]
        if precio >= precio_min and precio <= precio_max: 
            print (codigo)
            print (peliculas[codigo][0])
            print(precio, "$")
            encontrado=True
    if encontrado==False:
        print("No se han encontrado películas en ese rango de precio")

def acualizar_precio(cartelera):
    codigo=input("Ingrese el código de la película: ")
    codigo=codigo.upper()
    if buscar_codigo(cartelera, codigo):
        print("Código encontrado")
        respuesta=input("¿Desea acualizar el precio de esta película? (s/n): ")
        while True: 
            if respuesta=="s":
                nuevo_precio=int(input("Ingrese precio acualizado: "))
                if validar_precio(nuevo_precio):
                    print("Nuevo precio válido.")
                    cartelera[codigo][0]=nuevo_precio
                    break
                else:
                    print("Precio no válido.")

def agregar_pelicula(peliculas, cartelera):
    codigo=input("Ingrese codigo de la película a agregar: ")
    codigo=codigo.upper()
    if buscar_codigo(peliculas, codigo):
        print("Código válido")
        return
    while True:
        titulo=input("Ingrese el título de la nueva película: ")
        if validar_titulo(titulo):
            print("Nombre disponible")      
            break      
    while True:
        genero=input("Ingrese género de la película: ") 
        if validar_genero(genero):
            print("Género disponible")
            break
    while True:
        try:
            duracion=int(input("Ingrese duración de la película: "))
            if valida_duracion(duracion):
                print("Duración válida")
                break
        except:
            print("Debe ingresar un número")
    while True:
        clasificacion=input("Ingrese clasificación de la película (A,B,C): ")
        if vaidar_clasificacion(clasificacion):
            print("Clasificación válida")
            break
    while True:
        idioma=input("Inrese el idioma de la película: ")
        if validar_idioma(idioma):
            print("Idioma válido")
            break
    while True:
        tresde=input("Es una película 3d (S/N): ")
        if validar_3d(tresde):
            break
        if tresde.upper()=="S":
            tresde=True
        else:
            tresde=False
    while True:
        try:
            precio=int(input("Ingrese precio de la película: "))
            if validar_precio(precio):
                print("Precio válido.")
                break
        except:
            print("Debe ingresar un número.")
    while True:
        try:
            cupos=int(input("¿Cuántos cupos posee la película?: "))
            if validar_cupos(cupos):
                print("Cupos válidos")
                break
        except:
            print("Debe inresar números.")
    peliculas[codigo]=[titulo, genero, duracion, clasificacion, idioma, tresde
                       ]
    cartelera[codigo]=[precio, cupos
                       ]
    
def eliminar_pelicula(peliculas, cartelera):
    codigo=input("Ingrese código de película a eliminar: ")
    codigo = codigo.upper()
    if buscar_codigo(peliculas, codigo):
        peliculas.pop(codigo)
        cartelera.pop(codigo)
        print(f"La película se ha eliminado")
   


while opcion!=6:
    menu_principal()
    opcion=leer_opcion()
    match opcion:
        case 1:
            cupos_genero(peliculas, cartelera)
        case 2:
            try:
                buscar_precio(peliculas, cartelera)
            except:
                print("Debe ingresar valores enteros")
        case 3:
            try:
                acualizar_precio(cartelera)
            except:
                print("Debe ingresar datos válidos.")
        case 4:
            agregar_pelicula(peliculas, cartelera)
        case 5:
            eliminar_pelicula(peliculas, cartelera)
        case 6:
            print("Programa finalizado")
        case _:
            print("Opción no disponible")
            