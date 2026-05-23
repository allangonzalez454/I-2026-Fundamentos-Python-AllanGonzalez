print("Cajero Automatico")
print("Bienvenido al cajero automatico")
Saldo = 0

while True:
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:

        print(f"Su saldo es: {Saldo}")
    elif opcion == 2:
        cantidad = int(input("ingrese la catidad de retirar:"))
        if cantidad > Saldo:
            print("No tiene suficiente saldo")
        else:
            Saldo = Saldo - cantidad
            print(F"Ha retirado: {cantidad}")
    elif opcion == 3:
        cantidad = int(input("ingrese la cantidad que desea depositar:"))
        Saldo = Saldo + cantidad
        print(f"Ha depositado: {cantidad}")
    elif opcion == 4:
        print("Gracias por usar el cajero automatico")
        break
    else:
        print("Opcion no valida")     


            




         