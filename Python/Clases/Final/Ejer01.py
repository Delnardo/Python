def CARGA(n):
    alumnos = {}
    for i in range(n):
        legajo = int(input("Ingrese legajo del alumno: "))
        while legajo <= 0:
            legajo = int(input("Ingrese un legajo válido (mayor que 0): "))
        
        apellido_nombre = input("Ingrese Apellido y Nombre del alumno: ")
        nota1 = float(input("Ingrese nota 1: "))
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input("Ingrese una nota válida (entre 0 y 10): "))
        
        nota2 = float(input("Ingrese nota 2: "))
        while nota2 < 0 or nota2 > 10:
            nota2 = float(input("Ingrese una nota válida (entre 0 y 10): "))
        
        alumnos[legajo] = [apellido_nombre, nota1, nota2]
    return alumnos

def BUSCA(legajo, diccionario):
    if legajo in diccionario:
        print("- Datos del alumno -")
        print(f"Legajo: {legajo}")
        print(f"Nombre: {diccionario[legajo][0]}")
        print(f"Nota 1: {diccionario[legajo][1]}")
        print(f"Nota 2: {diccionario[legajo][2]}")
    else:
        print(f"El legajo {legajo} no se encuentra registrado.")

def MUESTRA(diccionario):
    for legajo, datos in diccionario.items():
        print(f"Legajo: {legajo}, Nombre: {datos[0]}, Nota 1: {datos[1]}, Nota 2: {datos[2]}")

def main():
    print("*- Bienvenido al programa de control de notas de Alumnos -*")
    
    n = int(input("-> Ingrese la cantidad de alumnos: "))
    while n <= 0:
        n = int(input("* Error * -> Ingrese un valor válido (mayor que 0): "))
    
    alumnos = {}
    carga_realizada = False
    
    while True:
        print("\n*----------- Menú ----------*")
        print("1. Carga de datos")
        print("2. Búsqueda")
        print("3. Cálculo")
        print("4. Salir")
        
        opcion = int(input("-> Seleccione una opción: "))
        
        if opcion == 1:
            alumnos = CARGA(n)
            carga_realizada = True
        elif opcion == 2:
            if carga_realizada:
                legajo_buscar = int(input("Ingrese el legajo del alumno a buscar: "))
                BUSCA(legajo_buscar, alumnos)
            else:
                print("* Error -> Primero debe realizar la carga de datos. *")
        elif opcion == 3:
            if carga_realizada:
                MUESTRA(alumnos)
            else:
                print("* Error -> Primero debe realizar la carga de datos. *")
        elif opcion == 4:
            print("* Saliendo del programa. *")
            print("*- Gracias por usar nuestro sistema -*")
            break
        else:
            print("* Error -> Opción inválida. Por favor, elija una opción válida. *")

if __name__ == "__main__":
    main()