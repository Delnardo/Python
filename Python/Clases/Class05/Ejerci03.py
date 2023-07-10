#my_list=[1,2,3,4,5]
#new_list=my_list[-1:-4:-1]
#print(new_list)

#car_1=("hola","como")
#print(car_1)

clientes = {123456789: "Juan", 456123789: "Luis", 789456123: "Jose", 123789456: "Raul"}

dni = int(input("Ingrese el DNI: "))

if dni in clientes:
    nombre = clientes[dni]
    print("El nombre asociado al DNI", dni, "es:", nombre)
else:
    print("No se encontró un cliente con el DNI ingresado.")