productos = {}
continuar = "s"
print("*** Sistema de gestion de stock ***")
#ingresar productos
while continuar == "s":
    SKU = int(input("Ingrese el SKU del Producto "))
    desc = input("Ingrese descripcion del producto ")
    precio = float(input("Ingrese Precio de venta "))
    stock = int(input("Ingrese stock "))
    productos[SKU] = [desc, precio, stock]
    continuar = input("Desea cargar otro SKU.? s/n ")
    print("----------------------------------------")

for i in productos:
    print(
        "SKU",
        i,
        " Desc.",
        productos[i][0],
        " Precio",
        productos[i][1],
        " Stock",
        productos[i][2],
    )
print("--------------------------------------------")

# Buscar un SKU en particular
print("*** Busquemos un producto ***")
busqueda = int(input("Ingrese SKU del producto:"))
if busqueda in productos:
    i = busqueda
    print(
        "SKU",
        i,
        " Desc.",
        productos[i][0],
        " Precio",
        productos[i][1],
        " Stock",
        productos[i][2],
    )
else:
    print("No se encuentra el producto con SKU", i)
print("--------------------------------------------")

# listar productos con stock cero
print("*** Lista de productos sin stock ***")
for i in productos:
    if (productos[i][2]) <= 0:
        print("SKU:", (i), "Desc.:", productos[i][0], "Sin Stock")
