
productos={}
opcion=-1
while(opcion!=0):
    print("Bienvenido a la base de datos del kiosco, seleccione una opción:")
    print("1 Agregar un producto"+"\n2 Eliminar un producto"+ "\n3 Mostrar inventario"+"\n0 Salir del programa")
    opcion=(int(input()))
    match opcion:
        case 1:
                nom=str(input("Ingrese el nombre del producto: "))
                if (nom not in productos):
                     productos[nom]=int(input("Ingrese la cantidad inicial del producto: "))
                else:
                     print("Error: El producto ya existe")
        case 2:
                nom=input("Ingrese el nombre del producto a eliminar: ")
                if (nom in productos):
                      del productos[nom]
                else: print("Error: El producto no existe")
        case 3:
                for key in productos:
                      print(f"|Producto: {key} | Cantidad: {productos[key]}|")
        case 0:
                print("Hasta luego")