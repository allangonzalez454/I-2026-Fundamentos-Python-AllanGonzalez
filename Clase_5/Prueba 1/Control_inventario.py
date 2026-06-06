print("Ingrese la cantidad de productos que desea agregar al inventario")
Productos = int(input("Ingrese la cantidad de productos: "))
 
contador = 0

valor_total = 0


while contador < Productos:
    print("Nombre de los productos")
    Nombre_productos = input("Ingrese el nombre del producto: ")

    Precio = int(input("Ingrese el precio del producto: "))
    Cantidad = int(input("Ingrese la cantidad disponible: "))

    Valor_total = Precio * Cantidad
    print(f"El valor total del inventario es: {Valor_total}")
    print(f"Nombre del producto: {Nombre_productos}")

contador += 1                                   
    
    
    
   
    
    
    
    
     
