def agregar_producto (productos):
    producto = input("Agregar un producto: ").strip().lower()
    stock = int(input("Ingrese la cantidad: "))

    if producto in productos:
        productos[producto] += stock
        print("Producto existente, modificación en el stock.")
    
    else:
        productos[producto] = stock
        print("Producto agregado con éxito.")
    

def mostrar_productos (productos):
    print("\nLISTA DE PRODUCTOS")
    if not productos:
        print("El inventario está vacio.")
    
    else:
        for producto, stock in productos.items():
            print(producto, ":", stock)


def buscar_producto (productos):
    print("\nBUSCAR PRODUCTO")
    #Quitar espacios y todo a minúsculas
    nombreProducto = input("Nombre del producto: ").strip().lower()

    if nombreProducto in productos:
        stockProducto = productos[nombreProducto]
        print(f"Producto: {nombreProducto}      Cantidad: {stockProducto}")
    
    else:
        print("No existe dicho producto.")

def main():
    inventario = {
        "chocolate": 15,
        "arroz": 20
    }

    while True:
        print("\nMENÚ")
        print("1. Agregar o actualizar producto.")
        print("2. Mostrar inventario completo.")
        print("3. Buscar producto por nombre.")
        print("4. Salir")

        opcion = input("Elige la opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            print("Se salió del programa.")
            break
        else:
            print("Opción inválida, inténtelo de nuevo.")


main()