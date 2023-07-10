estudiantes = {}
continuar = "s"
repetir = "s"
contador = 0
while repetir == "s":
    print("*** Sistema de gestion estudiantil ***")
    print("--------------------------------------------")
    print("Ingrese 1 para añadir estudiantes")
    print("Ingrese 2 para saber la cantidad de alumnos")
    print("Ingreso 3 para mostrar los estudiantes registrados.")
    print("Ingrese 4 para mostrar el promedio mas alto")
    print("Ingrese 5 para salir del programa")
    opcion = int(input("ingrese una opcion"))
    
    if opcion==1:
        # ingresar datos de estudiantes
        while continuar == "s":
            nombre = (input("Ingrese nombre completo del alumno ")).upper()
            nota1 = float(input("Ingrese nota 1 "))
            nota2 = float(input("Ingrese nota 2 "))
            promedio = (nota1 + nota2) / 2
            estudiantes[nombre] = [nota1, nota2, promedio]
            continuar = input("Desea cargar otro alumno.? s/n ")
            contador += 1
            print("----------------------------------------")
    elif opcion==2:
        #contador de estudiantes
        print("Hay un total de", contador, "estudiantes cargados")
        print("---------------------------------------------")
    elif opcion==3:
        #mostrar lista de estudiantes y sus notas
        for i in estudiantes.items():
            print(i)
        print("--------------------------------------------")
    elif opcion==4:
        #Mostrar promedio mas alto
        maxNota=0
        nombreNotaMayor={}
        nombreNotaMayor[nombre]=[nota1,nota2,promedio]
        for i in estudiantes:
            if maxNota < estudiantes[i][2]:
                maxNota = estudiantes[i][2]
                nombreNotaMayor[nombre]= estudiantes[nombre]
            else :
                continue

        print ("El mayor promedio es:", maxNota,"de",nombreNotaMayor.items())
    elif opcion==5:
        print("Gracias por usar nuestro sistema")
        repetir="n"
        break
    else:
        print("Opcion no valida")
       
