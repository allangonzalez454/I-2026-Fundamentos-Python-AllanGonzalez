archivo = open("Clase_06\Info_del_estudiante.txt","a")
 
while True:
    print("1. Ingresar datos del estudiante")
    print("2. salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("Ingrese los datos del estudiante")

        nombre = input("Ingrese el nombre del estudiante: ")
        Carne = input("ingrese el numero de carne:")
        Nota_final = input("ingrese la nota final del estudiante:")
    elif opcion == 2:
     break

    archivo.write("Nombre del estudiante: " + nombre +"\n")
    archivo.write("Numero de carne: " + Carne + "\n" )
    archivo.write("Nota final: " + Nota_final + "\n")

    

archivo.close()